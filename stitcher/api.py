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
import json

from flask import Flask, request
from stitcher.stitcher import Stitcher

app = Flask(__name__)

@app.route('/stitch',  methods = ['POST'])
def stitch():
    content = request.json
    stitcher = Stitcher([], False)
    for cg in content.values():
        stitcher.parse_cg(cg)
    stitcher.stitch()

    output = json.dumps(stitcher.output(), indent=4)

    return output


def deploy(host='0.0.0.0', port=5000):
    app.run(threaded=True, host=host, port=port)