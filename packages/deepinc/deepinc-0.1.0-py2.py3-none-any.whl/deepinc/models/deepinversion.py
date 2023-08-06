import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset

import math
import numpy as np
import copy

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel


def loss_fn_kd(scores, target_scores, allowed_predictions, T=2., soft_t=False):
    """Compute knowledge-distillation (KD) loss given [scores] and [target_scores].
    Both [scores] and [target_scores] should be tensors, although [target_scores] should be repackaged.
    'Hyperparameter': temperature"""

    log_scores_norm = F.log_softmax(scores[:, allowed_predictions] / T, dim=1)
    if soft_t:
        targets_norm = target_scores
    else:
        targets_norm = F.softmax(target_scores[:, allowed_predictions] / T, dim=1)

    # Calculate distillation loss (see e.g., Li and Hoiem, 2017)
    KD_loss_unnorm = -(targets_norm * log_scores_norm)
    KD_loss_unnorm = KD_loss_unnorm.sum(dim=1)  # --> sum over classes
    KD_loss_unnorm = KD_loss_unnorm.mean()  # --> average over batch

    # normalize
    KD_loss = KD_loss_unnorm  # * T**2

    return KD_loss


class DeepInversion(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(DeepInversion, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.batch_size = args.batch_size
        self.net = None

        self.inversion_replay = False
        self.previous_teacher = None
        self.power_iters = self.args.power_iters
        self.mu = self.args.mu
        self.DTemp = 2
        self.deep_inv_params = self.args.deep_inv_params

        self.criterion = nn.CrossEntropyLoss()
        self.kd_criterion = nn.MSELoss(reduction="none")

        self.current_task = 0
        self.last_valid_out_dim, self.valid_out_dim = 0, 0

    def begin_il(self, dataset):
        if self.args.dataset == 'seq-cifar100' \
                or self.args.dataset == 'seq-cifar10' \
                or self.args.dataset == 'seq-tinyimg':

            if self.args.featureNet:
                self.net = MNISTMLP(1000, dataset.nc, hidden_dim=[500, 800]).to(self.device)
                self.generator = Generator_MLP(zdim=1000, img_sz=1000, mid_dim=1000, is_img=False).to(self.device)
                self.generator_optimizer = Adam(params=self.generator.parameters(), lr=self.learning_rate / 10)
            else:
                self.net = resnet18(dataset.nc).to(self.device)
                self.generator = Generator(zdim=1000, in_channel=dataset.n_channel, img_sz=dataset.n_imsize1).to(
                    self.device)
                self.generator_optimizer = Adam(params=self.generator.parameters(), lr=self.learning_rate)
        else:
            self.net = MNISTMLP(28 * 28, dataset.nc).to(self.device)
            self.generator = Generator_MLP(zdim=1000, img_sz=28).to(self.device)
            self.generator_optimizer = Adam(params=self.generator.parameters(), lr=self.learning_rate / 10)

        self.optimizer = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.valid_out_dim += len(self.t_c_arr[self.current_task])
        self.train_(train_loader)
        self.last_valid_out_dim = self.valid_out_dim

        self.current_task += 1

        # for eval
        if self.previous_teacher is not None:
            self.previous_previous_teacher = self.previous_teacher

        if self.args.dataset == 'seq-mnist':
            img_shape = (-1, 1, 28, 28)
        else:
            img_shape = (-1, dataset.n_channel, dataset.n_imsize1, dataset.n_imsize1)
        self.previous_teacher = Teacher(solver=copy.deepcopy(self.net), generator=self.generator,
                                        gen_opt=self.generator_optimizer,
                                        img_shape=img_shape,
                                        iters=self.power_iters, deep_inv_params=self.deep_inv_params,
                                        class_idx=np.arange(self.last_valid_out_dim), device=self.device)
        self.sample(self.previous_teacher, self.batch_size, self.device, return_scores=False)

        self.inversion_replay = True

        # used for always be dreaming
        self.previous_classifier = copy.deepcopy(self.net.classifier)

    def train_(self, train_loader):
        self.net.train()
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                x, y = data[0].to(self.device), data[1].to(self.device)

                # data replay
                if self.inversion_replay:
                    x_replay, y_replay, y_replay_hat = self.sample(self.previous_teacher, len(x), self.device)


                # if KD
                if self.inversion_replay:
                    y_hat = self.previous_teacher.generate_scores(x, allowed_predictions=np.arange(
                        self.last_valid_out_dim))
                    _, y_hat_com = self.combine_data(((x, y_hat), (x_replay, y_replay_hat)))
                else:
                    y_hat_com = None

                # combine inputs and generated samples for classification
                if self.inversion_replay:
                    x_com, y_com = self.combine_data(((x, y), (x_replay, y_replay)))
                else:
                    x_com, y_com = x, y

                # model update
                loss, loss_class, loss_kd, output = self.update_model(x_com, y_com, y_hat_com,
                                                                      kd_index=np.arange(len(x), len(x_com)))

            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))

    def update_model(self, inputs, targets, target_scores=None, kd_index=None):

        loss_kd = torch.zeros((1,), requires_grad=True).cuda()

        # forward pass
        logits = self.net(inputs)[:, :self.valid_out_dim]

        # classification
        loss_class = self.criterion(logits, targets.long())

        # KD old
        if target_scores is not None:
            loss_kd = self.mu * loss_fn_kd(logits, target_scores,
                                           np.arange(self.last_valid_out_dim).tolist(), self.DTemp)

        # KD new
        if target_scores is not None:
            target_scores = F.softmax(target_scores[:, :self.last_valid_out_dim] / self.DTemp, dim=1)
            target_scores = [target_scores]
            target_scores.append(torch.zeros((len(targets), self.valid_out_dim - self.last_valid_out_dim),
                                             requires_grad=True).cuda())
            target_scores = torch.cat(target_scores, dim=1)
            loss_kd += self.mu * loss_fn_kd(logits[kd_index], target_scores[kd_index],
                                            np.arange(self.valid_out_dim).tolist(), self.DTemp, soft_t=True)
            # print(loss_kd, loss_class)
        total_loss = loss_class + loss_kd
        self.optimizer.zero_grad()
        total_loss.backward()
        self.optimizer.step()
        return total_loss.detach(), loss_class.detach(), loss_kd.detach(), logits

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs

    def sample(self, teacher, dim, device, return_scores=True):
        return teacher.sample(dim, device, return_scores=return_scores)

    def combine_data(self, data):
        x, y = [], []
        for i in range(len(data)):
            x.append(data[i][0])
            y.append(data[i][1])
        x, y = torch.cat(x), torch.cat(y)
        return x, y


