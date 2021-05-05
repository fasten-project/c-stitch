prefix = /usr/local
LIBS = -ltransdep

all: src/libdepshareda.so src/libdepsharedb.so

src/libdepshareda.so: src/depshareda.o
	$(CC) -shared -o $@ $^ $(LIBS)

src/libdepsharedb.so: src/depsharedb.o
	$(CC) -shared -o $@ $^

install: src/libdepshareda.so src/libdepsharedb.so
	install -D src/libdepshareda.so \
		$(DESTDIR)$(prefix)/lib/libdepshareda.so
	install -D src/libdepsharedb.so \
		$(DESTDIR)$(prefix)/lib/libdepsharedb.so
	install -D include/libdepshareda.h \
		$(DESTDIR)$(prefix)/include/libdepshareda.h
	install -D include/libdepsharedb.h \
		$(DESTDIR)$(prefix)/include/libdepsharedb.h

clean:
	-rm -f src/depshareda.o src/depsharedb.o src/libdepshareda.so \
		src/libdepsharedb.so

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib/libdepshareda.so
	-rm -f $(DESTDIR)$(prefix)/lib/libdepsharedb.so
	-rm -f $(DESTDIR)$(prefix)/include/libdepshareda.h
	-rm -f $(DESTDIR)$(prefix)/include/libdepsharedb.h

.PHONY: all install clean distclean uninstall
