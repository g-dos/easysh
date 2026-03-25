import os


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


def confirm(prompt: str) -> bool:
    try:
        answer = input(prompt).strip().lower()
        return answer == "y"
    except (EOFError, KeyboardInterrupt):
        return False