class Teacher(nn.Module):

    def __init__(self, solver, generator, gen_opt, img_shape, iters, class_idx, deep_inv_params, train=True,
                 device='cuda'):

        super().__init__()
        self.solver = solver
        self.generator = generator
        self.gen_opt = gen_opt
        self.solver.eval()
        self.generator.eval()
        self.img_shape = img_shape
        self.iters = iters
        self.device = device

        # hyperparameters
        self.di_lr = deep_inv_params[0]
        self.r_feature_weight = deep_inv_params[1]
        self.di_var_scale = deep_inv_params[2]
        self.content_temp = deep_inv_params[3]
        self.content_weight = deep_inv_params[4]

        # get class keys
        self.class_idx = list(class_idx)
        self.num_k = len(self.class_idx)

        # first time?
        self.first_time = train

        # set up criteria for optimization
        self.criterion = nn.CrossEntropyLoss()
        self.mse_loss = nn.MSELoss(reduction="none").cuda()
        self.smoothing = Gaussiansmoothing(self.img_shape[1], 5, 1)

        # Create hooks for feature statistics catching
        loss_r_feature_layers = []
        for module in self.solver.modules():
            if isinstance(module, nn.BatchNorm2d) or isinstance(module, nn.BatchNorm1d):
                loss_r_feature_layers.append(DeepInversionFeatureHook(module, 0, self.r_feature_weight))
        self.loss_r_feature_layers = loss_r_feature_layers

    def sample(self, size, device, return_scores=False):

        # make sure solver is eval mode
        self.solver.eval()

        # train if first time
        self.generator.train()
        if self.first_time:
            self.first_time = False
            self.get_images(bs=size, epochs=self.iters, idx=-1)

        # sample images
        self.generator.eval()
        with torch.no_grad():
            x_i = self.generator.sample(size)

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x_i)
        y_hat = y_hat[:, self.class_idx]

        # get predicted class-labels (indexed according to each class' position in [self.class_idx]!)
        _, y = torch.max(y_hat, dim=1)

        return (x_i, y, y_hat) if return_scores else (x_i, y)

    def generate_scores(self, x, allowed_predictions=None, return_label=False):

        # make sure solver is eval mode
        self.solver.eval()

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x)
        y_hat = y_hat[:, allowed_predictions]

        # get predicted class-labels
        _, y = torch.max(y_hat, dim=1)

        return (y, y_hat) if return_label else y_hat

    def generate_scores_pen(self, x):

        # make sure solver is eval mode
        self.solver.eval()

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x)

        return y_hat

    def get_images(self, bs=256, epochs=1000, idx=-1):

        print('training generator ...')

        # clear cuda cache
        torch.cuda.empty_cache()

        self.generator.train()
        for epoch in range(epochs):

            # sample from generator
            inputs = self.generator.sample(bs)

            # forward with images
            self.gen_opt.zero_grad()
            self.solver.zero_grad()

            # content
            outputs = self.solver(inputs)[:, :self.num_k]
            loss = self.criterion(outputs / self.content_temp, torch.argmax(outputs, dim=1)) * self.content_weight

            # class balance
            softmax_o_T = F.softmax(outputs, dim=1).mean(dim=0)
            loss += (1.0 + (softmax_o_T * torch.log(softmax_o_T) / math.log(self.num_k)).sum())

            # R_feature loss
            for mod in self.loss_r_feature_layers:
                loss_distr = mod.r_feature * self.r_feature_weight / len(self.loss_r_feature_layers)
                loss_distr = loss_distr.to(self.device)
                loss = loss + loss_distr

            # image prior
            loss_var = torch.tensor(0).to(self.device)
            if self.generator.is_img:
                inputs_smooth = self.smoothing(F.pad(inputs, (2, 2, 2, 2), mode='reflect'))
                loss_var = self.mse_loss(inputs, inputs_smooth).mean()

            loss = loss + self.di_var_scale * loss_var

            # backward pass
            loss.backward()

            self.gen_opt.step()

            if epoch % 1000 == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))

        # clear cuda cache
        torch.cuda.empty_cache()
        self.generator.eval()


class Generator(nn.Module):
    def __init__(self, zdim, in_channel, img_sz):
        super(Generator, self).__init__()
        self.is_img = True
        self.z_dim = zdim

        self.init_size = img_sz // 4
        self.l1 = nn.Sequential(nn.Linear(zdim, 128 * self.init_size ** 2))

        self.conv_blocks0 = nn.Sequential(
            nn.BatchNorm2d(128),
        )
        self.conv_blocks1 = nn.Sequential(
            nn.Conv2d(128, 128, 3, stride=1, padding=1),
            nn.BatchNorm2d(128, 0.8),
            nn.LeakyReLU(0.2, inplace=True),
        )
        self.conv_blocks2 = nn.Sequential(
            nn.Conv2d(128, 64, 3, stride=1, padding=1),
            nn.BatchNorm2d(64, 0.8),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(64, in_channel, 3, stride=1, padding=1),
            nn.Tanh(),
            nn.BatchNorm2d(in_channel, affine=False)
        )

    def forward(self, z):
        out = self.l1(z)
        out = out.view(out.shape[0], 128, self.init_size, self.init_size)
        img = self.conv_blocks0(out)
        img = nn.functional.interpolate(img, scale_factor=2)
        img = self.conv_blocks1(img)
        img = nn.functional.interpolate(img, scale_factor=2)
        img = self.conv_blocks2(img)
        return img

    def sample(self, size):
        # sample z
        z = torch.randn(size, self.z_dim)
        z = z.cuda()
        X = self.forward(z)
        return X


