#include <libtransdep.h>

int dep_shared_fun_a() {
    int a = trans_dep_fun();
    return a;
}
