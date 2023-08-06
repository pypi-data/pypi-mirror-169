import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset
import numpy as np
import copy

from deepinc.backbone.MNISTMLP_LWM import MNISTMLP
from deepinc.backbone.ResNet_LWM import resnet18, resnet34
from deepinc.models.utils.incremental_model import IncrementalModel
from deepinc.utils.args import *
from deepinc.utils.buffer import Buffer

class LWM(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(LWM, self).__init__(args)
        self.writer = None
        self.epochs = args.n_epochs
        self.lr = args.lr
        self.loss = F.cross_entropy
        self.beta = args.beta
        self.gamma = args.gamma
        self.current_task = 0

    def begin_il(self, dataset):
        self.ntasks = dataset.nc
        self.class_per_task = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.net_old = None
        if self.args.dataset == 'seq-mnist':
            self.net_new = MNISTMLP(28*28, dataset.nc).to(self.device)
        else:
            if self.args.backbone == 'None' or self.args.backbone == 'resnet18':
                self.net_new = resnet18(dataset.nc).to(self.device)
            elif self.args.backbone == 'resnet34':
                self.net_new = resnet34(dataset.nc).to(self.device)

    def train_task(self, dataset, train_loader):
        self.net_new.train()
        opt = SGD(self.net_new.parameters(), lr=self.lr)
        losses = []
        if self.current_task == 0:
            for epoch in range(self.epochs):
                for step, data in enumerate(train_loader):
                    inputs, labels = data[0].to(self.device), data[1].to(self.device)
                    y_pred = self.net_new(inputs)[:, :self.class_per_task]
                    loss = self.loss(y_pred, labels).mean()

                    opt.zero_grad()
                    loss.backward()
                    opt.step()

                    losses.append(loss.item())
                loss = np.array(losses, dtype=np.float).mean()
                if epoch % self.args.print_freq == 0:
                    print('| epoch %d, task %d, train_loss %.4f' % (epoch, 0, loss))
        else:
            lim = (self.current_task + 1) * self.class_per_task
            # copying the old network
            self.net_new.feature = None
            self.net_old = copy.deepcopy(self.net_new)
            self.net_old.requires_grad_(False)
            self.net_old.train()

            loss_Cs, loss_Ds, loss_ADs = [], [], []
            for epoch in range(self.epochs):
                for step, data in enumerate(train_loader):
                    inputs, labels = data[0].to(self.device), data[1].to(self.device)
                    y_pred_old = self.net_old(inputs)[:, :lim - self.class_per_task]
                    y_pred_new = self.net_new(inputs)[:, :lim]

                    loss_C = F.cross_entropy(y_pred_new, labels).mean()
                    loss_D = F.binary_cross_entropy_with_logits(y_pred_new[:, :-self.class_per_task], y_pred_old.detach().sigmoid())
                    if isinstance(self.net_new, MNISTMLP):
                        loss_AD = self.grad_cam_loss_MNIST(self.net_old.feature, y_pred_old, self.net_new.feature, y_pred_new[:, :-self.class_per_task])
                    else:
                        loss_AD = self.grad_cam_loss(self.net_old.feature, y_pred_old, self.net_new.feature, y_pred_new[:, :-self.class_per_task])
                    loss = loss_C + loss_D * self.beta + loss_AD * self.gamma

                    opt.zero_grad()
                    loss.backward()
                    opt.step()

                    losses.append(loss.item())
                    loss_Cs.append(loss_C.item())
                    loss_Ds.append(loss_D.item())
                    loss_ADs.append(loss_AD.item())

                    torch.cuda.empty_cache()

                loss = np.array(losses, dtype=np.float).mean()
                loss_C = np.array(loss_Cs, dtype=np.float).mean()
                loss_D = np.array(loss_Ds, dtype=np.float).mean()
                loss_AD = np.array(loss_ADs, dtype=np.float).mean()

                if epoch % self.args.print_freq == 0:
                    print('| epoch %d, task %d, train_loss %.4f, train_loss_C %.4f, train_loss_D %.4f, train_loss_AD %.4f' % (
                        epoch, self.current_task, loss, loss_C, loss_D, loss_AD))


        self.current_task += 1

    def grad_cam_loss(self, feature_o, out_o, feature_n, out_n):
        batch = out_n.size()[0]
        index = out_n.argmax(dim=-1).view(-1, 1)
        onehot = torch.zeros_like(out_n)
        onehot.scatter_(-1, index, 1.)
        out_o, out_n = torch.sum(onehot * out_o), torch.sum(onehot * out_n)

        grads_o = torch.autograd.grad(out_o, feature_o)[0]
        grads_n = torch.autograd.grad(out_n, feature_n, create_graph=True)[0]
        weight_o = grads_o.mean(dim=(2, 3)).view(batch, -1, 1, 1)
        weight_n = grads_n.mean(dim=(2, 3)).view(batch, -1, 1, 1)

        cam_o = F.relu((grads_o * weight_o).sum(dim=1))
        cam_n = F.relu((grads_n * weight_n).sum(dim=1))

        # normalization
        cam_o = F.normalize(cam_o.view(batch, -1), p=2, dim=-1)
        cam_n = F.normalize(cam_n.view(batch, -1), p=2, dim=-1)

        loss_AD = (cam_o - cam_n).norm(p=1, dim=1).mean()
        return loss_AD

    def grad_cam_loss_MNIST(self, feature_o, out_o, feature_n, out_n):
        batch = out_n.size()[0]
        index = out_n.argmax(dim=-1).view(-1, 1)
        onehot = torch.zeros_like(out_n)
        onehot.scatter_(-1, index, 1.)
        out_o, out_n = torch.sum(onehot * out_o), torch.sum(onehot * out_n)

        grads_o = torch.autograd.grad(out_o, feature_o)[0]
        grads_n = torch.autograd.grad(out_n, feature_n, create_graph=True)[0]
        weight_o = grads_o.mean(dim=1).view(batch, -1)
        weight_n = grads_n.mean(dim=1).view(batch, -1)

        cam_o = F.relu((grads_o * weight_o))
        cam_n = F.relu((grads_n * weight_n))

        # normalization
        cam_o = F.normalize(cam_o.view(batch, -1), p=2, dim=-1)
        cam_n = F.normalize(cam_n.view(batch, -1), p=2, dim=-1)


        loss_AD = (cam_o - cam_n).norm(p=1, dim=1).mean()
        return loss_AD

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        lim = (self.current_task + 1) * self.class_per_task
        self.net_new.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net_new(x)[:, :lim]
        return outputs
