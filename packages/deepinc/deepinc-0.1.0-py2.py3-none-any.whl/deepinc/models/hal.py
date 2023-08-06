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

class HAL(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(HAL, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy


        self.hal_lambda = args.hal_lambda
        self.beta = args.beta
        self.gamma = args.gamma
        self.anchor_optimization_steps = 100
        self.finetuning_epochs = 1

        self.current_task = 0

        # 任务初始化
    def begin_il(self, dataset):
        self.buffer = Buffer(self.args.buffer_size, self.device, dataset.nt, mode='ring')
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.net = resnet18(dataset.nc).to(self.device)
            self.spare_model = resnet18(dataset.nc).to(self.device)
        elif self.args.dataset == 'seq-tinyimg':
            self.net = resnet18(dataset.nc).to(self.device)
            self.spare_model = resnet18(dataset.nc).to(self.device)
        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)
            self.spare_model = MNISTMLP(28*28, dataset.nc).to(self.device)
        self.spare_opt = SGD(self.spare_model.parameters(), lr=self.args.lr)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.train_(train_loader)
        self.end_task(train_loader)

    def end_task(self, train_loader):
        self.current_task += 1
        # ring buffer mgmt (if we are not loading
        if self.current_task > self.buffer.task_number:
            self.buffer.num_seen_examples = 0
            self.buffer.task_number = self.current_task
        # get anchors (provided that we are not loading the model
        if len(self.anchors) < self.current_task * self.cpt:
            self.get_anchors(train_loader)
            del self.phi

    def get_anchors(self, train_loader):
        theta_t = self.net.get_params().detach().clone()
        self.spare_model.set_params(theta_t)

        # fine tune on memory buffer
        for _ in range(self.finetuning_epochs):
            inputs, labels = self.buffer.get_data(self.args.batch_size)
            self.spare_opt.zero_grad()
            out = self.spare_model(inputs)
            loss = self.loss(out, labels)
            loss.backward()
            self.spare_opt.step()

        theta_m = self.spare_model.get_params().detach().clone()

        classes_for_this_task = np.unique(train_loader.dataset.targets)

        for a_class in classes_for_this_task:
            e_t = torch.rand(self.input_shape, requires_grad=True, device=self.device)
            e_t_opt = SGD([e_t], lr=self.args.lr)
            print()
            for i in range(self.anchor_optimization_steps):
                e_t_opt.zero_grad()
                cum_loss = 0

                self.spare_opt.zero_grad()
                self.spare_model.set_params(theta_m.detach().clone())
                loss = -torch.sum(self.loss(self.spare_model(e_t.unsqueeze(0)), torch.tensor([a_class]).to(self.device)))
                loss.backward()
                cum_loss += loss.item()

                self.spare_opt.zero_grad()
                self.spare_model.set_params(theta_t.detach().clone())
                loss = torch.sum(self.loss(self.spare_model(e_t.unsqueeze(0)), torch.tensor([a_class]).to(self.device)))
                loss.backward()
                cum_loss += loss.item()

                self.spare_opt.zero_grad()
                loss = torch.sum(self.gamma * (self.spare_model.features(e_t.unsqueeze(0)) - self.phi) ** 2)
                assert not self.phi.requires_grad
                loss.backward()
                cum_loss += loss.item()

                e_t_opt.step()

            e_t = e_t.detach()
            e_t.requires_grad = False
            self.anchors = torch.cat((self.anchors, e_t.unsqueeze(0)))
            del e_t
            print('Total anchors:', len(self.anchors))

        self.spare_model.zero_grad()

    def train_(self, train_loader):
        self.net.train()
        self.opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)
                loss = self.observe(inputs, labels)
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss))


    def observe(self, inputs, labels):
        real_batch_size = inputs.shape[0]
        not_aug_inputs = inputs
        if not hasattr(self, 'input_shape'):
            self.input_shape = inputs.shape[1:]
        if not hasattr(self, 'anchors'):
            self.anchors = torch.zeros(tuple([0] + list(self.input_shape))).to(self.device)
        if not hasattr(self, 'phi'):
            print('Building phi')
            with torch.no_grad():
                self.phi = torch.zeros_like(self.net.features(inputs[0].unsqueeze(0)), requires_grad=False)
            assert not self.phi.requires_grad

        if not self.buffer.is_empty():
            buf_inputs, buf_labels = self.buffer.get_data(
                self.args.minibatch_size)
            inputs = torch.cat((inputs, buf_inputs))
            labels = torch.cat((labels, buf_labels))

        old_weights = self.net.get_params().detach().clone()

        self.opt.zero_grad()
        outputs = self.net(inputs)

        k = self.current_task

        loss = self.loss(outputs, labels)
        loss.backward()
        self.opt.step()

        first_loss = 0

        assert len(self.anchors) == self.cpt * k

        if len(self.anchors) > 0:
            first_loss = loss.item()
            with torch.no_grad():
                pred_anchors = self.net(self.anchors)

            self.net.set_params(old_weights)
            pred_anchors -= self.net(self.anchors)
            loss = self.hal_lambda * (pred_anchors ** 2).mean()
            loss.backward()
            self.opt.step()

        with torch.no_grad():
            self.phi = self.beta * self.phi + (1 - self.beta) * self.net.features(inputs[:real_batch_size]).mean(0)

        self.buffer.add_data(examples=not_aug_inputs,
                             labels=labels[:real_batch_size])

        return first_loss + loss.item()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs
