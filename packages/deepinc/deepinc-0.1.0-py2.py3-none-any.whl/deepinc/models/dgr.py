import copy
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel


class DGR(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(DGR, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.criterion = F.cross_entropy

        self.generative_replay = False
        self.previous_scholar = None
        self.mu = self.args.mu

        self.current_task = 0
        self.valid_out_dim = 0
        self.last_valid_out_dim = 0
        # 任务初始化
    def begin_il(self, dataset):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg':
            if self.args.featureNet:
                self.net = MNISTMLP(1000, dataset.nc).to(self.device)
                self.generator = AutoEncoder_MLP(in_dim=1000).to(self.device)
                self.generator.recon_criterion = nn.MSELoss(reduction="none")
            else:
                self.net = resnet18(dataset.nc).to(self.device)
                self.generator = CIFAR_GEN().to(self.device)
                self.generator.recon_criterion = nn.BCELoss(reduction="none")

        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)
            self.generator = AutoEncoder_MLP(in_dim=28*28, hidden_dim=[100, 100], embedding_dim=100).to(self.device)
            self.generator.recon_criterion = nn.MSELoss(reduction="none")

        self.generator.optimizer = torch.optim.SGD(self.generator.parameters(), lr=self.learning_rate)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.last_valid_out_dim = self.valid_out_dim
        self.valid_out_dim += len(self.t_c_arr[0])

        self.train_(train_loader)

        self.net.eval()
        self.generator.eval()

        self.current_task += 1
        scholar = Scholar(generator=self.generator, solver=self.net)
        self.previous_scholar = copy.deepcopy(scholar)
        self.generative_replay = True

    def train_(self, train_loader):
        self.net.train()
        self.generator.train()
        opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                if data[0].shape[0] != self.args.batch_size:
                    continue

                x, y = data[0].to(self.device), data[1].to(self.device)

                if self.args.dataset == 'seq-mnist':
                    x = x.view(x.shape[0], -1)

                # data replay
                if not self.generative_replay:
                    x_replay = None  # -> if no replay
                else:
                    allowed_predictions = list(range(self.last_valid_out_dim))
                    x_replay, y_replay, y_replay_hat = self.previous_scholar.sample(len(x),
                                                                                    allowed_predictions=allowed_predictions,
                                                                                    return_scores=True)

                # if KD
                if self.generative_replay:
                    y_hat = self.previous_scholar.generate_scores(x, allowed_predictions=allowed_predictions)
                    _, y_hat_com = self.combine_data(((x, y_hat), (x_replay, y_replay_hat)))
                else:
                    y_hat_com = None

                # combine inputs and generated samples for classification
                if self.generative_replay:
                    x_com, y_com = self.combine_data(((x, y), (x_replay, y_replay)))
                else:
                    x_com, y_com = x, y

                # dgr data weighting
                mappings = torch.ones(y_com.size(), dtype=torch.float32).to(self.device)

                rnt = 1.0 * self.last_valid_out_dim / self.valid_out_dim
                mappings[:self.last_valid_out_dim] = rnt
                mappings[self.last_valid_out_dim:] = 1 - rnt
                dw_cls = mappings[y_com.long()]

                # print(x_com.shape)
                logits = self.net(x_com)
                kd_index = np.arange(len(x), len(x_com))

                loss = (self.criterion(logits, y_com.long()) * dw_cls).mean()

                if self.generative_replay:
                    # if self.current_task == 5:
                    #     print(kd_index)
                    #     print(logits[kd_index, :self.last_valid_out_dim].shape)
                    #     print(y_hat_com[kd_index, :self.last_valid_out_dim].shape)

                    loss += self.mu * loss_fn_kd(logits[kd_index, :self.last_valid_out_dim], y_hat_com[kd_index, :self.last_valid_out_dim], dw_cls[kd_index], np.arange(self.last_valid_out_dim).tolist())

                opt.zero_grad()
                loss.backward()
                opt.step()

                # generator update
                self.generator.train_batch(x_com, dw_cls, list(range(self.valid_out_dim)))
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs

    def combine_data(self, data):
        x, y = [],[]
        for i in range(len(data)):
            x.append(data[i][0])
            y.append(data[i][1])
        x, y = torch.cat(x), torch.cat(y)
        return x, y


def loss_fn_kd(scores, target_scores, data_weights, allowed_predictions, T=2., soft_t = False):
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
    KD_loss_unnorm = KD_loss_unnorm.sum(dim=1)                      #--> sum over classes
    KD_loss_unnorm = KD_loss_unnorm.mean()                          #--> average over batch

    # normalize
    KD_loss = KD_loss_unnorm # * T**2

    return KD_loss


class Scholar(nn.Module):

    def __init__(self, generator, solver, stats = None, class_idx = None, temp = None):

        super().__init__()
        self.generator = generator
        self.solver = solver

        # get class keys
        if class_idx is not None:
            self.class_idx = list(class_idx)
            self.layer_idx = list(self.stats.keys())
            self.num_k = len(self.class_idx)


    def sample(self, size, allowed_predictions=None, return_scores=False):

        # set model to eval()-mode
        mode = self.training
        self.eval()

        # sample images
        x = self.generator.sample(size)

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x)
        y_hat = y_hat[:, allowed_predictions]

        # get predicted class-labels (indexed according to each class' position in [allowed_predictions]!)
        _, y = torch.max(y_hat, dim=1)

        # set model back to its initial mode
        self.train(mode=mode)

        return (x, y, y_hat) if return_scores else (x, y)

    def generate_scores(self, x, allowed_predictions=None):

        # set model to eval()-mode
        mode = self.training
        self.eval()

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x)
        y_hat = y_hat[:, allowed_predictions]

        # get predicted class-labels (indexed according to each class' position in [allowed_predictions]!)
        _, y = torch.max(y_hat, dim=1)

        # set model back to its initial mode
        self.train(mode=mode)

        return y_hat

    def generate_scores_pen(self, x):

        # set model to eval()-mode
        mode = self.training
        self.eval()

        # get predicted logit-scores
        with torch.no_grad():
            y_hat = self.solver.forward(x=x, pen=True)

        # set model back to its initial mode
        self.train(mode=mode)

        return y_hat


