#!/usr/bin/env python3
"""One-command daily pipeline: capture ALL games via tbp, then extract.

Run from the project root (or anywhere; paths are relative to this file):

    python3 src/run_all.py                 # today
    python3 src/run_all.py --date 2026-07-15

Steps:
    1. src/tbp_capture.py          -> cache/<date>/<game>.html + <game>_meta.json
                                       (single HTML-getter strategy; covers the
                                        grid games via their /view/<slug>/desktop
                                        iframe URL and wend/patches via the
                                        "Iniciar jogo"/"Start game" click)
    2. src/scrape_games.py         -> outputs/<date>/zip|tango|queens|minisudoku.json
                                       (reads the cached HTML; no re-dump)
    3. src/extract_wend.py         -> outputs/<date>/wend.json  (no --words:
                                       the "words" key is omitted unless you pass
                                       them; they are not in the board DOM)
    4. src/extract_patches.py      -> outputs/<date>/patches.json

Pinpoint / Crossclimb remain deferred (their content needs in-game reveal
buttons + a voyager session) and are commented out in tbp_capture.py.
"""
import os, sys, subprocess, argparse
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = HERE


def run(script, *extra):
    cmd = [sys.executable, os.path.join(SRC, script), *extra]
    print(f"\n$ {' '.join(cmd)}", flush=True)
    r = subprocess.run(cmd)
    if r.returncode != 0:
        print(f"  [WARN] {script} exited {r.returncode}", flush=True)
    return r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    args = ap.parse_args()
    d = args.date

    # 1) capture every game's HTML via tbp (the single strategy)
    run("tbp_capture.py")

    # 2) extract the four grid games (read cache, no headless re-dump)
    run("scrape_games.py", "--date", d,
        "--games", "zip,tango,queens,minisudoku")

    # 3) wend (no words placeholder) + patches, using the captured number meta
    run("extract_wend.py", "--date", d,
        "--meta", os.path.join(ROOT, "cache", d, "wend_meta.json"))
    run("extract_patches.py", "--date", d,
        "--meta", os.path.join(ROOT, "cache", d, "patches_meta.json"))

    print(f"\nDone. Outputs in outputs/{d}/", flush=True)


if __name__ == "__main__":
    main()
