FROM docker.pkg.github.com/fasten-project/debian-builder/sbuild-cscout:1.0.1

RUN sudo apt update -yqq && sudo apt upgrade -yqq
RUN sudo apt install -yqq debmake

RUN mkdir -p /home/builder/micro
COPY ./transdep-0.1 /home/builder/micro/transdep-0.1
COPY ./depshared-0.1 /home/builder/micro/depshared-0.1
COPY ./depstatic-0.1 /home/builder/micro/depstatic-0.1
COPY ./example-0.1 /home/builder/micro/example-0.1
COPY ./build.sh /home/builder/micro/build.sh
COPY ./install.sh /home/builder/micro/install.sh
COPY ./Makefile /home/builder/micro/Makefile
COPY ./helper /home/builder/micro/helper
COPY ./helper/sbuildrc /home/builder/.sbuildrc
WORKDIR /home/builder/micro
RUN sudo ./build.sh && sudo ./install.sh
RUN sudo mkdir -p /results/deps
RUN sudo cp /home/builder/micro/*.deb /results/deps
