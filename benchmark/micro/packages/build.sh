#! /bin/bash

build_proj () {
    name=$1
    tar czf $name.tar.gz $name
    cd $name
    debmake
    cp ../helper/rules debian/rules
    if [[ "$name" == "depshared-0.1" ]]; then
        printf "\noverride_dh_dwz:\n" >> debian/rules
    fi
    sed -i s/unknown/devel/g debian/control
    sed -i 's/<insert the upstream URL, if relevant>/https:\/\/example.org/g' \
        debian/control
    if [[ "$name" == "depshared-0.1" ]]; then
        sed -i '/^Depends:/ s/$/, transdep/' debian/control
    elif [[ "$name" == "example-0.1" ]]; then
        sed -i '/^Build-Depends:/ s/$/, depstatic/' debian/control
        sed -i '/^Depends:/ s/$/, depshared/' debian/control
    fi
    cd ..
}

build_proj transdep-0.1
build_proj depshared-0.1
build_proj depstatic-0.1
build_proj example-0.1
