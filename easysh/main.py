import os
import sys

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import InMemoryHistory
except ImportError:
    print("error: prompt_toolkit is required. run: pip install prompt_toolkit")
    sys.exit(1)

from .commands import suggest, translate
from .executor import execute
from .utils import confirm, format_path, print_dim, print_green, print_red

_DESTRUCTIVE = ("rm ", "git checkout -- .", "git reset --hard")


def is_destructive(cmd: str) -> bool:
    return any(cmd.startswith(d) for d in _DESTRUCTIVE)


def get_prompt() -> str:
    return f"easysh {format_path(os.getcwd())} \u276f "


def main() -> None:
    session = PromptSession(history=InMemoryHistory())

    while True:
        try:
            raw = session.prompt(get_prompt())
        except EOFError:
            print("bye.")
            break
        except KeyboardInterrupt:
            print()
            continue

        user_input = raw.strip()

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("bye.")
            break

        translated = translate(user_input)

        # Show clean error for bad usage (missing args, etc.)
        if translated and translated.startswith("__error__:"):
            print_red(translated[len("__error__:"):].strip())
            continue

        cmd = translated if translated is not None else user_input

        print_green(f"\u2192 {cmd}")

        if is_destructive(cmd):
            if not confirm("this may be destructive. continue? (y/n): "):
                continue

        returncode = execute(cmd)

        # Show suggestions only when the command wasn't recognized by easysh
        # and the native shell also failed to find it (exit 127 = not found)
        if translated is None and returncode == 127:
            hints = suggest(user_input)
            print_dim("\ndid you mean:")
            for h in hints:
                print_dim(f"  {h}")


if __name__ == "__main__":
    main()
