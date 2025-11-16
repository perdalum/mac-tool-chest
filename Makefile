INSTALL_DIR := $(HOME)/Documents/dotfiles/bin
INSTALL_PATH := $(INSTALL_DIR)/FileOpen

.DEFAULT_GOAL := no-target

no-target:
	@echo "Error: no build target specified. Use 'make install'." >&2
	@exit 1

install:
	@test -d "$(INSTALL_DIR)" || { echo "Directory $(INSTALL_DIR) does not exist" >&2; exit 1; }
	cp -p FileOpen.py "$(INSTALL_PATH)"
	chmod +x "$(INSTALL_PATH)"
