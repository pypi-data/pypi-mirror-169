import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.nn.functional import relu, avg_pool2d
from torch.utils.data import DataLoader, Dataset

from collections import OrderedDict
import numpy as np

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel


class GPM(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(GPM, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.feature_list = []

        self.current_task = -1

        # 任务初始化
    def begin_il(self, dataset):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg':
            if self.args.dataset == 'seq-tinyimg':
                self.img_size = 64
            else:
                self.img_size = 32
            self.net = ResNet18(dataset.nc,20, self.img_size).to(self.device)
        else:
            self.net = MLPNet().to(self.device)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)
        self.current_task += 1

        self.train_(train_loader)

        example = []
        for step, data in enumerate(train_loader):
            inputs = data[0].to(self.device)
            example.append(inputs)
            if step > 2: break
        example = torch.cat(example)

        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg':
            mat_list = self.get_representation_matrix_ResNet18(self.net, example)
        else:
            mat_list = self.get_representation_matrix_MLP(self.net, example)
        threshold = np.array([0.965] * 20)
        self.feature_list = self.update_GPM(mat_list, threshold, self.feature_list)

        # Projection Matrix Precomputation
        self.feature_mat = []
        for i in range(len(self.feature_list)):
            Uf = torch.Tensor(np.dot(self.feature_list[i], self.feature_list[i].transpose())).to(self.device)
            print('Layer {} - Projection Matrix shape: {}'.format(i + 1, Uf.shape))
            self.feature_mat.append(Uf)

    def train_(self, train_loader):
        self.net.train()
        opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                outputs = self.net(inputs)
                loss = self.loss(outputs, labels)

                opt.zero_grad()
                loss.backward()

                if self.current_task > 0:
                    kk = 0
                    for k, (m, params) in enumerate(self.net.named_parameters()):
                        if len(params.size()) == 4:
                            sz = params.grad.data.size(0)
                            params.grad.data = params.grad.data - torch.mm(params.grad.data.view(sz, -1), \
                                                                           self.feature_mat[kk]).view(params.size())
                            kk += 1
                        elif len(params.size()) == 1:
                            params.grad.data.fill_(0)

                opt.step()

            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs


    def update_GPM(self, mat_list, threshold, feature_list=[], ):
        print('Threshold: ', threshold)
        if not feature_list:
            # After First Task
            for i in range(len(mat_list)):
                activation = mat_list[i]
                U, S, Vh = np.linalg.svd(activation, full_matrices=False)
                # criteria (Eq-5)
                sval_total = (S ** 2).sum()
                sval_ratio = (S ** 2) / sval_total
                r = np.sum(np.cumsum(sval_ratio) < threshold[i])  # +1
                feature_list.append(U[:, 0:r])
        else:
            for i in range(len(mat_list)):
                activation = mat_list[i]
                U1, S1, Vh1 = np.linalg.svd(activation, full_matrices=False)
                sval_total = (S1 ** 2).sum()
                # Projected Representation (Eq-8)
                act_hat = activation - np.dot(np.dot(feature_list[i], feature_list[i].transpose()), activation)
                U, S, Vh = np.linalg.svd(act_hat, full_matrices=False)
                # criteria (Eq-9)
                sval_hat = (S ** 2).sum()
                sval_ratio = (S ** 2) / sval_total
                accumulated_sval = (sval_total - sval_hat) / sval_total

                r = 0
                for ii in range(sval_ratio.shape[0]):
                    if accumulated_sval < threshold[i]:
                        accumulated_sval += sval_ratio[ii]
                        r += 1
                    else:
                        break
                if r == 0:
                    print('Skip Updating GPM for layer: {}'.format(i + 1))
                    continue
                # update GPM
                Ui = np.hstack((feature_list[i], U[:, 0:r]))
                if Ui.shape[1] > Ui.shape[0]:
                    feature_list[i] = Ui[:, 0:Ui.shape[0]]
                else:
                    feature_list[i] = Ui

        print('-' * 40)
        print('Gradient Constraints Summary')
        print('-' * 40)
        for i in range(len(feature_list)):
            print('Layer {} : {}/{}'.format(i + 1, feature_list[i].shape[1], feature_list[i].shape[0]))
        print('-' * 40)
        return feature_list

    def get_representation_matrix_ResNet18(self, net, example_data):
        # Collect activations by forward pass
        net.eval()
        example_out = net(example_data)

        act_list = []
        act_list.extend([net.act['conv_in'],
                         net.layer1[0].act['conv_0'], net.layer1[0].act['conv_1'], net.layer1[1].act['conv_0'],
                         net.layer1[1].act['conv_1'],
                         net.layer2[0].act['conv_0'], net.layer2[0].act['conv_1'], net.layer2[1].act['conv_0'],
                         net.layer2[1].act['conv_1'],
                         net.layer3[0].act['conv_0'], net.layer3[0].act['conv_1'], net.layer3[1].act['conv_0'],
                         net.layer3[1].act['conv_1'],
                         net.layer4[0].act['conv_0'], net.layer4[0].act['conv_1'], net.layer4[1].act['conv_0'],
                         net.layer4[1].act['conv_1']])

        batch_list = [10, 10, 10, 10, 10, 10, 10, 10, 50, 50, 50, 100, 100, 100, 100, 100, 100]  # scaled
        # network arch
        stride_list = [1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]
        map_list = [self.img_size, self.img_size, self.img_size, self.img_size, self.img_size, self.img_size,
                    self.img_size / 2, self.img_size / 2, self.img_size / 2, self.img_size / 2,
                    self.img_size / 4, self.img_size / 4, self.img_size / 4, self.img_size / 4,
                    self.img_size / 8, self.img_size / 8, self.img_size / 8]
        in_channel = [3, 20, 20, 20, 20, 20, 40, 40, 40, 40, 80, 80, 80, 80, 160, 160, 160]

        pad = 1
        sc_list = [5, 9, 13]
        p1d = (1, 1, 1, 1)
        mat_final = []  # list containing GPM Matrices
        mat_list = []
        mat_sc_list = []
        for i in range(len(stride_list)):
            if i == 0:
                ksz = 3
            else:
                ksz = 3
            bsz = batch_list[i]
            st = stride_list[i]
            k = 0
            s = compute_conv_output_size(map_list[i], ksz, stride_list[i], pad)
            mat = np.zeros((ksz * ksz * in_channel[i], s * s * bsz))
            act = F.pad(act_list[i], p1d, "constant", 0).detach().cpu().numpy()
            for kk in range(bsz):
                for ii in range(s):
                    for jj in range(s):
                        mat[:, k] = act[kk, :, st * ii:ksz + st * ii, st * jj:ksz + st * jj].reshape(-1)
                        k += 1
            mat_list.append(mat)
            # For Shortcut Connection
            if i in sc_list:
                k = 0
                s = compute_conv_output_size(map_list[i], 1, stride_list[i])
                mat = np.zeros((1 * 1 * in_channel[i], s * s * bsz))
                act = act_list[i].detach().cpu().numpy()
                for kk in range(bsz):
                    for ii in range(s):
                        for jj in range(s):
                            mat[:, k] = act[kk, :, st * ii:1 + st * ii, st * jj:1 + st * jj].reshape(-1)
                            k += 1
                mat_sc_list.append(mat)

        ik = 0
        for i in range(len(mat_list)):
            mat_final.append(mat_list[i])
            if i in [6, 10, 14]:
                mat_final.append(mat_sc_list[ik])
                ik += 1

        print('-' * 30)
        print('Representation Matrix')
        print('-' * 30)
        for i in range(len(mat_final)):
            print('Layer {} : {}'.format(i + 1, mat_final[i].shape))
        print('-' * 30)
        return mat_final

    def get_representation_matrix_MLP(self, net, example_data):
        # Collect activations by forward pass
        net(example_data)

        batch_list = [300, 300, 300]
        mat_list = []  # list contains representation matrix of each layer
        act_key = list(net.act.keys())

        for i in range(len(act_key)):
            bsz = batch_list[i]
            act = net.act[act_key[i]].detach().cpu().numpy()
            activation = act[0:bsz].transpose()
            mat_list.append(activation)

        print('-' * 30)
        print('Representation Matrix')
        print('-' * 30)
        for i in range(len(mat_list)):
            print('Layer {} : {}'.format(i + 1, mat_list[i].shape))
        print('-' * 30)
        return mat_list

# Define ResNet18 model
def compute_conv_output_size(Lin, kernel_size, stride=1, padding=0, dilation=1):
    return int(np.floor((Lin + 2 * padding - dilation * (kernel_size - 1) - 1) / float(stride) + 1))


def conv3x3(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


def conv7x7(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=7, stride=stride,
                     padding=1, bias=False)


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_planes, planes, stride=1):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(in_planes, planes, stride)
        self.bn1 = nn.BatchNorm2d(planes, track_running_stats=False)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = nn.BatchNorm2d(planes, track_running_stats=False)

        self.shortcut = nn.Sequential()
        if stride != 1 or in_planes != self.expansion * planes:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_planes, self.expansion * planes, kernel_size=1,
                          stride=stride, bias=False),
                nn.BatchNorm2d(self.expansion * planes, track_running_stats=False)
            )
        self.act = OrderedDict()
        self.count = 0

    def forward(self, x):
        self.count = self.count % 2
        self.act['conv_{}'.format(self.count)] = x
        self.count += 1
        out = relu(self.bn1(self.conv1(x)))
        self.count = self.count % 2
        self.act['conv_{}'.format(self.count)] = out
        self.count += 1
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = relu(out)
        return out


