INSTALL_DIR ?= $(HOME)/Documents/dotfiles/bin

# List of source files *with* extensions
# You can override this on the command line:
#   make install TOOLS="FileOpen.py foo.sh bar.jl"
TOOLS ?= FileOpen.py \
		 ascii-barchart.sh \
		 PlayDirectory \
		 PlayPlaylist \
		 PlayExtractPlaylist

# Default when no target is given (BSD make style)
.MAIN: no-target

no-target:
	@echo "Error: no build target specified. Use 'make install'." >&2
	@exit 1

install:
	@test -d "$(INSTALL_DIR)" || { echo "Directory $(INSTALL_DIR) does not exist" >&2; exit 1; }
	@for src in $(TOOLS); do \
		base=$${src##*/};      \
		base=$${base%.*};      \
		dest="$(INSTALL_DIR)/$${base}"; \
		echo "Installing $$src -> $$dest"; \
		cp -p "$$src" "$$dest"; \
		chmod +x "$$dest";     \
	done