import os
from .utils import BUILTINS

_CACHE = None

def get_executables():
    global _CACHE
    if _CACHE:
        return _CACHE

    cmds = set(BUILTINS)
    for path in os.environ.get("PATH", "").split(os.pathsep):
        if os.path.isdir(path):
            try:
                for f in os.listdir(path):
                    if os.access(os.path.join(path, f), os.X_OK):
                        cmds.add(f)
            except:
                pass

    _CACHE = sorted(cmds)
    return _CACHE

def completer(text, state):
    options = [c for c in get_executables() if c.startswith(text)]
    try:
        options += [f for f in os.listdir(".") if f.startswith(text)]
    except:
        pass

    options = sorted(set(options))
    return options[state] + " " if state < len(options) else None
