import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset
import numpy as np

from deepinc.backbone.MNISTMLP_PNN import MNISTMLP_PNN
from deepinc.backbone.ResNet_PNN import resnet18_pnn
from deepinc.models.utils.incremental_model import IncrementalModel
from deepinc.utils.args import *
from deepinc.utils.buffer import Buffer

class Pnn(IncrementalModel):
    COMPATIBILITY = ['task-il']
    def __init__(self, args):
        super(Pnn, self).__init__(args)
        self.loss = F.cross_entropy
        self.args = args
        self.transform = None
        self.x_shape = None

        self.soft = torch.nn.Softmax(dim=0)
        self.logsoft = torch.nn.LogSoftmax(dim=0)
        self.current_task = 0
        self.device = args.device
    # 任务初始化
    def begin_il(self, dataset):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.nc = dataset.nc
        self.nt = dataset.nt
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg':
            self.nets = [resnet18_pnn(self.nc, 64, None, None).to(self.device)]
        else:
            self.nets = [MNISTMLP_PNN(28 * 28, self.nc, None).to(self.device)]
        self.net = self.nets[-1]
        self.opt = Adam(self.net.parameters(), lr=self.args.lr)

    def train_task(self, dataset, train_loader):
        self.train_(train_loader)
        self.end_task()


    def train_(self, train_loader):
        for epoch in range(self.args.n_epochs):
            self.net.train()
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)
                loss = self.observe(inputs, labels)
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss))


    def forward(self, x: torch.Tensor, task_label) -> torch.Tensor:
        self.net.eval()
        with torch.no_grad():
            if self.x_shape is None:
                self.x_shape = x.shape

            #task_label = self.current_task
            if self.current_task == 0:
                out = self.net(x)
            else:
                self.nets[task_label].to(self.device)
                out = self.nets[task_label](x)
                if self.current_task != task_label:
                    self.nets[task_label].cpu()
        return out

    def end_task(self):
        # instantiate new column
        if self.current_task == self.nt - 1:
            return
        self.current_task += 1
        self.nets[-1].cpu()
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg':
            self.nets.append(resnet18_pnn(self.nc, 64, self.nets, self.x_shape).to(self.device))
        else:
            self.nets.append(MNISTMLP_PNN(28 * 28, self.nc, self.nets).to(self.device))
        self.net = self.nets[-1]
        self.opt = Adam(self.net.parameters(), lr=self.args.lr)

    def observe(self, inputs, labels):
        if self.x_shape is None:
            self.x_shape = inputs.shape

        self.opt.zero_grad()
        outputs = self.net(inputs)
        loss = self.loss(outputs, labels)
        loss.backward()
        self.opt.step()

        return loss.item()
