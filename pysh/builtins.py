import os
import shutil
import platform
from .utils import BUILTINS
from .history import get_readline

ASCII_LOGO = r"""
┏┓         
┃ ┓┏┏╋┏┓┏┳┓
┗┛┗┻┛┗┗┛┛┗┗
"""

def run_builtin(args, out, err):
    cmd = args[0]
    rl = get_readline()

    if cmd == "cd":
        path = args[1] if len(args) > 1 else os.path.expanduser("~")
        try:
            os.chdir(os.path.expanduser(path))
        except:
            err.write(f"cd: {path}: No such directory\n")

    elif cmd == "pwd":
        out.write(os.getcwd() + "\n")

    elif cmd == "echo":
        out.write(" ".join(args[1:]) + "\n")

    elif cmd == "type":
        if len(args) < 2:
            err.write("type: missing argument\n")
            return

        name = args[1]
        if name in BUILTINS:
            out.write(f"{name} is a shell builtin\n")
        elif shutil.which(name):
            out.write(f"{name} is {shutil.which(name)}\n")
        else:
            out.write(f"{name}: not found\n")

    elif cmd == "history":
        if not rl:
            err.write("history: not supported\n")
            return

        for i in range(1, rl.get_current_history_length() + 1):
            item = rl.get_history_item(i)
            if item:
                out.write(f"{i:5} {item}\n")

    elif cmd == "fetch":
        info = [
            f"OS:    {platform.system()} {platform.release()}",
            f"Host:  {platform.node()}",
            f"Shell: pysh",
            f"User:  {os.getenv('USER','N/A')}",
        ]

        logo = ASCII_LOGO.strip().splitlines()
        for i in range(max(len(logo), len(info))):
            l = logo[i] if i < len(logo) else ""
            r = info[i] if i < len(info) else ""
            out.write(f"{l:<12} {r}\n")
