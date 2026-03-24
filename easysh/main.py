import importlib.metadata
import os
import shutil
import sys

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import FileHistory
except ImportError:
    print("error: prompt_toolkit is required. run: pip install prompt_toolkit")
    sys.exit(1)

from .commands import translate
from .completion import EasyshCompleter
from .config import is_first_run, show_onboarding
from .executor import execute
from .explain import explain
from .help import show_help
from .suggest import suggest
from .utils import confirm, format_path, git_branch, print_dim, print_green, print_info, print_red, success_message

_DESTRUCTIVE = ("rm ", "git checkout -- .", "git reset --hard")
_VALID_MODES = ("normal", "learn", "preview")


def is_destructive(cmd: str) -> bool:
    return any(cmd.startswith(d) for d in _DESTRUCTIVE)


def get_prompt() -> str:
    branch = git_branch()
    suffix = f" ({branch})" if branch else ""
    return f"easysh {format_path(os.getcwd())}{suffix} \u276f "


def main() -> None:
    if is_first_run():
        show_onboarding()

    session = PromptSession(
        history=FileHistory(os.path.expanduser("~/.easysh_history")),
        completer=EasyshCompleter(),
        complete_while_typing=True,
    )
    mode = "normal"
    prev_dir: str | None = None

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

        if user_input.lower() == "version":
            try:
                ver = importlib.metadata.version("easysh")
            except importlib.metadata.PackageNotFoundError:
                ver = "dev"
            print(f"easysh v{ver}")
            continue

        if user_input.lower() == "back":
            if prev_dir is None:
                print_red("no previous directory")
            else:
                target = prev_dir
                prev_dir = os.getcwd()
                os.chdir(target)
                print_green(f"\u2714 now in {format_path(target)}")
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

        if mode == "preview":
            print_dim("(preview — not executed)")
            continue

        if is_destructive(cmd):
            if not confirm("this may be destructive. continue? (y/n): "):
                continue

        cwd_before = os.getcwd()
        returncode = execute(cmd)

        if cmd.startswith("cd "):
            cwd_after = os.getcwd()
            if cwd_after != cwd_before:
                prev_dir = cwd_before
        elif returncode == 0:
            print_green(f"\u2714 {success_message(cmd)}")


if __name__ == "__main__":
    main()
