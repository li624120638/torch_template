# author: lgx
# date: 2022-10-19 13:09:50
# description:
import torch
import torch.nn as nn


class MyLoss(nn.Module):
    def __init__(self, **kwargs):
        super(MyLoss, self).__init__(**kwargs)

    def forward(self, target, output):
        pass

