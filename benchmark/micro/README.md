Micro Benchmark
===============

```bash
docker build -t bench .
```

```bash
docker run -it --rm --privileged -v $(pwd)/callgraphs:/callgraphs \
    bench sbuild --apt-update --no-apt-upgrade \
    --no-apt-distupgrade --batch --stats-dir=/var/log/sbuild/stats \
    --dist=buster --arch=amd64 example_0.1-1.dsc
```
