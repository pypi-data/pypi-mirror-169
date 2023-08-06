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
from deepinc.utils.gss_buffer import Buffer as Buffer

class Gss(IncrementalModel):
    COMPATIBILITY = ['class-il', 'domain-il', 'task-il', 'general-continual']
    def __init__(self, args):
        super(Gss, self).__init__(args)
        self.buffer = Buffer(self.args.buffer_size, self.device,
                             self.args.gss_minibatch_size if
                             self.args.gss_minibatch_size is not None
                             else self.args.minibatch_size, self)
        self.alj_nepochs = self.args.batch_num
        self.loss = F.cross_entropy
        self.transform = None

    def begin_il(self, dataset):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.net = resnet18(dataset.nc).to(self.device)
        elif self.args.dataset == 'seq-tinyimg':
            self.net = resnet18(dataset.nc).to(self.device)
        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)
        self.opt = SGD(self.net.parameters(), lr=self.args.lr)

    def get_grads(self, inputs, labels):
        self.net.eval()
        self.opt.zero_grad()
        outputs = self.net(inputs)
        loss = self.loss(outputs, labels)
        loss.backward()
        grads = self.net.get_grads().clone().detach()
        self.opt.zero_grad()
        self.net.train()
        if len(grads.shape) == 1:
            grads = grads.unsqueeze(0)
        return grads

    def train_task(self, dataset, train_loader):
        self.net.train()
        for epoch in range(self.args.n_epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)
                loss = self.observe(inputs, labels)
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss))

    def observe(self, inputs, labels):
        real_batch_size = inputs.shape[0]
        self.buffer.drop_cache()
        self.buffer.reset_fathom()

        for _ in range(self.alj_nepochs):
            self.opt.zero_grad()
            if not self.buffer.is_empty():
                buf_inputs, buf_labels = self.buffer.get_data(
                    self.args.minibatch_size, transform=self.transform)
                tinputs = torch.cat((inputs, buf_inputs))
                tlabels = torch.cat((labels, buf_labels))
            else:
                tinputs = inputs
                tlabels = labels

            outputs = self.net(tinputs)
            loss = self.loss(outputs, tlabels)
            loss.backward()
            self.opt.step()

        self.buffer.add_data(examples=inputs[:real_batch_size],
                             labels=labels[:real_batch_size])
        return loss.item()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs
