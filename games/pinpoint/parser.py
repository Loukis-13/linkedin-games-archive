#!/usr/bin/env python3
"""pinpoint parser -- HTML to JSON. Number is date-math (local anchor).
The reveal DOM is locale-independent (driven by pinpoint__ classes): clue
words -> .pinpoint__card--clue, category -> .pinpoint__card__answer_text,
blank count -> .pinpoint__bottom-section."""
from datetime import date
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 17)
_ANCHOR_NUM = 487


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    clue_els = soup.select(".pinpoint__card--clue")
    clues = []
    for el in clue_els:
        txt = " ".join(el.get_text(" ", strip=True).split())
        if txt:
            clues.append(txt)
    ans_el = soup.select_one(".pinpoint__card__answer_text")
    answer = " ".join(ans_el.get_text(" ", strip=True).split()) if ans_el else None
    bottom = soup.select_one(".pinpoint__bottom-section")
    blanks = None
    if bottom:
        btxt = bottom.get_text(" ", strip=True)
        blanks = len([c for c in btxt.split() if set(c) == {"_"}])
        if blanks == 0:
            blanks = btxt.count("_")
    data = {"game": "pinpoint", "number": number(), "date": date_str,
            "answer": answer, "blanks": blanks, "clues": clues}
    out = _c.write_json(date_str, "pinpoint", data)
    print(f"wrote {out}")
    return data
