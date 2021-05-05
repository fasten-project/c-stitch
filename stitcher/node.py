# Copyright (c) 2018-2021 FASTEN.
#
# This file is part of FASTEN
# (see https://www.fasten-project.eu/).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
class Node:
    def __init__(self, uri_str, metadata, product="", version=""):
        self.uri_str = uri_str
        self.product = product
        self.version = version
        self.metadata = metadata
        self.internal = False
        self.external = False
        self.undefined = False
        self.static = False
        self.entity = ""

        if uri_str.startswith("///"):
            self.undefined = True
            self.external = True
            self.entity = uri_str[3:]
        elif uri_str.startswith("//"):
            self.external = True
            self.entity = uri_str[uri_str[2:].find('/')+3:]
            self.product = uri_str[2:uri_str.find('/', 2)]
        else:
            self.entity = uri_str[1:]
            self.internal = True

        if ';' in self.entity.split('/')[-1]:
            self.static = True

    def get_product(self):
        return self.product

    def get_version(self):
        return self.version

    def get_entity(self):
        return self.entity

    def to_string(self):
        forge_product_version = self.product  # For now we skip forge
        if self.version:
            forge_product_version += "$" + self.version
        return "fasten://{}/{}".format(forge_product_version, self.entity)
