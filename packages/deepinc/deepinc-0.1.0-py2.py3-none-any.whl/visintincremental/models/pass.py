import numpy as np

import torch
from torch.optim import SGD, Adam
import torch.nn as nn
from torch.optim.lr_scheduler import StepLR
import torchvision.models as models

from deepinc.backbone.MNISTMLP import MNISTMLP
from deepinc.backbone.ResNet import resnet18
from deepinc.backbone.VAE import VAE
from deepinc.backbone.VAE_MLP import VAE_MLP
from deepinc.models.utils.incremental_model import IncrementalModel

class network(nn.Module):
    def __init__(self, numclass, feature_extractor, hidden_dim=512):
        super(network, self).__init__()
        self.feature = feature_extractor
        self.fc = nn.Linear(hidden_dim, numclass, bias=True)

    def forward(self, input):
        x = self.feature(input)
        x = self.fc(x)
        return x

    def Incremental_learning(self, numclass):
        weight = self.fc.weight.data
        bias = self.fc.bias.data
        in_feature = self.fc.in_features
        out_feature = self.fc.out_features

        self.fc = nn.Linear(in_feature, numclass, bias=True)
        self.fc.weight.data[:out_feature] = weight[:out_feature]
        self.fc.bias.data[:out_feature] = bias[:out_feature]

    def feature_extractor(self,inputs):
        return self.feature(inputs)

