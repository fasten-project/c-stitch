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
import sys
import json

from stitcher.cg import CallGraph

class Stitcher:
    def __init__(self, call_graph_paths):
        self.cgs = {}

        self.node_id_cnt = 0
        self.node_to_id = {}

        self.stitched = {
            "edges": [],
            "nodes": {}
        }

        self.resolved_cnt = 0
        self.unresolved_cnt = 0

        self.dependencies = set()

        self._parse_cgs(call_graph_paths)

    def stitch(self):
        def add_edge(src, dst):
            self._assign_id(src.to_string())
            self._assign_id(dst.to_string())
            self.stitched['edges'].append([
                self.node_to_id[src.to_string()],
                self.node_to_id[dst.to_string()]
            ])

        for cg in self.cgs.values():
            for src, dst in cg.internal_calls:
                add_edge(src, dst)
            for src, dst in cg.resolved_calls:
                # TODO handle missing cases
                dst = self._get_resolved_node(dst)
                if not dst:
                    self.unresolved_cnt += 1
                    continue
                add_edge(src, dst)
            for src, dst in cg.external_calls:
                # TODO handle missing cases
                dst = self._resolve(dst)
                if not dst:
                    self.unresolved_cnt += 1
                    continue
                dst = self._get_resolved_node(dst)
                if not dst:
                    self.unresolved_cnt += 1
                    continue
                add_edge(src, dst)

        for node, node_id in self.node_to_id.items():
            self.stitched["nodes"][node_id] = {"URI": node, "metadata": {}}

    def _get_resolved_node(self, node):
        if node.product not in self.cgs.keys():
            return None
        node.version = self.cgs[node.product].version
        # TODO Currently CScout does not detect declarations of static calls
        # Hence they exist only in edges
        if (node.to_string() not in self.cgs[node.product].internal_nodes and
                not node.static):
            return None
        return node

    def _resolve(self, node):
        # TODO we must handle virtual packages and alternatives
        node.product = node.metadata['product']
        return node

    def output(self):
        print("Number of Missing Dependencies: {}".format(
            len(self.dependencies - set(self.cgs.keys()))
        ))
        print("Number of Skipped (Unresolved) Edges: {}".format(
            self.unresolved_cnt
        ))
        print("Number of Nodes: {}".format(
            len(self.stitched['nodes'])
        ))
        print("Number of Resolved Edges: {}".format(
            len(self.stitched['nodes'])
        ))
        print("Number of Edges: {}".format(
            len(self.stitched['nodes']) + self.unresolved_cnt
        ))
        return self.stitched

    def _parse_cgs(self, paths):
        for p in paths:
            with open(p, "r") as f:
                cg = json.load(f)
                if self.cgs.get(cg["product"], None):
                    self._err_and_exit(
                        "Cannot stitch call graphs of the same product"
                    )
                self.cgs[cg["product"]] = CallGraph(cg)
                self.dependencies.update(self.cgs[cg["product"]].dependencies)

    def _err_and_exit(self, msg):
        print(msg)
        sys.exit(1)

    def _assign_id(self, node_str):
        if not node_str in self.node_to_id:
            self.node_to_id[node_str] = self.node_id_cnt
            self.node_id_cnt += 1
