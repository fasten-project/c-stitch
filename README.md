# Stiching for FASTEN C-Debian Call Graphs

In this repository you can find the implementation of a stitcher for C-Debian
call graphs written in Python along with a benchmark to test its functionality.

Contents:
* [stitcher](stitcher): The source code for the stitcher.
* [benchmark](benchmark): A minimal benchmark to test the stitcher's
  functionality.

## Installation

Installation requires an installation of Python3.
From the root directory, run:
```
python3 setup.py install
```

## Usage

```
c-stitch --help
usage: Stitch C-Debian call graphs [-h] [-o OUTPUT] [callgraphs ...]

positional arguments:
  callgraphs            Paths to call graphs to be stitched together in FASTEN format

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        File to save the stitched call graph. If not given the graph will be
                        printed in standard output.
```

* `call_graph`: A list of paths containing FASTEN C-Debian call graphs in JSON
  format.
* `output`: (Optional) parameter specifying where the stitched call graph will
  be stored.


## Benchmark

The benchmark directory consists of a micro-benchmark.

### Micro-benchmark

The micro-benchmark is stored under `benchmark/micro` and contains the
following:

* `packages`: Contains the source code of 4 packages. Specifically it contains
  the source code of an `example` package which depends on the
  `depstatic` and `depshared` packages. In turn, `depshard` depends on the
  `transdep` packages.
* `call-graphs`: Contains CScout generated call graphs for the aforementioned
  packages.
* `Dockefile`: A Dockerfile to build an image in order to produce the call
  graphs.

In order to execute the benchmark:

```
c-stitch benchmark/micro/callgraphs/* --output out.json
```

The `out.json` file should contain the following output:

```
{
    "edges": [
        [0, 1],
        [2, 3],
        [2, 4],
        [2, 5],
        [2, 0],
        [2, 6]
    ],
    "nodes": {
        "0": {
            "URI": "fasten://depshared$0.1-1/libdepshareda.so;C/dep_shared_fun_a()",
            "metadata": {}
        },
        "1": {
            "URI": "fasten://transdep$0.1-1/libtransdep.so;C/trans_dep_fun()",
            "metadata": {}
        },
        "2": {
            "URI": "fasten://example$0.1-1/hello;C/main()",
            "metadata": {}
        },
        "3": {
            "URI": "fasten://example$0.1-1/hello;C/local()",
            "metadata": {}
        },
        "4": {
            "URI": "fasten://depstatic$0.1-1/libdepstatic.a;C/dep_static_call_fun()",
            "metadata": {}
        },
        "5": {
            "URI": "fasten://depstatic$0.1-1/;%2Fusr%2Finclude/libdepstatic.h;dep_static_fun()",
            "metadata": {}
        },
        "6": {
            "URI": "fasten://depshared$0.1-1/libdepsharedb.so;C/dep_shared_fun_b()",
            "metadata": {}
        }
    }
}
```
