#include <libdepstatic.h>
#include <libdepshareda.h>
#include <libdepsharedb.h>

void local() {}

int main() {
    local();
    dep_static_fun(4);
    int a = dep_static_call_fun();
    int b = dep_shared_fun_a();
    int c = dep_shared_fun_b();
    return 0;
}
