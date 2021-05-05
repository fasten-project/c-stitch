#! /bin/bash

install_proj () {
    name=$1
    cd ${name}-0.1
    debuild
    cd ..
    sudo dpkg --install ${name}_0.1-1_amd64.deb
}

install_proj transdep
install_proj depshared
install_proj depstatic
install_proj example
