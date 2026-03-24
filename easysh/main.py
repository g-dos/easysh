import os
import sys

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import InMemoryHistory
except ImportError:
    print("error: prompt_toolkit is required. run: pip install prompt_toolkit")
    sys.exit(1)

from .commands import translate
from .executor import execute
from .utils import confirm, format_path, print_green, print_red

DESTRUCTIVE_PREFIXES = ("rm ",)


def is_destructive(cmd: str) -> bool:
    return any(cmd.startswith(prefix) for prefix in DESTRUCTIVE_PREFIXES)


def get_prompt() -> str:
    cwd = format_path(os.getcwd())
    return f"easysh {cwd} ❯ "


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

        # Handle translation errors (missing args, etc.)
        if translated and translated.startswith("__error__:"):
            print_red(translated[len("__error__:"):].strip())
            continue

        cmd = translated if translated is not None else user_input

        print_green(f"→ {cmd}")

        if is_destructive(cmd):
            if not confirm("this may be destructive. continue? (y/n): "):
                continue

        execute(cmd)


if __name__ == "__main__":
    main()