class ResNet(nn.Module):
    def __init__(self, block, num_blocks, nc, nf, img_size):
        super(ResNet, self).__init__()
        self.in_planes = nf
        self.conv1 = conv3x3(3, nf * 1, 1)
        self.bn1 = nn.BatchNorm2d(nf * 1, track_running_stats=False)
        self.layer1 = self._make_layer(block, nf * 1, num_blocks[0], stride=1)
        self.layer2 = self._make_layer(block, nf * 2, num_blocks[1], stride=2)
        self.layer3 = self._make_layer(block, nf * 4, num_blocks[2], stride=2)
        self.layer4 = self._make_layer(block, nf * 8, num_blocks[3], stride=2)

        self.img_size = img_size
        self.linear = nn.Linear(nf * 8 * block.expansion * int(img_size / 16) * int(img_size / 16), nc, bias=False)
        self.act = OrderedDict()

    def _make_layer(self, block, planes, num_blocks, stride):
        strides = [stride] + [1] * (num_blocks - 1)
        layers = []
        for stride in strides:
            layers.append(block(self.in_planes, planes, stride))
            self.in_planes = planes * block.expansion
        return nn.Sequential(*layers)

    def forward(self, x):
        bsz = x.size(0)
        self.act['conv_in'] = x.view(bsz, 3, self.img_size, self.img_size)
        out = relu(self.bn1(self.conv1(x.view(bsz, 3, self.img_size, self.img_size))))
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = avg_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        y = self.linear(out)
        return y


def ResNet18(nc, nf=32, img_size=32):
    return ResNet(BasicBlock, [2, 2, 2, 2], nc, nf, img_size)


class MLPNet(nn.Module):
    def __init__(self, n_hidden=100, n_outputs=10):
        super(MLPNet, self).__init__()
        self.act = OrderedDict()
        self.lin1 = nn.Linear(784, n_hidden, bias=False)
        self.lin2 = nn.Linear(n_hidden, n_hidden, bias=False)
        self.fc1 = nn.Linear(n_hidden, n_outputs, bias=False)

    def forward(self, x):
        x = x.view(-1, 28*28)
        self.act['Lin1'] = x
        x = self.lin1(x)
        x = F.relu(x)
        self.act['Lin2'] = x
        x = self.lin2(x)
        x = F.relu(x)
        self.act['fc1'] = x
        x = self.fc1(x)
        return x