class AutoEncoder(nn.Module):

    def __init__(self, kernel_num, in_channel=1, img_sz=32, hidden_dim=256, z_size=100, bn=False):
        super(AutoEncoder, self).__init__()
        self.BN = bn
        self.in_dim = in_channel * img_sz * img_sz
        self.image_size = img_sz
        self.channel_num = in_channel
        self.kernel_num = kernel_num
        self.z_size = z_size

        # -weigths of different components of the loss function
        self.lamda_rcl = 1.
        self.lamda_vl = 1.

        # Training related components that should be set before training
        # -criterion for reconstruction
        self.recon_criterion = None

        self.encoder = nn.Sequential(
            self._conv(in_channel, 64),
            self._conv(64, 128),
            self._conv(128, 512),
        )

        self.decoder = nn.Sequential(
            self._deconv(512, 256),
            self._deconv(256, 64),
            self._deconv(64, in_channel, ReLU=False),
            nn.Sigmoid()
        )
        self.feature_size = img_sz // 8

        self.kernel_num = 512
        self.feature_volume = self.kernel_num * (self.feature_size ** 2)

        # q
        self.q_mean = self._linear(self.feature_volume, z_size, relu=False)
        self.q_logvar = self._linear(self.feature_volume, z_size, relu=False)

        # projection
        self.project = self._linear(z_size, self.feature_volume, relu=False)

    def reparameterize(self, mu, logvar):
        '''Perform "reparametrization trick" to make these stochastic variables differentiable.'''
        std = logvar.mul(0.5).exp_()
        eps = std.new(std.size()).normal_()
        return eps.mul(std).add_(mu)

    def forward(self, x):

        # encode (forward), reparameterize and decode (backward)
        mu, logvar, hE = self.encode(x)
        z = self.reparameterize(mu, logvar) if self.training else mu
        x_recon = self.decode(z)
        return (x_recon, mu, logvar, z)

    def sample(self, size):

        # set model to eval()-mode
        mode = self.training
        self.eval()
        # sample z
        z = torch.randn(size, self.z_size)
        z = z.cuda()
        with torch.no_grad():
            X = self.decode(z)
        # set model back to its initial mode
        self.train(mode=mode)
        # return samples as [batch_size]x[channels]x[image_size]x[image_size] tensor, plus classes-labels
        return X

    def loss_function(self, recon_x, x, dw, mu=None, logvar=None):
        batch_size = x.size(0)

        ###-----Reconstruction loss-----###
        reconL = (self.recon_criterion(input=recon_x.view(batch_size, -1), target=x.view(batch_size, -1))).mean(dim=1)
        reconL = torch.mean(reconL * dw)

        ###-----Variational loss-----###
        if logvar is not None:
            # ---- see Appendix B from: Kingma and Welling. Auto-Encoding Variational Bayes. ICLR, 2014 ----#
            variatL = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1).mean()
            # -normalise by same number of elements as in reconstruction
            variatL /= self.in_dim
            # --> because self.recon_criterion averages over batch-size but also over all pixels/elements in recon!!

        else:
            variatL = torch.tensor(0.)
            variatL = variatL.cuda()

        # Return a tuple of the calculated losses
        return reconL, variatL

    def train_batch(self, x, data_weights, allowed_predictions):
        '''Train model for one batch ([x],[y]), possibly supplemented with replayed data ([x_],[y_]).

        [x]               <tensor> batch of inputs (could be None, in which case only 'replayed' data is used)'''

        # Set model to training-mode
        self.train()

        ##--(1)-- CURRENT DATA --##
        # Run the model
        recon_batch, mu, logvar, z = self.forward(x)

        # Calculate all losses
        reconL, variatL = self.loss_function(recon_x=recon_batch, x=x, dw=data_weights, mu=mu, logvar=logvar)

        # Weigh losses as requested
        loss_total = self.lamda_rcl * reconL + self.lamda_vl * variatL

        # perform update
        self.optimizer.zero_grad()
        loss_total.backward()
        self.optimizer.step()
        return loss_total.detach()

    def decode(self, z):
        '''Pass latent variable activations through feedback connections, to give reconstructed image [image_recon].'''
        z_projected = self.project(z).view(
            -1, self.kernel_num,
            self.feature_size,
            self.feature_size,
        )
        return self.decoder(z_projected)

    def encode(self, x):
        '''Pass input through feed-forward connections, to get [hE], [z_mean] and [z_logvar].'''
        # encode x
        encoded = self.encoder(x)
        # sample latent code z from q given x.
        z_mean, z_logvar = self.q(encoded)
        return z_mean, z_logvar, encoded

    def q(self, encoded):
        unrolled = encoded.view(-1, self.feature_volume)
        return self.q_mean(unrolled), self.q_logvar(unrolled)

    def _conv(self, channel_size, kernel_num, kernel_size_=4, stride_=2):
        if self.BN:
            return nn.Sequential(
                nn.Conv2d(
                    channel_size, kernel_num,
                    kernel_size=kernel_size_, stride=stride_, padding=1,
                ),
                nn.BatchNorm2d(kernel_num),
                nn.ReLU(),
            )
        else:
            return nn.Sequential(
                nn.Conv2d(
                    channel_size, kernel_num,
                    kernel_size=kernel_size_, stride=stride_, padding=1,
                ),
                nn.ReLU(),
            )

    def _deconv(self, channel_num, kernel_num, ReLU=True, kernel_size_=4, stride_=2):
        if ReLU:
            if self.BN:
                return nn.Sequential(
                    nn.ConvTranspose2d(
                        channel_num, kernel_num,
                        kernel_size=kernel_size_, stride=stride_, padding=1,
                    ),
                    nn.BatchNorm2d(kernel_num),
                    nn.ReLU(),
                )
            else:
                return nn.Sequential(
                    nn.ConvTranspose2d(
                        channel_num, kernel_num,
                        kernel_size=kernel_size_, stride=stride_, padding=1,
                    ),
                    nn.ReLU(),
                )
        else:
            if self.BN:
                return nn.Sequential(
                    nn.ConvTranspose2d(
                        channel_num, kernel_num,
                        kernel_size=kernel_size_, stride=stride_, padding=1,
                    ),
                    nn.BatchNorm2d(kernel_num),
                )
            else:
                return nn.Sequential(
                    nn.ConvTranspose2d(
                        channel_num, kernel_num,
                        kernel_size=kernel_size_, stride=stride_, padding=1,
                    ),
                )

    def _linear(self, in_size, out_size, relu=True):
        return nn.Sequential(
            nn.Linear(in_size, out_size),
            nn.ReLU(),
        ) if relu else nn.Linear(in_size, out_size)


