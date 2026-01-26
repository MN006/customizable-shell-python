# pysh

A minimal Unix-like shell implemented in Python.

`pysh` provides an interactive command-line environment with built-in commands,
command history, tab completion, colored prompt, and external command execution.
It is designed with a clean internal architecture and clear separation of
concerns.

---

## Features

- Interactive shell with colored prompt
- Built-in commands:
  - `cd`, `pwd`, `echo`, `type`, `history`, `fetch`, `exit`
- Persistent command history
- Tab completion for commands and files
- External command execution via system `PATH`
- Modular, extensible codebase

---

## Requirements

- Python 3.9+
- Unix-like system for pipeline support  
  (Windows is supported **without pipelines**)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/pyshell.git
cd pyshell

##Usage
```bash
python -m pysh.shell
