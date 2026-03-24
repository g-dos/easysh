# easysh

**A human-friendly shell.**

Type what you mean. easysh translates it into real commands — and always shows you what it ran.

![easysh demo](demo/demo.gif)

```
easysh ~/project ❯ create app
→ mkdir -p app

easysh ~/project ❯ save fix auth bug
→ git add -A && git commit -m "fix auth bug"

easysh ~/project ❯ search TODO in src
→ grep -r "TODO" src

easysh ~/project ❯ dev
→ npm run dev
```

---

## Why easysh?

You open a terminal to get something done.

Instead, you spend 30 seconds trying to remember if it's `ls -la` or `ls -al`. You google "how to find a file linux". You type `git add . && git commit -m` and forget the closing quote. Again.

The terminal is powerful. But it wasn't designed to be friendly.

easysh sits on top of your shell and lets you speak plainly. It shows you the real command every time — so you actually learn, instead of just copying and pasting forever.

---

## Features

- **Natural language** — type `list`, `create`, `push`, `dev`
- **Always transparent** — always prints the real command before running it
- **Real shell fallback** — unknown commands run natively (`docker`, `make`, `python`, anything)
- **Safe by default** — destructive commands require confirmation
- **Suggests alternatives** — shows hints before running an unrecognized command
- **Tab completion** — complete commands and file paths with Tab
- **Persistent history** — arrow keys across sessions (`~/.easysh_history`)
- **Git branch in prompt** — `easysh ~/project (main) ❯`
- **Learn mode** — explains every command as it runs (`mode learn`)
- **Preview mode** — see what would run without executing (`mode preview`)
- **No config, no setup** — works immediately after install

---

## Installation

```bash
brew tap g-dos/easysh
brew install easysh
```

Then just run:

```bash
easysh
```

---

## Usage

```
easysh ~/project ❯ list
→ ls

easysh ~/project ❯ list all
→ ls -la

easysh ~/project ❯ open src
→ cd src

easysh ~/src ❯ create utils
→ mkdir -p utils

easysh ~/src ❯ show config.json
→ cat config.json

easysh ~/src ❯ search api_key in src
→ grep -r "api_key" src

easysh ~/src ❯ status
→ git status

easysh ~/src ❯ save refactor auth module
→ git add -A && git commit -m "refactor auth module"

easysh ~/src ❯ new branch feature/login
→ git checkout -b feature/login

easysh ~/src ❯ dev
→ npm run dev

easysh ~/src ❯ add lodash
→ npm install lodash

easysh ~/src ❯ docker ps
→ docker ps        (native passthrough)

easysh ~/src ❯ exit
bye.
```

Arrow keys for history. Ctrl+C to cancel. Ctrl+D or `exit` to quit.

---

## Philosophy

> Don't replace the terminal. Make it easier to use.

easysh is not a new shell. It's a friendly layer over the one you already have. Every command it runs is visible, copy-pasteable, and learnable.

The goal is that after a few weeks, you don't need easysh anymore — because you've learned the real commands. That's a feature, not a bug.

---

## Command Reference

### Filesystem

| Type | Runs |
|------|------|
| `list` | `ls` |
| `list all` | `ls -la` |
| `where` | `pwd` |
| `open <dir>` | `cd <dir>` |
| `create <name>` | `mkdir -p <name>` |
| `delete <file>` ⚠ | `rm <file>` |
| `move <a> <b>` | `mv <a> <b>` |
| `rename <a> <b>` | `mv <a> <b>` |
| `copy <a> <b>` | `cp -r <a> <b>` |
| `show <file>` | `cat <file>` |
| `edit <file>` | `nano <file>` |
| `find <name>` | `find . -name "<name>"` |
| `search <p>` | `grep -r "<p>" .` |
| `search <p> in <dir>` | `grep -r "<p>" <dir>` |
| `size <path>` | `du -sh <path>` |
| `count <file>` | `wc -l <file>` |
| `compress <path>` | `tar -czf <path>.tar.gz <path>` |
| `extract <file>` | `tar -xzf <file>` |
| `allow <file>` | `chmod +x <file>` |
| `link <src> <dst>` | `ln -s <src> <dst>` |

### System

| Type | Runs |
|------|------|
| `disk` | `df -h` |
| `memory` | `vm_stat` |
| `processes` | `ps aux` |
| `ports` | `lsof -iTCP -sTCP:LISTEN -P -n` |
| `ip` | `curl -s ifconfig.me` |
| `uptime` | `uptime` |
| `clear` | `clear` |
| `history` | `history` |
| `kill <name>` | `pkill -f <name>` |
| `run <cmd>` | `<cmd>` |

### Git

| Type | Runs |
|------|------|
| `status` | `git status` |
| `diff` | `git diff` |
| `log` | `git log --oneline -10` |
| `save` | `git add -A && git commit -m "update"` |
| `save <message>` | `git add -A && git commit -m "<message>"` |
| `push` | `git push` |
| `pull` | `git pull` |
| `fetch` | `git fetch` |
| `branch` | `git branch` |
| `new branch <name>` | `git checkout -b <name>` |
| `switch <branch>` | `git checkout <branch>` |
| `merge <branch>` | `git merge <branch>` |
| `stash` | `git stash` |
| `pop` | `git stash pop` |
| `undo` | `git reset HEAD~1 --soft` |
| `discard` ⚠ | `git checkout -- .` |
| `clone <url>` | `git clone <url>` |
| `init` | `git init` |
| `remote` | `git remote -v` |
| `tag <version>` | `git tag <version>` |
| `git ...` | passthrough |

### NPM

| Type | Runs |
|------|------|
| `dev` | `npm run dev` |
| `build` | `npm run build` |
| `start` | `npm start` |
| `test` | `npm test` |
| `lint` | `npm run lint` |
| `install` | `npm install` |
| `add <pkg>` | `npm install <pkg>` |
| `add dev <pkg>` | `npm install -D <pkg>` |
| `uninstall <pkg>` | `npm uninstall <pkg>` |
| `packages` | `npm list --depth=0` |
| `scripts` | `npm run` |
| `outdated` | `npm outdated` |
| `audit` | `npm audit` |
| `npm ...` | passthrough |

⚠ requires confirmation

---

## Contributing

easysh is intentionally small. Contributions that add commands, fix bugs, or improve UX are welcome.

```bash
git clone https://github.com/g-dos/easysh
cd easysh
pip install -e ".[dev]"
python -m easysh.main
```

Adding a command is as simple as adding a rule to one of the modules in `easysh/commands/`. Each module is ~50 lines and self-contained.

Open an issue before large changes. Keep it simple.

---

## Changelog

### v0.5.0
- Persistent history across sessions (`~/.easysh_history`)
- Tab completion for commands and file paths
- Git branch shown in prompt
- `back` command to return to previous directory
- `version` command
- `mode preview` — translate without executing
- New filesystem commands: `newest`, `biggest`, `tree`, `hidden`, `empty`, `permissions`
- 72 automated tests

### v0.4.0
- Onboarding on first run
- Suggestion engine (shows hints before execution)
- Compound command explanations in learn mode
- Visual polish

### v0.3.0
- Refactored commands into separate modules (`filesystem`, `git`, `npm`, `system`)
- Improved error messages with usage hints

### v0.2.0
- Expanded to ~60 translations across git, npm, filesystem, and system

### v0.1.0
- Initial release — interactive shell with basic filesystem commands
- Homebrew tap via `g-dos/easysh`
