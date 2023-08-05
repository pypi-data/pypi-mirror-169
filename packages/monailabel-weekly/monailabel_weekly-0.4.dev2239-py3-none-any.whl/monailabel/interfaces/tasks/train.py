# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod

from monailabel.interfaces.datastore import Datastore


class TrainTask(metaclass=ABCMeta):
    """
    Basic Train Task
    """

    def __init__(self, description):
        self.description = description

    def info(self):
        return {"description": self.description, "config": self.config()}

    def config(self):
        return {}

    def stats(self):
        return {}

    @abstractmethod
    def __call__(self, request, datastore: Datastore):
        pass
