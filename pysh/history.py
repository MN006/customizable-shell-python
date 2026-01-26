import os
import atexit

try:
    import readline
except ImportError:
    try:
        from pyreadline3 import Readline
        readline = Readline()
    except ImportError:
        readline = None

HISTORY_FILE = os.path.join(
    os.path.expanduser("~"),
    ".pysh_history"
)

def init_history():
    if not readline:
        return

    if os.path.exists(HISTORY_FILE):
        readline.read_history_file(HISTORY_FILE)

    readline.set_history_length(1000)
    atexit.register(readline.write_history_file, HISTORY_FILE)

def add_history(cmd):
    if readline:
        readline.add_history(cmd)

def get_readline():
    return readline
