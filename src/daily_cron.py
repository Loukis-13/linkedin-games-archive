#!/usr/bin/env python3
"""Daily pipeline: capture + extract, then send ONE Telegram bubble per game.

Run by the 8 AM cron (script-only, no agent). Also usable manually:
    python3 src/daily_cron.py                 # full run + send
    python3 src/daily_cron.py --skip-capture  # re-render today's cached games
    python3 src/daily_cron.py --no-send       # print locally instead of sending

Flow:
    1. run_all.py        -> cache/<date>/<game>.html + outputs/<date>/<game>.json
                           (tbp daemon auto-starts on the first goto)
    2. for each game: render with view_json.py, send as its own bubble.

Adding a game later: append its slug to GAMES below (and make sure
view_json.py has a renderer for it). pinpoint / crossclimb are left commented
until their in-game reveal flow is scripted.
"""
import os
import sys
import json
import argparse
import subprocess
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEND_CMD = "hermes"          # on PATH; `hermes send -t telegram "<msg>"`
TARGET = "telegram"          # home channel -> this chat

# Games rendered + sent, in order. Append new ones here as they're scripted.
GAMES = [
    "zip",
    "tango",
    "queens",
    "minisudoku",
    "wend",
    "patches",
    # "pinpoint",    # DEFERRED: needs in-game reveal
    # "crossclimb",  # DEFERRED: needs in-game reveal
]


def run_capture(d):
    subprocess.run([sys.executable, os.path.join(HERE, "run_all.py")], check=False)


def render(game, d):
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "view_json.py"), game, "--date", d],
        capture_output=True, text=True)
    return r.stdout.strip()


def sanity(game, d):
    """Short per-game status line; flags obviously-broken extractions."""
    p = os.path.join(ROOT, "outputs", d, f"{game}.json")
    if not os.path.exists(p):
        return f"⚠️ {game}: no output file (extraction failed)"
    try:
        j = json.load(open(p))
    except Exception as e:
        return f"⚠️ {game}: bad JSON ({e})"
    num = j.get("number")
    gs = j.get("grid_size") or ["?", "?"]
    if game == "wend":
        holes = sum(1 for row in j.get("grid", []) for v in row if v == ".")
        metric = f"{holes} holes"
        ok = holes >= 0 and len(j.get("grid", [])) > 0
    elif game == "patches":
        n = len(j.get("clues", []))
        metric = f"{n} clues"
        ok = n > 0
    elif game == "minisudoku":
        cells = j.get("cells", [])
        n = sum(1 for row in cells for v in row if v not in (None, "", ".", 0))
        metric = f"{n} givens"
        ok = len(cells) > 0
    elif game == "zip":
        n = len(j.get("nodes", []))
        metric = f"{n} nodes"
        ok = n > 0
    elif game == "tango":
        n = len(j.get("symbols", []))
        metric = f"{n} symbols"
        ok = n > 0
    elif game == "queens":
        board = j.get("board", [])
        n = len({v for row in board for v in row})
        metric = f"{n} regions"
        ok = len(board) > 0
    else:
        metric = f"{gs[0]}×{gs[1]}"
        ok = True
    icon = "🟩" if ok else "⚠️"
    num_s = f"#{num}" if num is not None else "#?"
    return f"{icon} {game} {num_s} · {gs[0]}×{gs[1]} · {metric}"


def send_bubble(target, text):
    r = subprocess.run([SEND_CMD, "send", "-t", target, text],
                       capture_output=True, text=True, timeout=30)
    return r.returncode == 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--target", default=TARGET)
    ap.add_argument("--skip-capture", action="store_true",
                    help="assume cache/outputs already exist for --date")
    ap.add_argument("--no-send", action="store_true",
                    help="print locally instead of sending (dry run)")
    args = ap.parse_args()
    d = args.date
    os.chdir(ROOT)

    if not args.skip_capture:
        run_capture(d)

    failures = []
    for g in GAMES:
        head = sanity(g, d)
        body = render(g, d)
        # Wrap the board in a code block so monospace is preserved on Telegram
        # (ASCII grids collapse without it). Header stays outside as plain text.
        msg = f"{head}\n\n```\n{body}\n```" if body else head
        if len(msg) > 3900:                       # Telegram cap ~4096
            msg = f"{head}\n\n(board too large to send; see outputs/{d}/{g}.json)"
        if args.no_send:
            print(f"----- {g} -----\n{msg}\n")
        else:
            if not send_bubble(args.target, msg):
                failures.append(g)

    if not args.no_send and failures:
        # only printed on failure -> cron delivers this as the lone alert bubble
        print(f"⚠️ daily_cron: failed to send {failures} for {d}. "
              f"Files are on disk under outputs/{d}/.")


if __name__ == "__main__":
    main()
