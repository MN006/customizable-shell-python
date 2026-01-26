import os
import getpass
import platform

ESC = "\x1b"
CLR = f"{ESC}[0m"
GRN = f"{ESC}[0;32m"
BLU = f"{ESC}[0;34m"

def build_prompt():
    user = getpass.getuser()
    host = platform.node().split(".")[0]
    cwd = os.getcwd().replace(os.path.expanduser("~"), "~")

    return (
        f"\n[{GRN}{user}@{host}{CLR} {BLU}{cwd}{CLR}]\n"
        f"{BLU}{user}{CLR} ▶ "
    )
