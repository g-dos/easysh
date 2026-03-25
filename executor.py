import os
import subprocess

from utils import print_blue, print_red


def execute(cmd: str) -> None:
    try:
        if cmd.startswith("cd "):
            path = cmd[3:].strip()
            expanded = os.path.expanduser(path)
            os.chdir(expanded)
            print_blue(f"now in {os.getcwd()}")
        else:
            subprocess.run(cmd, shell=True)
    except FileNotFoundError as e:
        print_red(f"error: {e}")
    except PermissionError as e:
        print_red(f"permission denied: {e}")
    except Exception as e:
        print_red(f"error: {e}")
