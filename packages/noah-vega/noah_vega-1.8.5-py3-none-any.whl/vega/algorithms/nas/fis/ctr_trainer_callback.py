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

"""Base CTR model TrainerCallback."""

import logging
import vega
from vega.common import ClassFactory, ClassType
from vega.trainer.callbacks import Callback

logger = logging.getLogger(__name__)


@ClassFactory.register(ClassType.CALLBACK)
class CtrTrainerCallback(Callback):
    """CtrTrainerCallback module."""

    def __init__(self):
        """Constuct CtrTrainerCallback class."""
        super(CtrTrainerCallback, self).__init__()

    def before_train(self, logs=None):
        """Be called before the training process."""
        self.config = self.trainer.config

    def make_batch(self, batch):
        """
        Make a batch data for ctr trainer.

        :param batch: a batch data
        :return: batch data, seperate input and target
        """
        input, target = batch
        if vega.is_gpu_device():
            input, target = input.cuda(), target.cuda()
        elif vega.is_npu_device():
            input, target = input.to(vega.get_devices()), target.to(vega.get_devices())
        return (input, target)
