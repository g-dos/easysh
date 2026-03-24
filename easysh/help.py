_HELP = """
commands:

  filesystem   list, list all, open <dir>, where, create <name>, delete <file>
               show <file>, find <name>, search <pattern>, edit <file>
               move <a> <b>, copy <a> <b>, rename <a> <b>, size <path>
               count <file>, compress <path>, extract <file>
               touch <file>, allow <file>, link <src> <dst>

  git          status, diff, log, save, save <message>, push, pull, fetch
               branch, new branch <name>, switch <branch>, merge <branch>
               stash, pop, undo, discard, clone <url>, init, remote, tag <v>

  npm          dev, build, start, test, lint, install, outdated, audit
               add <pkg>, add dev <pkg>, uninstall <pkg>, packages, scripts

  system       disk, memory, ports, processes, ip, uptime, whoami, env
               clear, history, run <cmd>, kill <name>

  shell        mode learn / mode normal
               help
               exit / quit

unknown commands run as-is (native shell fallback).
"""


def show_help() -> None:
    print(_HELP)
