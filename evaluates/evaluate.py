# author: lgx
# date: 2022-10-19 13:13:10
# description:
import torch
import torch.nn as nn


class MyMetric(nn.Module):
    def __init__(self, **kwargs):
        super(MyMetric, self).__init__(**kwargs)

    def forward(self, target, output):
        pass
