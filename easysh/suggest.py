_ALL_HINTS = [
    # Filesystem
    "list", "list all", "open <dir>", "where",
    "create <name>", "delete <file>", "move <src> <dst>",
    "copy <src> <dst>", "rename <src> <dst>",
    "show <file>", "edit <file>", "find <name>",
    "search <pattern>", "count <file>", "size <path>",
    "compress <path>", "extract <file>",
    "touch <file>", "allow <file>", "link <src> <dst>",
    # System
    "disk", "memory", "ports", "processes", "ip",
    "uptime", "clear", "history", "whoami", "env",
    "run <cmd>", "kill <name>",
    # Git
    "status", "diff", "log", "save <message>",
    "push", "pull", "fetch", "branch",
    "new branch <name>", "switch <branch>", "merge <branch>",
    "stash", "pop", "undo", "discard",
    "clone <url>", "init", "remote", "tag <version>",
    # NPM
    "dev", "build", "start", "test", "lint",
    "install", "add <package>", "add dev <package>",
    "uninstall <package>", "packages", "scripts",
    "outdated", "audit",
]


def suggest(user_input: str) -> list[str]:
    """Return up to 3 relevant hints for a given input string."""
    word = user_input.strip().lower().split()[0] if user_input.strip() else ""

    if not word:
        return _ALL_HINTS[:3]

    # Strategy 1: hint starts with the full word
    matches = [h for h in _ALL_HINTS if h.startswith(word)]
    if matches:
        return matches[:3]

    # Strategy 2: first token of hint starts with same prefix (up to 3 chars)
    prefix = word[:min(3, len(word))]
    matches = [h for h in _ALL_HINTS if h.split()[0].startswith(prefix)]
    if matches:
        return matches[:3]

    # Strategy 3: word appears anywhere in hint
    matches = [h for h in _ALL_HINTS if word[:3] in h]
    if matches:
        return matches[:3]

    return _ALL_HINTS[:3]
