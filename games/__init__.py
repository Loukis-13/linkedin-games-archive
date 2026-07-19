#!/usr/bin/env python3
"""Per-game LinkedIn Games extractor package.

Layout: games/<game>/{scraper,parser,renderer}.py
  - scraper.capture(page, date_str, save_html=False) -> html (str) or game data
  - parser.parse(date_str, raw) -> dict (writes outputs/<date>/<game>.json)
  - renderer.render(date_str) -> list[str]

Dispatch tables for the root extract.py / render.py tools.
"""
import importlib

GAMES = ("zip", "tango", "queens", "minisudoku",
         "patches", "wend", "pinpoint", "crossclimb")


def _mod(game, kind):
    return importlib.import_module(f"games.{game}.{kind}")


def scraper(game):
    return _mod(game, "scraper")


def parser(game):
    return _mod(game, "parser")


def renderer(game):
    return _mod(game, "renderer")
