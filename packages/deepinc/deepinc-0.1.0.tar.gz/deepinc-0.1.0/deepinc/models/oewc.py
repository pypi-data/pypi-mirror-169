import torch
import torch.nn.functional as F

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18, resnet34
from deepinc.models.utils.incremental_model import IncrementalModel


class OEWC(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(OEWC, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.args.gamma = args.gamma
        self.args.e_lambda = args.e_lambda

        self.soft = torch.nn.Softmax(dim=1)
        self.logsoft = torch.nn.LogSoftmax(dim=1)
        self.checkpoint = None
        self.fish = None

        self.current_task = 0

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
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.train_(train_loader)
        self.end_task(dataset)

    def train_(self, train_loader):
        self.net.train()
        self.opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                self.opt.zero_grad()
                outputs = self.net(inputs)
                penalty = self.penalty()
                loss = self.loss(outputs, labels) + self.args.e_lambda * penalty
                assert not torch.isnan(loss)
                loss.backward()
                self.opt.step()

            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))

    def end_task(self, dataset):
        fish = torch.zeros_like(self.net.get_params())

        for j, data in enumerate(dataset.train_loader):
            inputs, labels = data[0].to(self.device), data[1].to(self.device)
            for ex, lab in zip(inputs, labels):
                self.opt.zero_grad()
                output = self.net(ex.unsqueeze(0))
                loss = - F.nll_loss(self.logsoft(output), lab.unsqueeze(0),
                                    reduction='none')
                exp_cond_prob = torch.mean(torch.exp(loss.detach().clone()))
                loss = torch.mean(loss)
                loss.backward()
                fish += exp_cond_prob * self.net.get_grads() ** 2

        fish /= (len(dataset.train_loader) * self.args.batch_size)

        if self.fish is None:
            self.fish = fish
        else:
            self.fish *= self.args.gamma
            self.fish += fish

        self.checkpoint = self.net.get_params().data.clone()


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs

    def penalty(self):
        if self.checkpoint is None:
            return torch.tensor(0.0).to(self.device)
        else:
            penalty = (self.fish * ((self.net.get_params() - self.checkpoint) ** 2)).sum()
            return penalty



