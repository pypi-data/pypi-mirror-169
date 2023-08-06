import torch
import torch.nn as nn
import torch.nn.functional as F

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18, resnet34
from deepinc.models.utils.incremental_model import IncrementalModel

def get_params(net) -> torch.Tensor:
    """
    Returns all the parameters concatenated in a single tensor.
    :return: parameters tensor (??)
    """
    params = []
    for pp in list(net.parameters()):
        params.append(pp.view(-1))
    return torch.cat(params)

def get_grads(net) -> torch.Tensor:
    """
    Returns all the gradients concatenated in a single tensor.
    :return: gradients tensor (??)
    """
    grads = []
    for pp in list(net.parameters()):
        grads.append(pp.grad.view(-1))
    return torch.cat(grads)

class SI(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(SI, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.checkpoint = None
        self.big_omega = None
        self.small_omega = 0

    # 任务初始化
    def begin_il(self, dataset):
        if self.args.dataset == 'seq-mnist':
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)
        else:
            if self.args.backbone == 'None' or self.args.backbone == 'resnet18':
                self.net = resnet18(dataset.nc).to(self.device)
            elif self.args.backbone == 'resnet34':
                self.net = resnet34(dataset.nc).to(self.device)

    def train_task(self, dataset, train_loader):
        self.before_task()
        self.train_(train_loader)
        self.end_task()

    def before_task(self):
        self.checkpoint = get_params(self.net).data.clone().to(self.device)

    def train_(self, train_loader):
        self.net.train()
        opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                outputs = self.net(inputs)
                penalty = self.penalty()
                loss = self.loss(outputs, labels) + self.args.c * penalty

                opt.zero_grad()
                loss.backward()
                nn.utils.clip_grad.clip_grad_value_(self.net.parameters(), 1)
                opt.step()

                self.small_omega += self.args.lr * get_grads(self.net).data ** 2
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))

    def end_task(self):
        # big omega calculation step
        if self.big_omega is None:
            self.big_omega = torch.zeros_like(get_params(self.net)).to(self.device)

        self.big_omega += self.small_omega / ((get_params(self.net).data - self.checkpoint) ** 2 + self.args.xi)

        # store parameters checkpoint and reset small_omega
        self.checkpoint = get_params(self.net).data.clone().to(self.device)
        self.small_omega = 0

    def penalty(self):
        if self.big_omega is None:
            return torch.tensor(0.0).to(self.device)
        else:
            penalty = (self.big_omega * ((get_params(self.net) - self.checkpoint) ** 2)).sum()
            return penalty

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs



