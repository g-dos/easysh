# easysh

A human-friendly interactive shell that translates simple words into real shell commands, with safe execution and seamless fallback to native commands.

## Philosophy

> Don't replace the terminal. Make it easier to use.

easysh always shows you the real command it runs. So you learn while you work.

## Installation

```bash
pip install prompt_toolkit
python main.py
```

## Usage

```
easysh ~/projects ❯ list
→ ls

easysh ~/projects ❯ list all
→ ls -la

easysh ~/projects ❯ open src
→ cd src

easysh ~/src ❯ where
→ pwd

easysh ~/src ❯ create build
→ mkdir build

easysh ~/src ❯ copy file.txt backup.txt
→ cp file.txt backup.txt

easysh ~/src ❯ move old.txt new.txt
→ mv old.txt new.txt

easysh ~/src ❯ delete temp.txt
→ rm temp.txt
(asks for confirmation)

easysh ~/src ❯ git status
→ git status
(passes through directly)

easysh ~/src ❯ npm install
→ npm install
(passes through directly)
```

## Features

- Human-readable command translation
- Always shows the real command being run
- Safe execution: confirmation required for destructive commands (`rm`)
- Native fallback: unknown commands run as-is
- Arrow key history (up/down)
- Ctrl+C is safe (does not exit)
- Ctrl+D or `exit` / `quit` to leave

## Supported Translations

| You type         | Runs          |
|------------------|---------------|
| `list`           | `ls`          |
| `list all`       | `ls -la`      |
| `open <dir>`     | `cd <dir>`    |
| `where`          | `pwd`         |
| `create <name>`  | `mkdir <name>`|
| `copy <a> <b>`   | `cp <a> <b>`  |
| `move <a> <b>`   | `mv <a> <b>`  |
| `delete <file>`  | `rm <file>`   |
| `run <cmd>`      | `<cmd>`       |
| `kill <proc>`    | `pkill -f <proc>` |
| `git ...`        | `git ...` (passthrough) |
| `npm ...`        | `npm ...` (passthrough) |
| anything else    | runs as-is    |