class Generator_MLP(nn.Module):
    def __init__(self, zdim, img_sz, in_channel=1, is_img=True, mid_dim=None):
        super(Generator_MLP, self).__init__()
        self.z_dim = zdim
        self.in_channel = in_channel
        self.img_sz = img_sz
        self.is_img = is_img
        if is_img:
            self.out_dim = in_channel * img_sz * img_sz
        else:
            self.out_dim = img_sz

        if mid_dim:
            self.mid_dim = mid_dim
        else:
            self.mid_dim = self.out_dim * 2

        self.l1 = nn.Sequential(nn.Linear(zdim, self.mid_dim))
        self.l2 = nn.Sequential(nn.Linear(self.mid_dim, self.out_dim))

    def forward(self, z):
        out = self.l1(z)
        out = self.l2(out)
        if self.is_img:
            out = out.view(-1, self.in_channel, self.img_sz, self.img_sz)
        return out

    def sample(self, size):
        # sample z
        z = torch.randn(size, self.z_dim)
        z = z.cuda()
        X = self.forward(z)
        return X


class Gaussiansmoothing(nn.Module):
    """
    Apply gaussian smoothing on a
    1d, 2d or 3d tensor. Filtering is performed seperately for each channel
    in the input using a depthwise convolution.
    Arguments:
        channels (int, sequence): Number of channels of the input tensors. Output will
            have this number of channels as well.
        kernel_size (int, sequence): Size of the gaussian kernel.
        sigma (float, sequence): Standard deviation of the gaussian kernel.
        dim (int, optional): The number of dimensions of the data.
            Default value is 2 (spatial).
    """

    def __init__(self, channels, kernel_size, sigma, dim=2):
        super(Gaussiansmoothing, self).__init__()
        kernel_size = [kernel_size] * dim
        sigma = [sigma] * dim

        # The gaussian kernel is the product of the
        # gaussian function of each dimension.
        kernel = 1
        meshgrids = torch.meshgrid(
            [
                torch.arange(size, dtype=torch.float32)
                for size in kernel_size
            ]
        )
        for size, std, mgrid in zip(kernel_size, sigma, meshgrids):
            mean = (size - 1) / 2
            kernel *= 1 / (std * math.sqrt(2 * math.pi)) * \
                      torch.exp(-((mgrid - mean) / (2 * std)) ** 2)

        # Make sure sum of values in gaussian kernel equals 1.
        kernel = kernel / torch.sum(kernel)

        # Reshape to depthwise convolutional weight
        kernel = kernel.view(1, 1, *kernel.size())
        kernel = kernel.repeat(channels, *[1] * (kernel.dim() - 1)).cuda()

        self.register_buffer('weight', kernel)
        self.groups = channels

        if dim == 1:
            self.conv = F.conv1d
        elif dim == 2:
            self.conv = F.conv2d
        elif dim == 3:
            self.conv = F.conv3d
        else:
            raise RuntimeError(
                'Only 1, 2 and 3 dimensions are supported. Received {}.'.format(dim)
            )

    def forward(self, input):
        """
        Apply gaussian filter to input.
        Arguments:
            input (torch.Tensor): Input to apply gaussian filter on.
        Returns:
            filtered (torch.Tensor): Filtered output.
        """
        return self.conv(input, weight=self.weight, groups=self.groups)


class DeepInversionFeatureHook():
    '''
    Implementation of the forward hook to track feature statistics and compute a loss on them.
    Will compute mean and variance, and will use l2 as a loss
    '''

    def __init__(self, module, gram_matrix_weight, layer_weight):
        self.hook = module.register_forward_hook(self.hook_fn)
        self.target = None
        self.gram_matrix_weight = gram_matrix_weight
        self.layer_weight = layer_weight

    def hook_fn(self, module, input, output):
        # hook co compute deepinversion's feature distribution regularization
        nch = input[0].shape[1]
        mean = input[0].mean([0, 2, 3])
        var = input[0].permute(1, 0, 2, 3).contiguous().view([nch, -1]).var(1, unbiased=False) + 1e-8
        r_feature = torch.log(
            var ** (0.5) / (module.running_var.data.type(var.type()) + 1e-8) ** (0.5)).mean() - 0.5 * (1.0 - (
                module.running_var.data.type(var.type()) + 1e-8 + (
                module.running_mean.data.type(var.type()) - mean) ** 2) / var).mean()

        self.r_feature = r_feature

    def close(self):
        self.hook.remove()
