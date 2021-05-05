prefix = /usr/local

all: src/libdepstatic.a

src/libdepstatic.a: src/depstatic.o
	ar rcs $@ $^

install: src/libdepstatic.a
	install -D src/libdepstatic.a \
		$(DESTDIR)$(prefix)/lib/libdepstatic.a
	install -D include/libdepstatic.h \
		$(DESTDIR)$(prefix)/include/libdepstatic.h

clean:
	-rm -f src/depstatic.o src/libdepstatic.a

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/lib/libdepstatic.a
	-rm -f $(DESTDIR)$(prefix)/include/libdepstatic.h

.PHONY: all install clean distclean uninstall
