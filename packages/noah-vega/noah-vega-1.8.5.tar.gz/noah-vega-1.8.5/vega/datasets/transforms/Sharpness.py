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

"""This is a class for Sharpness."""
from PIL import ImageEnhance
from vega.common import ClassFactory, ClassType
from .ops import float_parameter


@ClassFactory.register(ClassType.TRANSFORM)
class Sharpness(object):
    """Applies Sharpness to 'img'.

    The Sharpness operation adjusts the sharpness of the image, level = 0 gives a blurred image,
    whereas level = 1 gives the original image
    :param level: Strength of the operation specified as an Integer from [0, 'PARAMETER_MAX'].
    :type level: int
    """

    def __init__(self, level):
        """Construct the Sharpness class."""
        self.level = level

    def __call__(self, img):
        """Call function of Sharpness.

        :param img: input image
        :type img: numpy or tensor
        :return: the image after transform
        :rtype: numpy or tensor
        """
        v = float_parameter(self.level, 1.8) + .1
        return ImageEnhance.Sharpness(img).enhance(v)
