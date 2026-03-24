from typing import Optional

from . import filesystem, git, npm, system

_PASSTHROUGHS = frozenset(("git", "npm", "npx", "node", "python", "python3"))


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
