# author: lgx
# date: 2022-10-19 12:48:15
# description:
from torch.utils.data import Dataset
from torchvision.transforms import *


class MyDataset(Dataset):
    def __init__(self, transform_dict=None, **kwargs):
        super(MyDataset, self).__init__(**kwargs)
        self.transform_dict = transform_dict
        self.transform = self.init_transform()
        self.data_infos = ['1.jpg']

    def __len__(self):
        return len(self.data_infos)

    def init_transform(self):
        if self.transform_dict is None:
            return None
        transform = transforms.Compose(
            [eval(k)(**v) if (v is not None) else eval(k)() for k, v in self.transform_dict.items()]
        )
        return transform

    def __getitem__(self, item):
        input = self._get_input(item)
        target = self._generate_target(item)
        return input, target

    def _get_input(self, item):
        info = self.data_infos[item]
        input = 0
        if self.transform is not None:
            input = self.transform(input)
        return input

    def _generate_target(self, item):
        info = self.data_infos[item]
        target = 0
        return target

    # used for debug
    def visualize(self, input, target, save_path=None):
        pass

