import re

# Dict is defined unordered; matching always uses keys sorted longest-first
# to prevent shorter prefixes shadowing more specific entries.
_EXPLANATIONS: dict[str, str] = {
    # Filesystem
    "ls -la":                  "Lists all files including hidden ones, with details",
    "ls":                      "Lists files in the current directory",
    "pwd":                     "Prints the current working directory",
    "mkdir":                   "Creates a new directory",
    "cd":                      "Changes the current directory",
    "rm -rf":                  "Recursively removes a directory and all its contents",
    "rm":                      "Removes a file",
    "mv":                      "Moves or renames a file",
    "cp":                      "Copies a file or directory",
    "cat":                     "Prints the contents of a file",
    "nano":                    "Opens a file in the nano text editor",
    "touch":                   "Creates an empty file or updates its timestamp",
    "find . -name":            "Searches for files matching a name pattern",
    "grep -r":                 "Searches for a text pattern recursively in files",
    "wc -l":                   "Counts the number of lines in a file",
    "du -sh":                  "Shows the disk size of a file or directory",
    "df -h":                   "Shows available disk space on all drives",
    "tar -czf":                "Compresses files into a .tar.gz archive",
    "tar -xzf":                "Extracts a .tar.gz archive",
    "unzip":                   "Extracts a .zip archive",
    "chmod +x":                "Makes a file executable",
    "ln -s":                   "Creates a symbolic link",
    # System
    "ps aux":                  "Lists all running processes",
    "pkill -f":                "Kills a process by name",
    "lsof -iTCP":              "Lists processes listening on network ports",
    "curl -s ifconfig.me":     "Fetches your current public IP address",
    "vm_stat":                 "Shows memory usage statistics (macOS)",
    "uptime":                  "Shows how long the system has been running",
    "whoami":                  "Prints the current logged-in user",
    "history":                 "Shows previously run commands",
    "clear":                   "Clears the terminal screen",
    "env":                     "Lists all environment variables",
    # Git
    "git add -A":              "Stages all changes for the next commit",
    "git commit":              "Creates a commit with a message",
    "git status":              "Shows the current state of the repository",
    "git diff":                "Shows unstaged changes in tracked files",
    "git log --oneline":       "Shows a compact commit history",
    "git push":                "Pushes local commits to the remote repository",
    "git pull":                "Pulls and merges the latest remote changes",
    "git fetch":               "Downloads remote changes without merging",
    "git branch":              "Lists all local branches",
    "git checkout -b":         "Creates and switches to a new branch",
    "git checkout -- .":       "Discards all uncommitted changes in the working tree",
    "git checkout":            "Switches to an existing branch",
    "git merge":               "Merges another branch into the current one",
    "git stash pop":           "Restores the most recently stashed changes",
    "git stash":               "Temporarily saves uncommitted changes",
    "git reset HEAD~1 --soft": "Undoes the last commit, keeping changes staged",
    "git clone":               "Downloads a remote repository locally",
    "git init":                "Initializes a new git repository",
    "git remote -v":           "Lists the configured remote repositories",
    "git tag":                 "Creates a tag pointing to the current commit",
    # NPM
    "npm run dev":             "Starts the development server",
    "npm run build":           "Builds the project for production",
    "npm run lint":            "Runs the linter to check code style",
    "npm run":                 "Lists or runs npm scripts",
    "npm start":               "Runs the default start script",
    "npm test":                "Runs the test suite",
    "npm install -D":          "Installs a package as a dev dependency",
    "npm install":             "Installs all project dependencies",
    "npm uninstall":           "Removes an installed package",
    "npm list":                "Lists installed packages",
    "npm outdated":            "Shows packages that have newer versions available",
    "npm audit":               "Checks for known security vulnerabilities",
}

# Pre-sort keys longest-first once at import time
_SORTED_KEYS: list[str] = sorted(_EXPLANATIONS, key=len, reverse=True)

_COMPOUND_SPLIT = re.compile(r"\s*&&\s*|\s*;\s*")


def _explain_single(part: str) -> str | None:
    """Return the explanation for a single (non-compound) command fragment."""
    part = part.strip()
    for key in _SORTED_KEYS:
        if part.startswith(key):
            return _EXPLANATIONS[key]
    return None


def explain(cmd: str) -> list[str]:
    """Return explanations for each part of a (possibly compound) command."""
    parts = [p for p in _COMPOUND_SPLIT.split(cmd) if p.strip()]
    seen: set[str] = set()
    results: list[str] = []
    for part in parts:
        desc = _explain_single(part)
        if desc and desc not in seen:
            seen.add(desc)
            results.append(desc)
    return results
