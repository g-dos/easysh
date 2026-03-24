from typing import Optional

_EXACT: dict[str, str] = {
    "dev":       "npm run dev",
    "build":     "npm run build",
    "start":     "npm start",
    "test":      "npm test",
    "tests":     "npm test",
    "lint":      "npm run lint",
    "install":   "npm install",
    "outdated":  "npm outdated",
    "audit":     "npm audit",
    "packages":  "npm list --depth=0",
    "scripts":   "npm run",
}


def translate(tokens: list, raw: list, lower: str) -> Optional[str]:
    if lower in _EXACT:
        return _EXACT[lower]

    if tokens[0] == "add":
        if len(tokens) < 2:
            return "__error__: missing package — usage: add <package>"
        if len(tokens) >= 3 and tokens[1] == "dev":
            return f"npm install -D {raw[2]}"
        return f"npm install {raw[1]}"

    if tokens[0] == "uninstall":
        if len(tokens) < 2:
            return "__error__: missing package — usage: uninstall <package>"
        return f"npm uninstall {raw[1]}"

    return None
