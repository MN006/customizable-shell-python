import os
import sys
from .builtins import run_builtin
from .utils import BUILTINS

def run_pipeline(stages):
    prev_read = None
    pids = []

    for i, args in enumerate(stages):
        is_last = i == len(stages) - 1
        r, w = (None, None) if is_last else os.pipe()

        pid = os.fork()
        if pid == 0:
            if prev_read is not None:
                os.dup2(prev_read, 0)

            if not is_last:
                os.close(r)
                os.dup2(w, 1)

            if args[0] in BUILTINS:
                run_builtin(args, sys.stdout, sys.stderr)
                sys.exit(0)

            os.execvp(args[0], args)

        if prev_read:
            os.close(prev_read)
        if not is_last:
            os.close(w)
            prev_read = r

        pids.append(pid)

    for pid in pids:
        os.waitpid(pid, 0)
