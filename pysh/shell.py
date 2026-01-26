import shlex
import subprocess
import sys
import os

from .prompt import build_prompt
from .history import init_history, add_history
from .completion import completer
from .pipeline import run_pipeline
from .builtins import run_builtin
from .utils import BUILTINS, which

def main():
    init_history()

    try:
        import readline
        readline.set_completer(completer)
        readline.parse_and_bind("tab: complete")
    except:
        pass

    while True:
        try:
            line = input(build_prompt()).strip()
            if not line:
                continue

            add_history(line)

            if "|" in line:
                if os.name == "nt":
                    print("pipelines are not supported on Windows")
                    continue
                stages = [shlex.split(p) for p in line.split("|")]
                run_pipeline(stages)
                continue

            args = shlex.split(line)

            if args[0] == "exit":
                break

            if args[0] in BUILTINS:
                run_builtin(args, sys.stdout, sys.stderr)
            else:
                if which(args[0]):
                    subprocess.run(args)
                else:
                    print(f"{args[0]}: command not found")

        except (EOFError, KeyboardInterrupt):
            print()
            break

if __name__ == "__main__":
    main()
