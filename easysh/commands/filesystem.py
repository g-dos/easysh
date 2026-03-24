from typing import Optional


def translate(tokens: list, raw: list, lower: str) -> Optional[str]:
    if lower == "list":
        return "ls"

    if lower in ("list all", "list -a", "la"):
        return "ls -la"

    if lower == "where":
        return "pwd"

    if tokens[0] == "open":
        if len(tokens) < 2:
            return "__error__: missing directory — usage: open <dir>"
        return f"cd {raw[1]}"

    if tokens[0] == "create":
        if len(tokens) < 2:
            return "__error__: missing name — usage: create <name>"
        return f"mkdir -p {raw[1]}"

    if tokens[0] in ("delete", "remove"):
        if len(tokens) < 2:
            return f"__error__: missing file — usage: {tokens[0]} <file>"
        return f"rm {raw[1]}"

    if tokens[:2] == ["delete", "all"]:
        if len(tokens) < 3:
            return "__error__: missing path — usage: delete all <path>"
        return f"rm -rf {raw[2]}"

    if tokens[0] in ("move", "rename"):
        if len(tokens) < 3:
            return "__error__: missing arguments — usage: move <src> <dst>"
        return f"mv {raw[1]} {raw[2]}"

    if tokens[0] == "copy":
        if len(tokens) < 3:
            return "__error__: missing arguments — usage: copy <src> <dst>"
        return f"cp -r {raw[1]} {raw[2]}"

    if tokens[0] in ("show", "read", "cat"):
        if len(tokens) < 2:
            return "__error__: missing filename — usage: show <file>"
        return f"cat {raw[1]}"

    if tokens[0] == "find":
        if len(tokens) < 2:
            return "__error__: missing name — usage: find <name>"
        return f'find . -name "{raw[1]}"'

    if tokens[0] == "search":
        if len(tokens) < 2:
            return "__error__: missing pattern — usage: search <pattern>"
        if len(tokens) >= 4 and tokens[-2] == "in":
            pattern = " ".join(raw[1:-2])
            return f'grep -r "{pattern}" {raw[-1]}'
        return f'grep -r "{" ".join(raw[1:])}" .'

    if tokens[0] == "count":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: count <file>"
        return f"wc -l {raw[1]}"

    if tokens[0] == "size":
        if len(tokens) < 2:
            return "__error__: missing path — usage: size <path>"
        return f"du -sh {raw[1]}"

    if tokens[0] == "edit":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: edit <file>"
        return f"nano {raw[1]}"

    if tokens[0] == "touch":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: touch <file>"
        return f"touch {raw[1]}"

    if tokens[0] == "allow":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: allow <file>"
        return f"chmod +x {raw[1]}"

    if tokens[0] == "link":
        if len(tokens) < 3:
            return "__error__: missing arguments — usage: link <src> <dst>"
        return f"ln -s {raw[1]} {raw[2]}"

    if tokens[0] == "compress":
        if len(tokens) < 2:
            return "__error__: missing path — usage: compress <path>"
        name = raw[1]
        return f"tar -czf {name}.tar.gz {name}"

    if tokens[0] == "extract":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: extract <file>"
        f = raw[1]
        return f"unzip {f}" if f.endswith(".zip") else f"tar -xzf {f}"

    if lower == "newest":
        return "ls -t | head -1"

    if lower == "biggest":
        return "du -sh * | sort -rh | head -5"

    if tokens[0] == "empty":
        if len(tokens) < 2:
            return "__error__: missing directory — usage: empty <dir>"
        d = raw[1]
        return f"mkdir -p {d} && touch {d}/.gitkeep"

    if lower == "tree":
        return "find . -maxdepth 2 | sort"

    if lower == "hidden":
        return 'ls -la | grep "^\\."'

    if tokens[0] == "permissions":
        if len(tokens) < 2:
            return "__error__: missing filename — usage: permissions <file>"
        return f"ls -la {raw[1]}"

    return None
