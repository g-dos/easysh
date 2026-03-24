import os
import subprocess

from .utils import print_blue, print_red


def execute(cmd: str) -> int:
    """Run cmd. Returns the exit code (0 = success, non-zero = failure)."""
    try:
        if cmd.startswith("cd "):
            path = cmd[3:].strip()
            os.chdir(os.path.expanduser(path))
            print_blue(f"\u2714 now in {os.getcwd()}")
            return 0
        result = subprocess.run(cmd, shell=True)
        return result.returncode
    except FileNotFoundError as e:
        print_red(f"not found: {e}")
        return 127
    except PermissionError as e:
        print_red(f"permission denied: {e}")
        return 1
    except Exception as e:
        print_red(f"error: {e}")
        return 1
