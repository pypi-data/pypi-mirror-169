# -*- coding: utf-8 -*-

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a class for Imagenet dataset."""

from torchvision.datasets import ImageFolder
from vega.datasets.transforms.Compose import Compose
from vega.common import ClassFactory, ClassType
from vega.common import FileOps
from vega.datasets.conf.imagenet import ImagenetConfig
from .dataset import Dataset


@ClassFactory.register(ClassType.DATASET)
class Imagenet(Dataset):
    """This is a class for Imagenet dataset, wchich is the subclass of ImageNet and Dataset.

    :param mode: `train`,`val` or `test`, defaults to `train`
    :type mode: str, optional
    :param cfg: the config the dataset need, defaults to None, and if the cfg is None,
    the default config will be used, the default config file is a yml file with the same name of the class
    :type cfg: yml, py or dict
    """

    config = ImagenetConfig()

    def __init__(self, **kwargs):
        """Construct the Imagenet class."""
        Dataset.__init__(self, **kwargs)
        self.args.data_path = FileOps.download_dataset(self.args.data_path)
        split = 'train' if self.mode == 'train' else 'val'
        local_data_path = FileOps.join_path(self.args.data_path, split)
        self.image_folder = ImageFolder(root=local_data_path, transform=Compose(self.transforms.__transform__))

    @property
    def input_channels(self):
        """Input channel number of the Imagenet image.

        :return: the channel number
        :rtype: int
        """
        return 3

    @property
    def input_size(self):
        """Input size of Imagenet image.

        :return: the input size
        :rtype: int
        """
        return self.shape[1]

    def __len__(self):
        """Get the length of the dataset."""
        return self.image_folder.__len__()

    def __getitem__(self, index):
        """Get an item of the dataset according to the index."""
        return self.image_folder.__getitem__(index)
