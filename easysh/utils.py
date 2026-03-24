import os
import subprocess


def git_branch() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=0.5
        )
        branch = result.stdout.strip()
        return branch if result.returncode == 0 and branch != "HEAD" else None
    except Exception:
        return None


def format_path(path: str) -> str:
    home = os.path.expanduser("~")
    if path.startswith(home):
        return "~" + path[len(home):]
    return path


def print_green(text: str) -> None:
    print(f"\033[32m{text}\033[0m")


def print_blue(text: str) -> None:
    print(f"\033[34m{text}\033[0m")


def print_red(text: str) -> None:
    print(f"\033[31m\u2716 {text}\033[0m")


def print_dim(text: str) -> None:
    print(f"\033[2m{text}\033[0m")


def print_info(text: str) -> None:
    print(f"\033[2m\u2139 {text}\033[0m")


# Longest-prefix-first so specific entries match before generic ones
_SUCCESS_PREFIXES: list[tuple[str, str]] = [
    ("git add -A && git commit", "committed"),
    ("git checkout -b",          "branch created"),
    ("git checkout -- .",        "discarded"),
    ("git checkout",             "switched"),
    ("git stash pop",            "restored"),
    ("git stash",                "stashed"),
    ("git push",                 "pushed"),
    ("git pull",                 "pulled"),
    ("git clone",                "cloned"),
    ("git init",                 "initialized"),
    ("git merge",                "merged"),
    ("git tag",                  "tagged"),
    ("mkdir",                    "created"),
    ("touch",                    "created"),
    ("mv",                       "moved"),
    ("cp",                       "copied"),
    ("rm",                       "deleted"),
    ("npm install",              "installed"),
    ("npm uninstall",            "removed"),
    ("chmod +x",                 "allowed"),
    ("ln -s",                    "linked"),
]


def success_message(cmd: str) -> str:
    for prefix, msg in _SUCCESS_PREFIXES:
        if cmd.startswith(prefix):
            return msg
    return "done"


def confirm(prompt: str) -> bool:
    try:
        answer = input(prompt).strip().lower()
        return answer == "y"
    except (EOFError, KeyboardInterrupt):
        return False
