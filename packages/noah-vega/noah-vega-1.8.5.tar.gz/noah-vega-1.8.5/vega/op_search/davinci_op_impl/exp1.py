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

"""This is a class for Exp1."""
from mindspore.ops import prim_attr_register, PrimitiveWithInfer


class Exp1(PrimitiveWithInfer):
    """Define Exp1 primitive."""

    @prim_attr_register
    def __init__(self):
        self.init_prim_io_names(inputs=['x'], outputs=['y'])
        from exp1_impl import Exp1Impl

    def infer_shape(self, data_shape):
        """Infer shape."""
        return data_shape

    def infer_dtype(self, data_dtype):
        """Infer dtype."""
        return data_dtype
