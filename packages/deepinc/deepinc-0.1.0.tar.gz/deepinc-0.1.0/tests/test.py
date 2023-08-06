#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `deepinc` package."""


import deepinc as di
from deepinc.utils.args import get_args
from deepinc.utils.training import train_il

args = get_args()

args.model = 'lwf'              # 模型名称
args.dataset = 'seq-mnist'      # 数据集
args.print_freq = 1             # 报告loss的频率
args.n_epochs = 1               # 迭代次数
args.device = 'cpu'             # 设备

args.lr = 0.02                  # 学习率
args.batch_size = 64            # batch size
args.alpha = 5                  # 蒸馏损失权重
args.softmax_temp = 2.0         # 蒸馏损失温度系数
args.wd_reg = 5e-5              # 正则项权重

train_il(args)


