from typing import Optional


def translate(input_str: str) -> Optional[str]:
    text = input_str.strip()
    lower = text.lower()
    tokens = lower.split()

    if not tokens:
        return None

    # Git passthrough
    if tokens[0] == "git":
        return None

    # NPM passthrough
    if tokens[0] == "npm":
        return None

    # Filesystem commands
    if lower == "list":
        return "ls"

    if lower == "list all":
        return "ls -la"

    if lower == "where":
        return "pwd"

    if tokens[0] == "open":
        if len(tokens) < 2:
            return "__error__: open requires a directory argument"
        return f"cd {tokens[1]}"

    if tokens[0] == "create":
        if len(tokens) < 2:
            return "__error__: create requires a name argument"
        return f"mkdir {tokens[1]}"

    if tokens[0] == "delete":
        if len(tokens) < 2:
            return "__error__: delete requires a file argument"
        return f"rm {tokens[1]}"

    if tokens[0] == "move":
        if len(tokens) < 3:
            return "__error__: move requires two arguments (source destination)"
        return f"mv {tokens[1]} {tokens[2]}"

    if tokens[0] == "copy":
        if len(tokens) < 3:
            return "__error__: copy requires two arguments (source destination)"
        return f"cp {tokens[1]} {tokens[2]}"

    # Process commands
    if tokens[0] == "run":
        if len(tokens) < 2:
            return "__error__: run requires a command argument"
        return " ".join(tokens[1:])

    if tokens[0] == "kill":
        if len(tokens) < 2:
            return "__error__: kill requires a process name"
        return f"pkill -f {tokens[1]}"

    # No rule matched
    return None
