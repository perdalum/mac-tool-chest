# Mac Tool Chest

# Mac Tool Chest

This repository is for automation and quick scripting on macOS. The advent of LLMs has finally, after 40 years of creating tools and then forgetting about them, motivated me to create a tool chest—this repository! 😃

I'm still the creative and executive boss, but I now have several quite capable assistants—and they are much better than me at remembering libraries, function calls, parameters, etc., and they don't get bored...

So, everything here is written for me with a focus on what I need. If you can use it, enjoy!


## FileOpen.py

A macOS command-line utility that searches for files and folders by name using the Spotlight index and opens them with a single command.

### Description

FileOpen.py leverages macOS Spotlight's `mdfind` command to quickly locate files or folders by name and opens them using the system's default application. When multiple matches are found, it presents an interactive menu to choose which item to open.

### Requirements

- **macOS only** (requires `mdfind` and `open` commands)
- Python 3.10 or higher (uses match-case syntax)
- No external dependencies required

### Installation

1. Define a path to a directory in your `$PATH` in the Makefile, e.g., `INSTALL_DIR := $(HOME)/.local/bin`

2. Install the script using `make install`

### Usage

The tool takes two options: `-t` (type) and `-h` (help). If no type is specified, the tool will search for files and folders.

     >: FileOpen
    usage: FileOpen [-h] [-t {file,folder}] filename
    FileOpen: error: the following arguments are required: filename

This is what it looks like when multiple matches are found:

     >: FileOpen wierd-file-name      
    Found 3 matches:
    (1) /Users/au15929/test-bed/wierd-file-name.txt
    (2) /Users/au15929/test-bed/wierd-file-name-2.txt
    (3) /Users/au15929/test-bed/wierd-file-name-3456.txt
    Enter number to open (or q to quit): 
