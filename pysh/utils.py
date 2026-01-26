import os
import shutil

BUILTINS = [
    "exit",
    "cd",
    "pwd",
    "echo",
    "type",
    "history",
    "fetch",
]

def which(cmd):
    return shutil.which(cmd)

def expand_path(path):
    return os.path.expanduser(path)
