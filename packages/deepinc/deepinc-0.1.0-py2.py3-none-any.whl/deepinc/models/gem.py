import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam
import quadprog
import numpy as np
from torch.utils.data import DataLoader, Dataset

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.models.utils.incremental_model import IncrementalModel
from deepinc.utils.buffer import Buffer

def store_grad(params, grads, grad_dims):
    """
        This stores parameter gradients of past tasks.
        pp: parameters
        grads: gradients
        grad_dims: list with number of parameters per layers
    """
    # store the gradients
    grads.fill_(0.0)
    count = 0
    for param in params():
        if param.grad is not None:
            begin = 0 if count == 0 else sum(grad_dims[:count])
            end = np.sum(grad_dims[:count + 1])
            grads[begin: end].copy_(param.grad.data.view(-1))
        count += 1


def overwrite_grad(params, newgrad, grad_dims):
    """
        This is used to overwrite the gradients with a new gradient
        vector, whenever violations occur.
        pp: parameters
        newgrad: corrected gradient
        grad_dims: list storing number of parameters at each layer
    """
    count = 0
    for param in params():
        if param.grad is not None:
            begin = 0 if count == 0 else sum(grad_dims[:count])
            end = sum(grad_dims[:count + 1])
            this_grad = newgrad[begin: end].contiguous().view(
                param.grad.data.size())
            param.grad.data.copy_(this_grad)
        count += 1

def project2cone2(gradient, memories, margin=0.5, eps=1e-3):
    """
        Solves the GEM dual QP described in the paper given a proposed
        gradient "gradient", and a memory of task gradients "memories".
        Overwrites "gradient" with the final projected update.

        input:  gradient, p-vector
        input:  memories, (t * p)-vector
        output: x, p-vector
    """
    memories_np = memories.cpu().t().double().numpy()
    gradient_np = gradient.cpu().contiguous().view(-1).double().numpy()
    n_rows = memories_np.shape[0]
    self_prod = np.dot(memories_np, memories_np.transpose())
    self_prod = 0.5 * (self_prod + self_prod.transpose()) + np.eye(n_rows) * eps
    grad_prod = np.dot(memories_np, gradient_np) * -1
    G = np.eye(n_rows)
    h = np.zeros(n_rows) + margin
    v = quadprog.solve_qp(self_prod, grad_prod, G, h)[0]
    x = np.dot(v, memories_np) + gradient_np
    gradient.copy_(torch.from_numpy(x).view(-1, 1))

class GEM(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(GEM, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.current_task = 0
        self.buffer = Buffer(self.args.buffer_size, self.device)

        self.transform = None

        # 任务初始化
    def begin_il(self, dataset):
        self.nt = dataset.nt
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.net = resnet18(dataset.nc).to(self.device)
        elif self.args.dataset == 'seq-tinyimg':
            self.net = resnet18(dataset.nc).to(self.device)
        else:
            self.net = MNISTMLP(28*28, dataset.nc).to(self.device)

        # Allocate temporary synaptic memory
        self.grad_dims = []
        for pp in self.net.parameters():
            self.grad_dims.append(pp.data.numel())

        self.grads_cs = []
        self.grads_da = torch.zeros(np.sum(self.grad_dims)).to(self.device)

    def train_task(self, dataset, train_loader):
        self.cpt = int(dataset.nc / dataset.nt)
        self.t_c_arr = dataset.t_c_arr
        self.eye = torch.tril(torch.ones((dataset.nc, dataset.nc))).bool().to(self.device)

        self.train_(train_loader)
        self.end_task(train_loader)

    def end_task(self, train_loader):
        self.current_task += 1
        self.grads_cs.append(torch.zeros(
            np.sum(self.grad_dims)).to(self.device))

        # add data to the buffer
        samples_per_task = self.args.buffer_size // self.nt

        cur_x, cur_y = next(iter(train_loader))
        self.buffer.add_data(
            examples=cur_x[:samples_per_task].to(self.device),
            labels=cur_y[:samples_per_task].to(self.device),
            task_labels=torch.ones(samples_per_task,
                dtype=torch.long).to(self.device) * (self.current_task - 1)
        )

    def train_(self, train_loader):
        self.net.train()
        opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        loss_fn = F.cross_entropy
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                if not self.buffer.is_empty():
                    buf_inputs, buf_labels, buf_task_labels = self.buffer.get_data(
                        self.args.buffer_size, transform=self.transform)

                    for tt in buf_task_labels.unique():
                        # compute gradient on the memory buffer
                        opt.zero_grad()
                        cur_task_inputs = buf_inputs[buf_task_labels == tt]
                        cur_task_labels = buf_labels[buf_task_labels == tt]
                        cur_task_outputs = self.net(cur_task_inputs)
                        penalty = loss_fn(cur_task_outputs, cur_task_labels)
                        penalty.backward()
                        store_grad(self.net.parameters, self.grads_cs[tt], self.grad_dims)

                # now compute the grad on the current data
                outputs = self.net(inputs)
                loss = loss_fn(outputs, labels)
                # loss = loss_fn(outputs, labels).requires_grad_(True)
                # print(loss.require_grad)
                opt.zero_grad()
                loss.backward()

                # check if gradient violates buffer constraints
                if not self.buffer.is_empty():
                    # copy gradient
                    store_grad(self.net.parameters, self.grads_da, self.grad_dims)

                    dot_prod = torch.mm(self.grads_da.unsqueeze(0),
                                        torch.stack(self.grads_cs).T)
                    if (dot_prod < 0).sum() != 0:
                        project2cone2(self.grads_da.unsqueeze(1),
                                      torch.stack(self.grads_cs).T, margin=self.args.gamma)
                        # copy gradients back
                        overwrite_grad(self.net.parameters, self.grads_da,
                                       self.grad_dims)

                opt.step()

            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs



