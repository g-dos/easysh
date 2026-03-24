# easysh

A human-friendly interactive shell that translates simple words into real shell commands, with safe execution and seamless fallback to native commands.

## Philosophy

> Don't replace the terminal. Make it easier to use.

easysh always shows you the real command it runs. So you learn while you work.

## Installation

```bash
brew tap g-dos/easysh
brew install easysh
```

## Usage

```
easysh ~/projects ❯ list
→ ls

easysh ~/projects ❯ save fix login bug
→ git add -A && git commit -m "fix login bug"

easysh ~/projects ❯ dev
→ npm run dev

easysh ~/projects ❯ search TODO in src
→ grep -r "TODO" src

easysh ~/projects ❯ delete temp.txt
→ rm temp.txt
(asks for confirmation)

easysh ~/projects ❯ git log --all
→ git log --all
(passes through directly)
```

## Features

- Human-readable command translation (filesystem, git, npm, system)
- Always shows the real command being run — learn while you work
- Safe execution: confirmation required for destructive commands
- Native fallback: unknown commands run as-is
- Arrow key history (up/down)
- Ctrl+C is safe (does not exit)
- Ctrl+D or `exit` / `quit` to leave

## Command Reference

### Filesystem

| You type              | Runs                        |
|-----------------------|-----------------------------|
| `list`                | `ls`                        |
| `list all`            | `ls -la`                    |
| `where`               | `pwd`                       |
| `open <dir>`          | `cd <dir>`                  |
| `create <name>`       | `mkdir -p <name>`           |
| `delete <file>`       | `rm <file>` ⚠️              |
| `move <a> <b>`        | `mv <a> <b>`                |
| `rename <a> <b>`      | `mv <a> <b>`                |
| `copy <a> <b>`        | `cp -r <a> <b>`             |
| `show <file>`         | `cat <file>`                |
| `edit <file>`         | `nano <file>`               |
| `touch <file>`        | `touch <file>`              |
| `find <name>`         | `find . -name "<name>"`     |
| `search <pattern>`    | `grep -r "<pattern>" .`     |
| `search <p> in <dir>` | `grep -r "<p>" <dir>`       |
| `count <file>`        | `wc -l <file>`              |
| `size <path>`         | `du -sh <path>`             |
| `compress <path>`     | `tar -czf <path>.tar.gz`    |
| `extract <file>`      | `tar -xzf <file>`           |
| `allow <file>`        | `chmod +x <file>`           |
| `link <src> <dst>`    | `ln -s <src> <dst>`         |

### System

| You type    | Runs                              |
|-------------|-----------------------------------|
| `clear`     | `clear`                           |
| `history`   | `history`                         |
| `disk`      | `df -h`                           |
| `memory`    | `vm_stat`                         |
| `processes` | `ps aux`                          |
| `ports`     | `lsof -iTCP -sTCP:LISTEN -P -n`   |
| `ip`        | `curl -s ifconfig.me`             |
| `uptime`    | `uptime`                          |
| `whoami`    | `whoami`                          |
| `env`       | `env`                             |
| `run <cmd>` | `<cmd>`                           |
| `kill <p>`  | `pkill -f <p>`                    |

### Git

| You type            | Runs                              |
|---------------------|-----------------------------------|
| `status`            | `git status`                      |
| `diff`              | `git diff`                        |
| `log`               | `git log --oneline -10`           |
| `save`              | `git add -A && git commit -m "update"` |
| `save <message>`    | `git add -A && git commit -m "<message>"` |
| `push`              | `git push`                        |
| `pull`              | `git pull`                        |
| `fetch`             | `git fetch`                       |
| `branch`            | `git branch`                      |
| `new branch <name>` | `git checkout -b <name>`          |
| `switch <branch>`   | `git checkout <branch>`           |
| `merge <branch>`    | `git merge <branch>`              |
| `stash`             | `git stash`                       |
| `pop`               | `git stash pop`                   |
| `undo`              | `git reset HEAD~1 --soft`         |
| `discard`           | `git checkout -- .` ⚠️            |
| `clone <url>`       | `git clone <url>`                 |
| `init`              | `git init`                        |
| `remote`            | `git remote -v`                   |
| `tag <version>`     | `git tag <version>`               |
| `git ...`           | `git ...` (passthrough)           |

### NPM

| You type          | Runs                  |
|-------------------|-----------------------|
| `dev`             | `npm run dev`         |
| `build`           | `npm run build`       |
| `start`           | `npm start`           |
| `test`            | `npm test`            |
| `lint`            | `npm run lint`        |
| `install`         | `npm install`         |
| `add <pkg>`       | `npm install <pkg>`   |
| `add dev <pkg>`   | `npm install -D <pkg>`|
| `uninstall <pkg>` | `npm uninstall <pkg>` |
| `packages`        | `npm list --depth=0`  |
| `scripts`         | `npm run`             |
| `outdated`        | `npm outdated`        |
| `audit`           | `npm audit`           |
| `npm ...`         | `npm ...` (passthrough)|

⚠️ = requires confirmation before execution