class AutoEncoder_MLP(nn.Module):

    def __init__(self, in_dim, hidden_dim=[800, 500], embedding_dim=256):
        super(AutoEncoder_MLP, self).__init__()
        self.in_dim = in_dim
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim

        # -weigths of different components of the loss function
        self.lamda_rcl = 1.
        self.lamda_vl = 1.

        # Training related components that should be set before training
        # -criterion for reconstruction
        self.recon_criterion = None

        self.encoder = nn.Sequential(
            self._linear(in_dim, self.hidden_dim[0], relu=True),
            self._linear(self.hidden_dim[0], self.hidden_dim[1], relu=True),
            self._linear(self.hidden_dim[1], self.embedding_dim, relu=False),
        )

        self.decoder = nn.Sequential(
            self._linear(self.embedding_dim, self.hidden_dim[1], relu=True),
            self._linear(self.hidden_dim[1], self.hidden_dim[0], relu=True),
            self._linear(self.hidden_dim[0], self.in_dim, relu=False),
        )

        # q
        self.q_mean = self._linear(self.embedding_dim, self.embedding_dim, relu=False)
        self.q_logvar = self._linear(self.embedding_dim, self.embedding_dim, relu=False)

        # projection
        self.project = self._linear(self.embedding_dim, self.embedding_dim, relu=False)

    def reparameterize(self, mu, logvar):
        '''Perform "reparametrization trick" to make these stochastic variables differentiable.'''
        std = logvar.mul(0.5).exp_()
        eps = std.new(std.size()).normal_()
        return eps.mul(std).add_(mu)

    def forward(self, x):

        # encode (forward), reparameterize and decode (backward)
        mu, logvar, hE = self.encode(x)
        z = self.reparameterize(mu, logvar) if self.training else mu
        x_recon = self.decode(z)
        return (x_recon, mu, logvar, z)

    def sample(self, size):

        # set model to eval()-mode
        mode = self.training
        self.eval()
        # sample z
        z = torch.randn(size, self.embedding_dim)
        z = z.cuda()
        with torch.no_grad():
            X = self.decode(z)
        # set model back to its initial mode
        self.train(mode=mode)
        # return samples as [batch_size]x[channels]x[image_size]x[image_size] tensor, plus classes-labels
        return X

    def loss_function(self, recon_x, x, dw, mu=None, logvar=None):
        batch_size = x.size(0)

        ###-----Reconstruction loss-----###
        reconL = (self.recon_criterion(input=recon_x.view(batch_size, -1), target=x.view(batch_size, -1))).mean(dim=1)
        reconL = torch.mean(reconL * dw)

        ###-----Variational loss-----###
        if logvar is not None:
            # ---- see Appendix B from: Kingma and Welling. Auto-Encoding Variational Bayes. ICLR, 2014 ----#
            variatL = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=1).mean()
            # -normalise by same number of elements as in reconstruction
            variatL /= self.in_dim
            # --> because self.recon_criterion averages over batch-size but also over all pixels/elements in recon!!

        else:
            variatL = torch.tensor(0.)
            variatL = variatL.cuda()

        # Return a tuple of the calculated losses
        return reconL, variatL

    def train_batch(self, x, data_weights, allowed_predictions):
        '''Train model for one batch ([x],[y]), possibly supplemented with replayed data ([x_],[y_]).

        [x]               <tensor> batch of inputs (could be None, in which case only 'replayed' data is used)'''

        # Set model to training-mode
        self.train()

        ##--(1)-- CURRENT DATA --##
        # Run the model
        recon_batch, mu, logvar, z = self.forward(x)

        # Calculate all losses
        reconL, variatL = self.loss_function(recon_x=recon_batch, x=x, dw=data_weights, mu=mu, logvar=logvar)

        # Weigh losses as requested
        loss_total = self.lamda_rcl * reconL + self.lamda_vl * variatL

        # perform update
        self.optimizer.zero_grad()
        loss_total.backward()
        self.optimizer.step()
        return loss_total.detach()

    def decode(self, z):
        '''Pass latent variable activations through feedback connections, to give reconstructed image [image_recon].'''
        z_projected = self.project(z)
        return self.decoder(z_projected)

    def encode(self, x):
        '''Pass input through feed-forward connections, to get [hE], [z_mean] and [z_logvar].'''
        # encode x
        x = x.view(x.shape[0], -1)
        encoded = self.encoder(x)
        # sample latent code z from q given x.
        z_mean, z_logvar = self.q(encoded)
        return z_mean, z_logvar, encoded

    def q(self, encoded):
        return self.q_mean(encoded), self.q_logvar(encoded)


    def _linear(self, in_size, out_size, relu=True):
        return nn.Sequential(
            nn.Linear(in_size, out_size),
            nn.ReLU(),
        ) if relu else nn.Linear(in_size, out_size)


def CIFAR_GEN():
    return AutoEncoder(in_channel=3, img_sz=32, kernel_num=512, z_size=1024)

def TinyImg_GEN():
    return AutoEncoder(in_channel=3, img_sz=64, kernel_num=512, z_size=1024)

