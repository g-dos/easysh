from easysh.commands import translate


# Filesystem
def test_list():
    assert translate("list") == "ls"

def test_list_all():
    assert translate("list all") == "ls -la"

def test_where():
    assert translate("where") == "pwd"

def test_open():
    assert translate("open src") == "cd src"

def test_open_missing_arg():
    assert translate("open").startswith("__error__")

def test_create():
    assert translate("create app") == "mkdir -p app"

def test_delete():
    assert translate("delete README.md") == "rm README.md"

def test_move():
    assert translate("move a.txt b.txt") == "mv a.txt b.txt"

def test_copy():
    assert translate("copy a.txt b.txt") == "cp -r a.txt b.txt"

def test_show():
    assert translate("show README.md") == "cat README.md"

def test_find():
    assert translate("find main.py") == 'find . -name "main.py"'

def test_count():
    assert translate("count app.py") == "wc -l app.py"

def test_size():
    assert translate("size dist") == "du -sh dist"

def test_compress():
    assert translate("compress dist") == "tar -czf dist.tar.gz dist"

def test_extract_zip():
    assert translate("extract archive.zip") == "unzip archive.zip"

def test_extract_tar():
    assert translate("extract archive.tar.gz") == "tar -xzf archive.tar.gz"

def test_newest():
    assert translate("newest") == "ls -t | head -1"

def test_biggest():
    assert translate("biggest") == "du -sh * | sort -rh | head -5"

def test_tree():
    assert translate("tree") == "find . -maxdepth 2 | sort"

def test_hidden():
    assert translate("hidden") == 'ls -la | grep "^\\."'

def test_empty():
    assert translate("empty fixtures") == "mkdir -p fixtures && touch fixtures/.gitkeep"

def test_permissions():
    assert translate("permissions script.sh") == "ls -la script.sh"


# Git
def test_git_status():
    assert translate("status") == "git status"

def test_git_save():
    assert translate("save") == 'git add -A && git commit -m "update"'

def test_git_save_message():
    assert translate("save fix bug") == 'git add -A && git commit -m "fix bug"'

def test_git_push():
    assert translate("push") == "git push"

def test_git_pull():
    assert translate("pull") == "git pull"

def test_git_log():
    assert translate("log") == "git log --oneline -10"

def test_git_diff():
    assert translate("diff") == "git diff"

def test_git_branch():
    assert translate("branch") == "git branch"

def test_git_new_branch():
    assert translate("new branch feature") == "git checkout -b feature"

def test_git_switch():
    assert translate("switch main") == "git checkout main"

def test_git_stash():
    assert translate("stash") == "git stash"

def test_git_pop():
    assert translate("pop") == "git stash pop"

def test_git_undo():
    assert translate("undo") == "git reset HEAD~1 --soft"

def test_git_discard():
    assert translate("discard") == "git checkout -- ."

def test_git_init():
    assert translate("init") == "git init"

def test_git_clone():
    assert translate("clone https://github.com/foo/bar") == "git clone https://github.com/foo/bar"


# npm
def test_npm_dev():
    assert translate("dev") == "npm run dev"

def test_npm_build():
    assert translate("build") == "npm run build"

def test_npm_install():
    assert translate("install") == "npm install"

def test_npm_add():
    assert translate("add express") == "npm install express"

def test_npm_add_dev():
    assert translate("add dev eslint") == "npm install -D eslint"

def test_npm_uninstall():
    assert translate("uninstall lodash") == "npm uninstall lodash"

def test_npm_packages():
    assert translate("packages") == "npm list --depth=0"

def test_npm_outdated():
    assert translate("outdated") == "npm outdated"


# System
def test_disk():
    assert translate("disk") == "df -h"

def test_memory():
    assert translate("memory") == "vm_stat"

def test_ports():
    assert translate("ports") == "lsof -iTCP -sTCP:LISTEN -P -n"

def test_processes():
    assert translate("processes") == "ps aux"

def test_ip():
    assert translate("ip") == "curl -s ifconfig.me"

def test_whoami():
    assert translate("whoami") == "whoami"

def test_clear():
    assert translate("clear") == "clear"

def test_history():
    assert translate("history") == "history"

def test_run():
    assert translate("run make test") == "make test"


# Passthrough — unknown input returns None
def test_passthrough_unknown():
    assert translate("foobar baz") is None

def test_passthrough_git():
    assert translate("git status") is None

def test_passthrough_npm():
    assert translate("npm run foo") is None
