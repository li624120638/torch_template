# author: lgx
# date: 2022-10-19 13:45:13
# description:

import torch
import torch.nn as nn


class MyModel(nn.Module):
    def __init__(self, **kwargs):
        super(MyModel, self).__init__(**kwargs)
        self.fc = nn.Linear(2, 3)

    def forward(self, inputs):
        res = self.fc(inputs)
        return res

