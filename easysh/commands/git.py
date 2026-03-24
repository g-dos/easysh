from typing import Optional

_EXACT: dict[str, str] = {
    "status":   "git status",
    "diff":     "git diff",
    "push":     "git push",
    "pull":     "git pull",
    "fetch":    "git fetch",
    "log":      "git log --oneline -10",
    "branch":   "git branch",
    "branches": "git branch",
    "remote":   "git remote -v",
    "stash":    "git stash",
    "pop":      "git stash pop",
    "undo":     "git reset HEAD~1 --soft",
    "discard":  "git checkout -- .",
    "init":     "git init",
}


def translate(tokens: list, raw: list, lower: str) -> Optional[str]:
    if lower in _EXACT:
        return _EXACT[lower]

    if tokens[0] == "save":
        msg = " ".join(raw[1:]).strip("\"'") if len(tokens) > 1 else "update"
        return f'git add -A && git commit -m "{msg}"'

    if tokens[0] == "clone":
        if len(tokens) < 2:
            return "__error__: missing URL — usage: clone <url>"
        return f"git clone {raw[1]}"

    if tokens[:2] == ["new", "branch"]:
        if len(tokens) < 3:
            return "__error__: missing name — usage: new branch <name>"
        return f"git checkout -b {raw[2]}"

    if tokens[0] == "switch":
        if len(tokens) < 2:
            return "__error__: missing branch — usage: switch <branch>"
        return f"git checkout {raw[1]}"

    if tokens[0] == "merge":
        if len(tokens) < 2:
            return "__error__: missing branch — usage: merge <branch>"
        return f"git merge {raw[1]}"

    if tokens[0] == "tag":
        if len(tokens) < 2:
            return "__error__: missing version — usage: tag <version>"
        return f"git tag {raw[1]}"

    return None
