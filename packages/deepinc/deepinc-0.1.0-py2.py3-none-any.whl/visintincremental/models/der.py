import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset
import numpy as np

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel

from deepinc.utils.args import *
from deepinc.utils.buffer import Buffer


class Der(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(Der, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy
        self.current_task = 0

    def begin_il(self, dataset):
        self.buffer = Buffer(self.args.buffer_size, self.device)
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.net = resnet18(dataset.nc).to(self.device)
        elif self.args.dataset == 'seq-tinyimg':
            self.net = resnet18(dataset.nc).to(self.device)
        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)
        self.opt = SGD(self.net.parameters(), lr=self.args.lr)

        self.transform = dataset.get_transform()

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.train_(train_loader)

    def train_(self, train_loader):
        self.net.train()
        self.opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels, not_aug = data[0].to(self.device), data[1].to(self.device), data[2].to(self.device)
                loss = self.observe(inputs, labels, not_aug)
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss))

    def observe(self, inputs, labels, not_aug):

        self.opt.zero_grad()

        outputs = self.net(inputs)
        loss = self.loss(outputs, labels)

        if not self.buffer.is_empty():
            buf_inputs, buf_logits = self.buffer.get_data(
                self.args.minibatch_size, transform=self.transform)
            buf_outputs = self.net(buf_inputs)
            loss += self.args.alpha * F.mse_loss(buf_outputs, buf_logits)

        loss.backward()
        self.opt.step()
        self.buffer.add_data(examples=not_aug, logits=outputs.data)

        return loss.item()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs
