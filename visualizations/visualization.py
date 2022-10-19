# author: lgx
# date: 2022-10-19 13:47:41
# description:
import torch
import torch.nn as nn


class MyVis(nn.Module):
    def __init__(self, **kwargs):
        super(MyVis, self).__init__(**kwargs)

    def forward(self, images,  outputs, prefix):
        pass
