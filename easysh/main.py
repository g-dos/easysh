import os
import shutil
import sys

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import InMemoryHistory
except ImportError:
    print("error: prompt_toolkit is required. run: pip install prompt_toolkit")
    sys.exit(1)

from .commands import translate
from .config import is_first_run, show_onboarding
from .executor import execute
from .explain import explain
from .help import show_help
from .suggest import suggest
from .utils import confirm, format_path, print_dim, print_green, print_info, print_red, success_message

_DESTRUCTIVE = ("rm ", "git checkout -- .", "git reset --hard")
_VALID_MODES = ("normal", "learn")


def is_destructive(cmd: str) -> bool:
    return any(cmd.startswith(d) for d in _DESTRUCTIVE)


def get_prompt() -> str:
    return f"easysh {format_path(os.getcwd())} \u276f "


def main() -> None:
    if is_first_run():
        show_onboarding()

    session = PromptSession(history=InMemoryHistory())
    mode = "normal"

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

        if user_input.lower() == "help":
            show_help()
            continue

        # Mode switching — handled before translation
        if user_input.lower().startswith("mode "):
            requested = user_input.split(None, 1)[1].lower()
            if requested in _VALID_MODES:
                mode = requested
                print_green(f"\u2714 {mode} mode enabled")
            else:
                print_red(f"unknown mode '{requested}' — valid: {', '.join(_VALID_MODES)}")
            continue

        translated = translate(user_input)

        # Show clean error for bad usage (missing args, etc.)
        if translated and translated.startswith("__error__:"):
            print_red(translated[len("__error__:"):].strip())
            continue

        cmd = translated if translated is not None else user_input

        # Show suggestions before running if the command won't be found in PATH.
        # Uses shutil.which so real tools (docker, make, python…) are never interrupted.
        if translated is None:
            first_word = user_input.strip().split()[0]
            if shutil.which(first_word) is None:
                hints = suggest(user_input)
                print_dim("did you mean:")
                for h in hints:
                    print_dim(f"  {h}")
                print()

        print_green(f"\u2192 {cmd}")

        if mode == "learn":
            for desc in explain(cmd):
                print_info(desc)

        if is_destructive(cmd):
            if not confirm("this may be destructive. continue? (y/n): "):
                continue

        returncode = execute(cmd)

        if returncode == 0 and not cmd.startswith("cd "):
            print_green(f"\u2714 {success_message(cmd)}")


if __name__ == "__main__":
    main()
