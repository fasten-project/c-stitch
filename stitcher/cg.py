#
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
from stitcher.node import Node


class CallGraph:
    def __init__(self, cg):
        self.cg = cg

        self.internal_calls = []
        self.external_calls = []  # Unresolved calls
        self.resolved_calls = []  # External resolved calls

        self.internal_nodes = set()
        self.external_nodes = set()

        self.id_to_node = {}

        self.dependencies = set()
        self.alternatives = {}

        self.product = self.cg["product"]
        self.version = self.cg["version"]

        self._parse_depset()
        self._parse_nodes()
        self._parse_edges()

    def _parse_nodes(self):
        def parse_methods(methods, internal):
            for node_id, properties in methods.items():
                if internal:
                    node = Node(
                        properties['uri'], properties['metadata'],
                        self.product, self.version
                    )
                    self.internal_nodes.add(node.to_string())
                else:
                    node = Node(properties['uri'], properties['metadata'])
                    self.external_nodes.add(node.to_string())
                self.id_to_node[node_id] = node

        # Internal nodes
        internal = self.cg['functions']['internal']
        for methods in internal['binaries'].values():
            parse_methods(methods['methods'], True)
        parse_methods(internal['static_functions']['methods'], True)

        # External nodes
        external = self.cg['functions']['external']
        for methods in external['products'].values():
            parse_methods(methods['methods'], False)
        parse_methods(external['undefined']['methods'], False)
        for methods in external['static_functions'].values():
            parse_methods(methods['methods'], False)

    def _parse_edges(self):
        lookup = {
            "externalCalls": self.external_calls,
            "internalCalls": self.internal_calls,
            "resolvedCalls": self.resolved_calls
        }
        for call_type, edges in self.cg['graph'].items():
            res = lookup[call_type]
            for src, dst, _ in edges:
                # TODO add check
                res.append([self.id_to_node[src], self.id_to_node[dst]])

    def _parse_depset(self):
        def parse_dep(dep, alternatives=None):
            if dep['dependency_type'] == 'Alternatives':
                for alt in dep['alternatives']:
                    parse_dep(alt, dep['alternatives'])
            else:
                self.dependencies.add(dep['product'])
                if alternatives is not None:
                    for alt in alternatives:
                        if alt['product'] != dep['product']:
                            self.alternatives[dep['product']] = alt['product']

        deps = self.cg['depset'] + self.cg['build_depset'] + \
            self.cg['undeclared_depset']
        for dep in deps:
            parse_dep(dep)
