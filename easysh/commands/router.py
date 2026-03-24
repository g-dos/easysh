from typing import Optional

from . import filesystem, git, npm, system

_PASSTHROUGHS = frozenset(("git", "npm", "npx", "node", "python", "python3"))

# Shown as hints when a command isn't recognized
_HINTS = [
    "list", "list all", "create <name>", "open <dir>",
    "show <file>", "find <name>", "search <pattern>",
    "status", "save <message>", "push", "pull", "log",
    "dev", "build", "install", "add <package>",
    "disk", "ports", "processes", "clear",
]


def translate(input_str: str) -> Optional[str]:
    text = input_str.strip()
    lower = text.lower()
    tokens = lower.split()
    raw = text.split()

    if not tokens:
        return None

    if tokens[0] in _PASSTHROUGHS:
        return None

    return (
        filesystem.translate(tokens, raw, lower)
        or system.translate(tokens, raw, lower)
        or git.translate(tokens, raw, lower)
        or npm.translate(tokens, raw, lower)
    )


def suggest(input_str: str) -> list[str]:
    """Return up to 3 hints relevant to the user's input."""
    word = input_str.strip().lower().split()[0] if input_str.strip() else ""
    if len(word) >= 2:
        matches = [h for h in _HINTS if h.startswith(word[:2])]
        if matches:
            return matches[:3]
    return _HINTS[:3]
