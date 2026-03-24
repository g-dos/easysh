from prompt_toolkit.completion import Completer, Completion, PathCompleter

_COMMANDS = [
    "list", "list all", "open", "where", "create", "delete", "show", "find",
    "search", "edit", "move", "copy", "rename", "size", "count", "compress",
    "extract", "touch", "allow", "link", "newest", "biggest", "empty", "tree",
    "hidden", "permissions",
    "status", "diff", "log", "save", "push", "pull", "fetch", "branch",
    "new branch", "switch", "merge", "stash", "pop", "undo", "discard",
    "clone", "init", "remote", "tag",
    "dev", "build", "start", "test", "lint", "install", "add", "add dev",
    "uninstall", "packages", "scripts", "outdated", "audit",
    "disk", "memory", "ports", "processes", "ip", "uptime", "whoami", "env",
    "clear", "history", "run", "kill",
    "help", "mode learn", "mode normal", "mode preview", "version", "back",
    "exit",
]

_FILE_ARG_COMMANDS = {
    "open", "delete", "show", "edit", "find", "count",
    "size", "compress", "extract", "allow", "touch", "permissions",
}


class EasyshCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        stripped = text.strip()
        word = document.get_word_before_cursor()
        first_token = stripped.split()[0].lower() if stripped else ""

        if " " not in stripped:
            for cmd in _COMMANDS:
                if cmd.startswith(word.lower()):
                    yield Completion(cmd[len(word):], start_position=0)
        elif first_token in _FILE_ARG_COMMANDS:
            yield from PathCompleter().get_completions(document, complete_event)
