prefix = /usr/local

all: src/libtransdep.so

src/libtransdep.so: src/trans_dep.o
	$(CC) -shared -o $@ $^

install: src/libtransdep.so
	install -D src/libtransdep.so \
		$(DESTDIR)$(prefix)/lib/libtransdep.so
	install -D include/libtransdep.h \
		$(DESTDIR)$(prefix)/include/libtransdep.h

clean:
	-rm -f src/trans_dep.o src/libtransdep.so

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib/libtransdep.so
	-rm -f $(DESTDIR)$(prefix)/include/libtransdep.h

.PHONY: all install clean distclean uninstall
