prefix = /usr/local
LDFLAGS=
BIN=src/hello
OBJ=src/hello.o
LIBS=-ldepstatic -ldepshareda -ldepsharedb

all: $(BIN)

$(BIN): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS)

install: $(BIN)
	install -D $(BIN) \
		$(DESTDIR)$(prefix)/bin/hello

clean:
	-rm -f $(BIN)
	-rm -f $(OBJ)

distclean: clean

uninstall:
	-rm -f $(DESTDIR)$(prefix)/bin/hello

.PHONY: all install clean distclean uninstall
