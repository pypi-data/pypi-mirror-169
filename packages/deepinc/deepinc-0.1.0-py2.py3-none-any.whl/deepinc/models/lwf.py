import torch
import torch.nn.functional as F
from torch.optim import SGD
from torch.utils.data import DataLoader

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18, resnet34
from deepinc.models.utils.incremental_model import IncrementalModel

def smooth(logits, temp, dim):
    log = logits ** (1 / temp)
    return log / torch.sum(log, dim).unsqueeze(1)

def modified_kl_div(old, new):
    return -torch.mean(torch.sum(old * torch.log(new), 1))

class LWF(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(LWF, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.net = None
        self.loss = F.cross_entropy

        self.soft = torch.nn.Softmax(dim=1)
        self.logsoft = torch.nn.LogSoftmax(dim=1)

        self.alpha = args.alpha
        self.softmax_temp = args.softmax_temp
        self.wd_reg = args.wd_reg

        self.current_task = 0

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

        self.before_task(train_loader)
        self.train_(train_loader)

    def before_task(self, train_loader):
        self.net.eval()
        if self.current_task > 0:
            # warm-up 对全连接层中此任务的参数进行训练
            opt = SGD(self.net.classifier.parameters(), lr=self.args.lr)
            for epoch in range(self.args.n_epochs):
                for i, data in enumerate(train_loader):
                    inputs, labels = data[0].to(self.device), data[1].to(self.device)
                    opt.zero_grad()
                    with torch.no_grad():  # 梯度不影响前面的层
                        feats = self.net.features(inputs)  # 计算前面层的特征
                    # 仅为此任务的输出为True，反之为False。目的是只修改此任务的全连接层参数
                    mask = self.eye[(self.current_task + 1) * self.cpt - 1] ^ self.eye[self.current_task * self.cpt - 1]
                    outputs = self.net.classifier(feats)[:, mask]  # 只有最后一层的此任务的参数才有梯度，即对最后这些参数进行梯度下降
                    # print(labels - self.current_task * self.cpt)
                    loss = self.loss(outputs, labels - self.current_task * self.cpt)
                    loss.backward()
                    opt.step()

            # 计算旧类别的输出，用于蒸馏损失
            dataset = train_loader.dataset
            loader = DataLoader(dataset, batch_size=self.args.batch_size, shuffle=False)
            logits = []
            with torch.no_grad():
                for i, data in enumerate(loader):
                    inputs = data[0].to(self.device)
                    log = self.net(inputs).cpu()
                    logits.append(log)
            dataset.set_att("logits", torch.cat(logits))
        self.net.train()
        self.current_task += 1


    def train_(self, train_loader):
        self.net.train()
        opt = torch.optim.SGD(self.net.parameters(), lr=self.learning_rate)
        for epoch in range(self.epochs):
            for step, data in enumerate(train_loader):
                inputs, labels = data[0].to(self.device), data[1].to(self.device)

                outputs = self.net(inputs)
                mask = self.eye[self.current_task * self.cpt - 1]
                loss = self.loss(outputs[:, mask], labels)

                if self.current_task > 1:
                    logits = data[3].to(self.device)
                    mask = self.eye[(self.current_task - 1) * self.cpt - 1]
                    loss += self.args.alpha * modified_kl_div(smooth(self.soft(logits[:, mask]).to(self.device), 2, 1),
                                                              smooth(self.soft(outputs[:, mask]), 2, 1))

                loss += self.args.wd_reg * torch.sum(self.net.get_params() ** 2)

                opt.zero_grad()
                loss.backward()
                opt.step()
            if epoch % self.args.print_freq == 0:
                print('epoch:%d, loss:%.5f' % (epoch, loss.to('cpu').item()))


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.net.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.net(x)
        return outputs



