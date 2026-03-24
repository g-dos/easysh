from typing import Optional

# Ordered longest-prefix-first so more specific entries match before generic ones.
_EXPLANATIONS: list[tuple[str, str]] = [
    # Filesystem
    ("ls -la",                  "Lists all files including hidden ones, with details"),
    ("ls",                      "Lists files in the current directory"),
    ("pwd",                     "Prints the current working directory"),
    ("mkdir",                   "Creates a new directory"),
    ("cd",                      "Changes the current directory"),
    ("rm -rf",                  "Recursively removes a directory and all its contents"),
    ("rm",                      "Removes a file"),
    ("mv",                      "Moves or renames a file"),
    ("cp",                      "Copies a file or directory"),
    ("cat",                     "Prints the contents of a file"),
    ("nano",                    "Opens a file in the nano text editor"),
    ("touch",                   "Creates an empty file or updates its timestamp"),
    ("find . -name",            "Searches for files matching a name pattern"),
    ("grep -r",                 "Searches for a text pattern recursively in files"),
    ("wc -l",                   "Counts the number of lines in a file"),
    ("du -sh",                  "Shows the disk size of a file or directory"),
    ("df -h",                   "Shows available disk space on all drives"),
    ("tar -czf",                "Compresses a directory into a .tar.gz archive"),
    ("tar -xzf",                "Extracts a .tar.gz archive"),
    ("unzip",                   "Extracts a .zip archive"),
    ("chmod +x",                "Makes a file executable"),
    ("ln -s",                   "Creates a symbolic link"),
    # System
    ("ps aux",                  "Lists all running processes"),
    ("pkill -f",                "Kills a process by name"),
    ("lsof -iTCP",              "Lists processes listening on network ports"),
    ("curl -s ifconfig.me",     "Fetches your current public IP address"),
    ("vm_stat",                 "Shows memory usage statistics (macOS)"),
    ("uptime",                  "Shows how long the system has been running"),
    ("whoami",                  "Prints the current logged-in user"),
    ("history",                 "Shows previously run commands"),
    ("clear",                   "Clears the terminal screen"),
    ("env",                     "Lists all environment variables"),
    # Git
    ("git add -A && git commit","Stages all changes and creates a commit"),
    ("git status",              "Shows the current state of the repository"),
    ("git diff",                "Shows unstaged changes in tracked files"),
    ("git log --oneline",       "Shows a compact commit history"),
    ("git push",                "Pushes local commits to the remote repository"),
    ("git pull",                "Pulls and merges the latest remote changes"),
    ("git fetch",               "Downloads remote changes without merging"),
    ("git branch",              "Lists all local branches"),
    ("git checkout -b",         "Creates and switches to a new branch"),
    ("git checkout",            "Switches to an existing branch"),
    ("git merge",               "Merges another branch into the current one"),
    ("git stash pop",           "Restores the most recently stashed changes"),
    ("git stash",               "Temporarily saves uncommitted changes"),
    ("git reset HEAD~1 --soft", "Undoes the last commit, keeping changes staged"),
    ("git checkout -- .",       "Discards all uncommitted changes in the working tree"),
    ("git clone",               "Downloads a remote repository locally"),
    ("git init",                "Initializes a new git repository"),
    ("git remote -v",           "Lists the configured remote repositories"),
    ("git tag",                 "Creates a tag pointing to the current commit"),
    # NPM
    ("npm run dev",             "Starts the development server"),
    ("npm run build",           "Builds the project for production"),
    ("npm start",               "Runs the default start script"),
    ("npm test",                "Runs the test suite"),
    ("npm run lint",            "Runs the linter to check code style"),
    ("npm install -D",          "Installs a package as a dev dependency"),
    ("npm install",             "Installs all project dependencies"),
    ("npm uninstall",           "Removes an installed package"),
    ("npm list",                "Lists installed packages"),
    ("npm run",                 "Lists available npm scripts"),
    ("npm outdated",            "Shows packages that have newer versions available"),
    ("npm audit",               "Checks for known security vulnerabilities"),
]


def explain(cmd: str) -> Optional[str]:
    """Return a one-line explanation for cmd, matched by prefix."""
    for prefix, description in _EXPLANATIONS:
        if cmd.startswith(prefix):
            return description
    return None
