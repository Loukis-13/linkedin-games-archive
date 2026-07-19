#!/usr/bin/env python3
"""Extract the Pinpoint puzzle (clues + revealed category) from a captured
reveal HTML and write outputs/<date>/pinpoint.json.

How the data is captured (see src/pinpoint_playwright.py):
  Pinpoint only reveals the answer in a brief window after the 5th guess, and
  the answer/category text isn't in any unauthenticated HTML. A Playwright run
  on a PC freezes the reveal + sniffs the voyager network response, saving:
    cache/<date>/pinpoint_reveal.html   -- full DOM at reveal (board + answer)
    cache/<date>/pinpoint_network.json  -- guess/answer network responses
  (No tbp capture for this game -- it can't beat the reveal->leaderboard race.)

Format:
  {
    "game": "pinpoint",
    "number": <int|null>,
    "date": "YYYY-MM-DD",
    "answer": "<revealed category/answer phrase>",
    "blanks": <int>,           # number of letters in the answer word
    "clues": ["Life", "Show", "Row", "Tug", "Whatever floats your"]
  }

The reveal DOM is locale-independent (driven by pinpoint__ classes, not text):
  - each clue word  -> .pinpoint__card--clue  (5 of them, order = pista 1..5)
  - the answer text -> .pinpoint__card__answer_text
  - the blanks      -> .pinpoint__bottom-section  (count the '_')

The puzzle NUMBER is not in the reveal DOM. It lives in pinpofit_network.json:
  urn:li:fsd_game:(<member>,6,<N>)   where gameTypeId 6 == Pinpoint.
We read it from there, or from a --meta / --number override.

Usage:
  python3 src/extract_pinpoint.py [cache/<date>/pinpoint_reveal.html]
                                 [--date ...]
                                 [--network cache/<date>/pinpoint_network.json]
                                 [--number N] [--meta cache/<date>/pinpoint_meta.json]
"""
import os, sys, json, argparse, re
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Pinpoint's voyager gameTypeId.
GAME_TYPE_ID = 6


def extract(path, number=None, network_path=None):
    dom = open(path, encoding="utf-8", errors="replace").read()
    from bs4 import BeautifulSoup
    s = BeautifulSoup(dom, "html.parser")

    # --- clues (locale-independent class selector) ---
    clue_els = s.select(".pinpoint__card--clue")
    clues = []
    for el in clue_els:
        txt = " ".join(el.get_text(" ", strip=True).split())
        if txt:
            clues.append(txt)
    # stable order is DOM order (pista 1..5) -- already in document order.

    # --- revealed answer / category ---
    ans_el = s.select_one(".pinpoint__card__answer_text")
    answer = " ".join(ans_el.get_text(" ", strip=True).split()) if ans_el else None

    # --- blank count ---
    bottom = s.select_one(".pinpoint__bottom-section")
    blanks = None
    if bottom:
        btxt = bottom.get_text(" ", strip=True)
        # each blank is a standalone '_' separated by spaces
        blanks = len([c for c in btxt.split() if set(c) == {"_"}])
        if blanks == 0:
            blanks = btxt.count("_")

    # --- number from network JSON if not already provided ---
    if number is None and network_path and os.path.exists(network_path):
        number = _number_from_network(network_path)

    return {
        "game": "pinpoint",
        "number": number,
        "answer": answer,
        "blanks": blanks,
        "clues": clues,
    }


def _number_from_network(network_path):
    """Parse 'urn:li:fsd_game:(<member>,6,<N>)' from the voyager responses."""
    try:
        hits = json.load(open(network_path))
    except Exception:
        return None
    pat = re.compile(r"fsd_game:\([^)]*,\s*%d\s*,\s*(\d+)\)" % GAME_TYPE_ID)
    for hit in hits:
        body = hit.get("body", "") if isinstance(hit, dict) else ""
        m = pat.search(body)
        if m:
            return int(m.group(1))
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=None)
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--network", default=None,
                    help="path to pinpoint_network.json (for the puzzle number)")
    ap.add_argument("--number", type=int, default=None,
                    help="puzzle number override (else read from --network/--meta)")
    ap.add_argument("--meta", default=None,
                    help="path to a *_meta.json with {\"number\": N} (optional)")
    args = ap.parse_args()

    path = args.path or os.path.join(ROOT, "cache", args.date,
                                     "pinpoint_reveal.html")
    network = args.network or os.path.join(ROOT, "cache", args.date,
                                           "pinpoint_network.json")
    number = args.number
    if number is None and args.meta and os.path.exists(args.meta):
        try:
            number = json.load(open(args.meta)).get("number")
        except Exception:
            pass

    data = extract(path, number, network)
    data["date"] = args.date

    out = os.path.join(ROOT, "outputs", args.date, "pinpoint.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(data, open(out, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {out}")
    print(f"clues={len(data['clues'])} blanks={data['blanks']} "
          f"number={data['number']} answer={data['answer']!r}")


if __name__ == "__main__":
    main()
