import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import SGD, Adam

import numpy as np
from models.deepinversion import DeepInversion

# AlwaysBeDreaming
class ABD(DeepInversion):
    def __init__(self, args):
        super(ABD, self).__init__(args)
        self.kl_loss = nn.KLDivLoss(reduction='batchmean').to(self.device)

    def update_model(self, inputs, targets, target_scores=None, kd_index=None):

        # class balancing
        mappings = torch.ones(targets.size(), dtype=torch.float32).to(self.device)

        rnt = 1.0 * self.last_valid_out_dim / self.valid_out_dim
        mappings[:self.last_valid_out_dim] = rnt
        mappings[self.last_valid_out_dim:] = 1 - rnt

        # forward pass
        logits_pen = self.net.features(inputs)
        logits = self.net.classifier(logits_pen)[:, :self.valid_out_dim]

        # classification
        if self.inversion_replay:

            # local classification
            batch_size = inputs.shape[0] / 2
            class_idx = np.arange(batch_size)

            loss_class = self.criterion(logits[class_idx, self.last_valid_out_dim:self.valid_out_dim],
                                        (targets[class_idx] - self.last_valid_out_dim).long())

            # ft classification
            with torch.no_grad():
                feat_class = self.net.features(inputs).detach()
            loss_class += self.criterion(self.net.classifier(feat_class), targets.long())

        else:
            loss_class = self.criterion(logits, targets.long())

        # KD
        if target_scores is not None:

            # hard - linear
            logits_KD = self.previous_classifier(logits_pen)[:, :self.last_valid_out_dim]
            logits_KD_past = self.previous_teacher.generate_scores_pen(inputs)[:,
                             :self.last_valid_out_dim]
            # logits_KD_past = target_scores
            loss_kd = self.mu * (self.kd_criterion(logits_KD, logits_KD_past.detach()).sum(dim=1)).mean() / (
                logits_KD.size(1))


        else:
            loss_kd = torch.zeros((1,), requires_grad=True).to(self.device)

        total_loss = loss_class + loss_kd

        self.optimizer.zero_grad()
        total_loss.backward()
        self.optimizer.step()

        return total_loss.detach(), loss_class.detach(), loss_kd.detach(), logits


