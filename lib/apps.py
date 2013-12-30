# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Thomas Quintana <quintana.thomas@gmail.com>

from pykka import ActorRegistry

class ActorLifeCycleManager(object):
  def __init__(self):
    self.__actors__ = dict()

  def __load_actor__(self):
    return None

  def get_instance(self, key):
    actor, type = self.__actors__.get(key)
    return actor

  def get_type(self, key):
    actor, type = self.__actors__.get(key)
    return type

  def register(self, key, actor, type = 'class'):
    if type == 'class':
      pass
    elif type == 'instance':
      pass
    elif type == 'producer':
      pass
    elif type == 'singleton':
      pass

  def unregister(self, key):
    pass