class PASS(IncrementalModel):
    COMPATIBILITY = ['class-il', 'task-il']

    def __init__(self, args):
        super(PASS, self).__init__(args)

        self.epochs = args.n_epochs
        self.learning_rate = args.lr
        self.model = None
        self.radius = 0
        self.prototype = None
        self.class_label = None
        self.numclass = 0
        self.currenttask = -1
        self.t_c_arr = None
        self.old_model = None

        self.embedding_dim = -1

        self.train_loader = None
        self.test_loader = None

    # 任务初始化
    def begin_il(self, dataset):
        if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
            self.embedding_dim = 512
            if self.args.isPretrain:
                net = models.resnet18(pretrained=True)
                net.fc = nn.Linear(self.embedding_dim, self.embedding_dim)
            else:
                net = resnet18(self.embedding_dim).to(self.device)
            self.model = network(dataset.nc*4, feature_extractor=net, hidden_dim=self.embedding_dim)
        elif self.args.dataset == 'seq-tinyimg':
            self.embedding_dim = 512
            net = resnet18(self.embedding_dim).to(self.device)
            self.model = network(dataset.nc*4, feature_extractor=net, hidden_dim=self.embedding_dim)
        else:
            self.embedding_dim = 100
            net = MNISTMLP(28*28, self.embedding_dim).to(self.device)
            self.model = network(dataset.nc*4, feature_extractor=net, hidden_dim=self.embedding_dim)

        self.t_c_arr = dataset.t_c_arr

    def train_task(self, dataset, train_loader):
        self.currenttask += 1
        self.train_loader = train_loader
        self.test_loader = dataset.test_loaders

        self.current_classes = self.t_c_arr[self.currenttask]

        self.beforeTrain(self.currenttask, train_loader)
        self.train(self.currenttask, old_class=self.current_classes[0])
        self.afterTrain(self.currenttask)

    def beforeTrain(self, current_task, train_loader):
        self.model.eval()
        self.numclass += len(self.t_c_arr[self.currenttask])
        # if current_task > 0:
        #     self.model.Incremental_learning(4 * self.numclass)
        self.model.train()
        self.model.to(self.device)

    def train(self, current_task, old_class=0):
        opt = torch.optim.Adam(self.model.parameters(), lr=self.learning_rate, weight_decay=2e-4)
        scheduler = StepLR(opt, step_size=45, gamma=0.1)
        accuracy = 0
        for epoch in range(self.epochs):
            scheduler.step()
            for step, (images, target) in enumerate(self.train_loader):
                images, target = images.to(self.device), target.to(self.device)

                # self-supervised learning based label augmentation
                images = torch.stack([torch.rot90(images, k, (2, 3)) for k in range(4)], 1)
                if self.args.dataset == 'seq-cifar100' or self.args.dataset == 'seq-cifar10':
                    images = images.view(-1, 3, 32, 32)
                elif self.args.dataset == 'seq-mnist':
                    images = images.view(-1, 1, 28, 28)
                elif self.args.dataset == 'seq-tinyimg':
                    images = images.view(-1, 3, 64, 64)

                target = torch.stack([target * 4 + k for k in range(4)], 1).view(-1)

                opt.zero_grad()
                loss = self._compute_loss(images, target, old_class)
                opt.zero_grad()
                loss.backward()
                opt.step()
            if epoch % self.args.print_freq == 0:
                accuracy = self._test(self.test_loader)
                print('epoch:%d, accuracy:%.5f' % (epoch, accuracy))
        self.protoSave(self.model, self.train_loader, current_task)

    def _test(self, testloaders):
        self.model.eval()
        correct, total = 0.0, 0.0
        for testloader in testloaders:
            for setp, (imgs, labels) in enumerate(testloader):
                imgs, labels = imgs.to(self.device), labels.to(self.device)
                with torch.no_grad():
                    outputs = self.model(imgs)
                outputs = outputs[:, ::4]  # only compute predictions on original class nodes
                predicts = torch.max(outputs, dim=1)[1]
                correct += (predicts.cpu() == labels.cpu()).sum()
                total += len(labels)
        accuracy = correct.item() / total
        self.model.train()
        return accuracy

    def _compute_loss(self, imgs, target, old_class=0):
        output = self.model(imgs)
        output, target = output.to(self.device), target.to(self.device)
        loss_cls = nn.CrossEntropyLoss()(output/self.args.temp, target)
        if self.old_model is None:
            return loss_cls
        else:
            feature = self.model.feature(imgs)
            feature_old = self.old_model.feature(imgs)
            loss_kd = torch.dist(feature, feature_old, 2)

            proto_aug = []
            proto_aug_label = []
            index = list(range(old_class))
            for _ in range(self.args.batch_size):
                np.random.shuffle(index)
                temp = self.prototype[index[0]] + np.random.normal(0, 1, self.embedding_dim) * self.radius
                proto_aug.append(temp)
                proto_aug_label.append(4*self.class_label[index[0]])

            proto_aug = torch.from_numpy(np.float32(np.asarray(proto_aug))).float().to(self.device)
            proto_aug_label = torch.from_numpy(np.asarray(proto_aug_label)).to(self.device)
            soft_feat_aug = self.model.fc(proto_aug)
            loss_protoAug = nn.CrossEntropyLoss()(soft_feat_aug/self.args.temp, proto_aug_label)

            return loss_cls + self.args.protoAug_weight*loss_protoAug + self.args.kd_weight*loss_kd

    def afterTrain(self, current_task):
        path = self.args.img_dir
        filename = path + '%d_model.pkl' % (current_task)
        torch.save(self.model, filename)
        self.old_model = torch.load(filename)
        self.old_model.to(self.device)
        self.old_model.eval()

    def protoSave(self, model, loader, current_task):
        features = []
        labels = []
        model.eval()
        with torch.no_grad():
            for i, (images, target) in enumerate(loader):
                feature = model.feature(images.to(self.device))
                if feature.shape[0] == self.args.batch_size:
                    labels.append(target.numpy())
                    features.append(feature.cpu().numpy())
        labels_set = np.unique(labels)
        labels = np.array(labels)
        labels = np.reshape(labels, labels.shape[0] * labels.shape[1])
        features = np.array(features)
        features = np.reshape(features, (features.shape[0] * features.shape[1], features.shape[2]))
        feature_dim = features.shape[1]

        prototype = []
        radius = []
        class_label = []
        for item in labels_set:
            index = np.where(item == labels)[0]
            class_label.append(item)
            feature_classwise = features[index]
            prototype.append(np.mean(feature_classwise, axis=0))
            if current_task == 0:
                cov = np.cov(feature_classwise.T)
                radius.append(np.trace(cov) / feature_dim)

        if current_task == 0:
            self.radius = np.sqrt(np.mean(radius))
            self.prototype = prototype
            self.class_label = class_label
            print(self.radius)
        else:
            self.prototype = np.concatenate((prototype, self.prototype), axis=0)
            self.class_label = np.concatenate((class_label, self.class_label), axis=0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        self.model.eval()
        x = x.to(self.device)
        with torch.no_grad():
            outputs = self.model(x)
        outputs = outputs[:, ::4]  # only compute predictions on original class nodes
        return outputs



