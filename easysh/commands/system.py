from typing import Optional

_EXACT: dict[str, str] = {
    "clear":     "clear",
    "history":   "history",
    "disk":      "df -h",
    "memory":    "vm_stat",
    "processes": "ps aux",
    "ps":        "ps aux",
    "ports":     "lsof -iTCP -sTCP:LISTEN -P -n",
    "ip":        "curl -s ifconfig.me",
    "uptime":    "uptime",
    "whoami":    "whoami",
    "env":       "env",
}


def translate(tokens: list, raw: list, lower: str) -> Optional[str]:
    if lower in _EXACT:
        return _EXACT[lower]

    if tokens[0] == "run":
        if len(tokens) < 2:
            return "__error__: missing command — usage: run <cmd>"
        return " ".join(raw[1:])

    if tokens[0] == "kill":
        if len(tokens) < 2:
            return "__error__: missing process — usage: kill <name>"
        return f"pkill -f {raw[1]}"

    return None
