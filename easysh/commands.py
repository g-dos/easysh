from typing import Optional


def translate(input_str: str) -> Optional[str]:
    text = input_str.strip()
    lower = text.lower()
    tokens = lower.split()
    # Original tokens preserving case (for filenames, messages, URLs)
    raw_tokens = text.split()

    if not tokens:
        return None

    # Native passthrough — git/npm commands run as-is
    if tokens[0] in ("git", "npm", "npx", "node", "python", "python3"):
        return None

    # ── Filesystem ────────────────────────────────────────────────────────────

    if lower == "list":
        return "ls"

    if lower in ("list all", "list -a", "la"):
        return "ls -la"

    if lower == "where":
        return "pwd"

    if tokens[0] == "open":
        if len(tokens) < 2:
            return "__error__: open requires a directory argument"
        return f"cd {raw_tokens[1]}"

    if tokens[0] == "create":
        if len(tokens) < 2:
            return "__error__: create requires a name argument"
        return f"mkdir -p {raw_tokens[1]}"

    if tokens[0] in ("delete", "remove"):
        if len(tokens) < 2:
            return f"__error__: {tokens[0]} requires a file argument"
        return f"rm {raw_tokens[1]}"

    if tokens[0] == "delete all":
        if len(tokens) < 2:
            return "__error__: delete all requires a path"
        return f"rm -rf {raw_tokens[2]}"

    if tokens[0] == "move" or tokens[0] == "rename":
        if len(tokens) < 3:
            return "__error__: move requires source and destination"
        return f"mv {raw_tokens[1]} {raw_tokens[2]}"

    if tokens[0] == "copy":
        if len(tokens) < 3:
            return "__error__: copy requires source and destination"
        return f"cp -r {raw_tokens[1]} {raw_tokens[2]}"

    if tokens[0] in ("show", "read", "cat"):
        if len(tokens) < 2:
            return "__error__: show requires a filename"
        return f"cat {raw_tokens[1]}"

    if tokens[0] == "find":
        if len(tokens) < 2:
            return "__error__: find requires a name"
        return f'find . -name "{raw_tokens[1]}"'

    if tokens[0] == "search":
        if len(tokens) < 2:
            return "__error__: search requires a pattern"
        # search X in Y
        if len(tokens) >= 4 and tokens[-2] == "in":
            pattern = " ".join(raw_tokens[1:-2])
            directory = raw_tokens[-1]
            return f'grep -r "{pattern}" {directory}'
        pattern = " ".join(raw_tokens[1:])
        return f'grep -r "{pattern}" .'

    if tokens[0] == "count":
        if len(tokens) < 2:
            return "__error__: count requires a filename"
        return f"wc -l {raw_tokens[1]}"

    if tokens[0] == "size":
        if len(tokens) < 2:
            return "__error__: size requires a path"
        return f"du -sh {raw_tokens[1]}"

    if tokens[0] == "edit":
        if len(tokens) < 2:
            return "__error__: edit requires a filename"
        return f"nano {raw_tokens[1]}"

    if tokens[0] == "touch":
        if len(tokens) < 2:
            return "__error__: touch requires a filename"
        return f"touch {raw_tokens[1]}"

    if tokens[0] == "allow":
        if len(tokens) < 2:
            return "__error__: allow requires a filename"
        return f"chmod +x {raw_tokens[1]}"

    if tokens[0] == "link":
        if len(tokens) < 3:
            return "__error__: link requires source and destination"
        return f"ln -s {raw_tokens[1]} {raw_tokens[2]}"

    if tokens[0] == "compress":
        if len(tokens) < 2:
            return "__error__: compress requires a path"
        name = raw_tokens[1]
        return f"tar -czf {name}.tar.gz {name}"

    if tokens[0] == "extract":
        if len(tokens) < 2:
            return "__error__: extract requires a filename"
        f = raw_tokens[1]
        if f.endswith(".zip"):
            return f"unzip {f}"
        return f"tar -xzf {f}"

    # ── System ────────────────────────────────────────────────────────────────

    if lower == "clear":
        return "clear"

    if lower == "history":
        return "history"

    if lower == "disk":
        return "df -h"

    if lower == "memory":
        return "vm_stat"

    if lower in ("processes", "ps"):
        return "ps aux"

    if lower == "ports":
        return "lsof -iTCP -sTCP:LISTEN -P -n"

    if lower == "ip":
        return "curl -s ifconfig.me"

    if lower == "uptime":
        return "uptime"

    if lower == "whoami":
        return "whoami"

    if lower == "env":
        return "env"

    # ── Process ───────────────────────────────────────────────────────────────

    if tokens[0] == "run":
        if len(tokens) < 2:
            return "__error__: run requires a command argument"
        return " ".join(raw_tokens[1:])

    if tokens[0] == "kill":
        if len(tokens) < 2:
            return "__error__: kill requires a process name"
        return f"pkill -f {raw_tokens[1]}"

    # ── Git ───────────────────────────────────────────────────────────────────

    if lower == "status":
        return "git status"

    if lower == "diff":
        return "git diff"

    if lower == "push":
        return "git push"

    if lower == "pull":
        return "git pull"

    if lower == "fetch":
        return "git fetch"

    if lower == "log":
        return "git log --oneline -10"

    if lower in ("branch", "branches"):
        return "git branch"

    if lower == "remote":
        return "git remote -v"

    if lower == "stash":
        return "git stash"

    if lower == "pop":
        return "git stash pop"

    if lower == "undo":
        return "git reset HEAD~1 --soft"

    if lower == "discard":
        return "git checkout -- ."

    if lower == "init":
        return "git init"

    if tokens[0] == "save":
        msg = " ".join(raw_tokens[1:]).strip("\"'") if len(tokens) > 1 else "update"
        return f'git add -A && git commit -m "{msg}"'

    if tokens[0] == "clone":
        if len(tokens) < 2:
            return "__error__: clone requires a URL"
        return f"git clone {raw_tokens[1]}"

    if tokens[:2] == ["new", "branch"]:
        if len(tokens) < 3:
            return "__error__: new branch requires a name"
        return f"git checkout -b {raw_tokens[2]}"

    if tokens[0] == "switch":
        if len(tokens) < 2:
            return "__error__: switch requires a branch name"
        return f"git checkout {raw_tokens[1]}"

    if tokens[0] == "merge":
        if len(tokens) < 2:
            return "__error__: merge requires a branch name"
        return f"git merge {raw_tokens[1]}"

    if tokens[0] == "tag":
        if len(tokens) < 2:
            return "__error__: tag requires a version"
        return f"git tag {raw_tokens[1]}"

    # ── NPM ───────────────────────────────────────────────────────────────────

    if lower == "dev":
        return "npm run dev"

    if lower == "build":
        return "npm run build"

    if lower == "start":
        return "npm start"

    if lower in ("test", "tests"):
        return "npm test"

    if lower == "lint":
        return "npm run lint"

    if lower == "install":
        return "npm install"

    if lower == "outdated":
        return "npm outdated"

    if lower == "audit":
        return "npm audit"

    if tokens[0] == "add":
        if len(tokens) < 2:
            return "__error__: add requires a package name"
        if len(tokens) >= 3 and tokens[1] == "dev":
            return f"npm install -D {raw_tokens[2]}"
        return f"npm install {raw_tokens[1]}"

    if tokens[0] == "uninstall":
        if len(tokens) < 2:
            return "__error__: uninstall requires a package name"
        return f"npm uninstall {raw_tokens[1]}"

    if lower == "packages":
        return "npm list --depth=0"

    if lower == "scripts":
        return "npm run"

    # No rule matched — fallback to native shell
    return None
