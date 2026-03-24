import json
import os

_CONFIG_PATH = os.path.expanduser("~/.easyshrc")

_ONBOARDING = """\
Welcome to easysh 👋

Type simple commands instead of memorizing shell syntax.

  list           → ls
  create app     → mkdir app
  open app       → cd app
  save fix bug   → git add -A && git commit -m "fix bug"
  dev            → npm run dev

Type 'mode learn' to see explanations as you go.
Type 'exit' to quit.
"""


def is_first_run() -> bool:
    try:
        with open(_CONFIG_PATH) as f:
            return not json.load(f).get("onboarding_shown", False)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return True


def mark_onboarding_done() -> None:
    try:
        with open(_CONFIG_PATH, "w") as f:
            json.dump({"onboarding_shown": True}, f)
    except OSError:
        pass


def show_onboarding() -> None:
    print(_ONBOARDING)
    mark_onboarding_done()
