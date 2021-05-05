all:
	@echo "Makefile needs your attention"

clean:
	$(MAKE) -C example-0.1 clean
	$(MAKE) -C depshared-0.1 clean
	$(MAKE) -C depstatic-0.1 clean
	$(MAKE) -C transdep-0.1 clean
	rm -rf *.build *.buildinfo *.changes *.deb *.debian.tar.xz *dbgsym*

clean_all: clean
	rm -rf *.tar.gz */debian *.dsc

clean_uninstall: clean_all
	dpkg --remove example
	dpkg --remove depstatic
	dpkg --remove depshared
	dpkg --remove transdep
