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
import argparse

from stitcher.stitcher import Stitcher


def get_args():
    parser = argparse.ArgumentParser("Stitch C-Debian call graphs")
    parser.add_argument(
        "callgraphs",
        nargs="*",
        help="Paths to call graphs to be stitched together in FASTEN format"
    )
    parser.add_argument(
        "-o",
        "--output",
        help=("File to save the stitched call graph. "
              "If not given the graph will be printed in standard output."),
        default=None
    )
    parser.add_argument(
        "-k",
        "--keep-unresolved",
        help="Keep nodes of missing call graphs",
        action="store_true"
    )
    return parser.parse_args()


def main():
    args = get_args()

    stitcher = Stitcher(args.callgraphs, args.keep_unresolved)
    stitcher.stitch()

    output = json.dumps(stitcher.output(), indent=4)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
