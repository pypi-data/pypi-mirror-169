import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import numpy as np
import math

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel
from deepinc.datasets.utils.validation import ValidationDataset
from deepinc.utils.args import *
from deepinc.utils.buffer import Buffer

class JOINT(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(JOINT, self).__init__(args)

        self.old_data = []
        self.old_labels = []
        self.current_task = 0

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.current_task = 0

        self.train_transform = transforms.Compose([
                transforms.RandomCrop(32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor()])

    def get_net(self, dataset):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.net = resnet18(dataset.nc).to(self.device)
        elif self.args.dataset == 'seq-tinyimg':
            self.net = resnet18(dataset.nc).to(self.device)
        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)

    def begin_il(self, dataset):
        self.get_net(dataset)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.end_task(dataset, train_loader)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs

    def end_task(self, dataset, train_loader):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10' or self.args.dataset == 'seq-tinyimg' or self.args.dataset == 'seq-mnist':
            self.old_data.append(dataset.train_loader.dataset.data)
            self.old_labels.append(torch.tensor(dataset.train_loader.dataset.targets))
            self.current_task += 1

            # # for non-incremental joint training
            if len(dataset.test_loaders) != dataset.N_TASKS: return

            # reinit network
            self.get_net(dataset)
            self.net.train()
            self.opt = SGD(self.net.parameters(), lr=self.args.lr)


            # prepare dataloader
            all_data, all_labels = None, None
            for i in range(len(self.old_data)):
                if all_data is None:
                    all_data = self.old_data[i]
                    all_labels = self.old_labels[i]
                else:
                    all_data = np.concatenate([all_data, self.old_data[i]])
                    all_labels = np.concatenate([all_labels, self.old_labels[i]])

            transform = train_loader.dataset.transform if train_loader.dataset.transform is not None else transforms.ToTensor()

            temp_dataset = ValidationDataset(all_data, all_labels, transform=transform)
            loader = torch.utils.data.DataLoader(temp_dataset, batch_size=self.args.batch_size, shuffle=True)

            # train
            for e in range(self.args.n_epochs):
                for i, batch in enumerate(loader):
                    inputs, labels = batch
                    inputs, labels = inputs.to(self.device), labels.to(self.device)

                    self.opt.zero_grad()
                    outputs = self.net(inputs)
                    loss = self.loss(outputs, labels.long())
                    loss.backward()
                    self.opt.step()
                    #progress_bar(i, len(loader), e, 'J', loss.item())

                if e % self.args.print_freq == 0:
                    print('epoch:%d, loss:%.5f' % (e, loss))
        else:
            self.old_data.append(dataset.train_loader)
            # train
            if len(dataset.test_loaders) != dataset.N_TASKS: return
            loader_caches = [[] for _ in range(len(self.old_data))]
            sources = torch.randint(5, (128,))
            all_inputs = []
            all_labels = []
            for source in self.old_data:
                for x, l, _ in source:
                    all_inputs.append(x)
                    all_labels.append(l)
            all_inputs = torch.cat(all_inputs)
            all_labels = torch.cat(all_labels)
            bs = self.args.batch_size
            for e in range(self.args.n_epochs):
                order = torch.randperm(len(all_inputs))
                for i in range(int(math.ceil(len(all_inputs) / bs))):
                    inputs = all_inputs[order][i * bs: (i+1) * bs]
                    labels = all_labels[order][i * bs: (i+1) * bs]
                    inputs, labels = inputs.to(self.device), labels.to(self.device)
                    self.opt.zero_grad()
                    outputs = self.net(inputs)
                    loss = self.loss(outputs, labels.long())
                    loss.backward()
                    self.opt.step()
                    #progress_bar(i, int(math.ceil(len(all_inputs) / bs)), e, 'J', loss.item())

                if e % self.args.print_freq == 0:
                    print('epoch:%d, loss:%.5f' % (e, loss))
