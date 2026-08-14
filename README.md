# LinkedIn Games Extractor
Capture the daily **LinkedIn Games** puzzles into per-day JSON files so they
can be inspected or replicated offline. All **eight** games are implemented and
captured with **Playwright**.
- Games: `zip`, `tango`, `queens`, `minisudoku`, `patches`, `wend`,
  `pinpoint`, `crossclimb`
- Output: `outputs/<YYYY-MM-DD>/<game>.json`, one file per game per day.

## Developer docs
See [`AGENTS.md`](./AGENTS.md) for the full architecture, the CI pipeline, the
local Telegram-posting cron, conventions, how to use, and how to add a new game.

<!-- DAILY-GAMES-START -->
## Today's games (2026-08-14)

### zip
```
+----+----+----+----+----+----+----+
| 13   ..   ..   ..   ..   ..    1 |
+                                  +
| ..    2   .. | ..   ..    8   .. |
+              +----               +
| ..   ..    3   ..    7   ..   .. |
+                         ----     +
| ..   .. | ..    6   .. | ..   .. |
+     ----+              +         +
| ..   ..    4   ..    5   ..   .. |
+               ----               +
| ..   12   ..   .. | ..   10   .. |
+                   +              +
| 11   ..   ..   ..   ..   ..    9 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . | . | . = . | . |
+---+---+---+---+---+-=-+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+-=-+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+-x-+
| M | M | S | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬛⬛⬛⬛⬛⬛⬛
⬜⬛⬛⬛🟧⬛⬛⬛⬛
⬜⬛🟥🟧🟧🟧🟫⬛⬛
⬜🟥🟥🟥🟧🟫🟫🟨⬛
⬜⬜🟥🟪🟪🟫🟨🟨🟨
⬜⬜⬜🟦🟪🟪🟩🟨⬜
⬜⬜🟦🟦🟦🟩🟩🟩⬜
⬜⬜⬜🟦⬜⬜🟩⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃ 2 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │ 4 ┃   │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | -3 | .. |
+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+
| .. | .. | -4 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+----+
| .. | -6 | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| A | # | O | C | # | # |
+---+---+---+---+---+---+
| E | N | R | R | I | M |
+---+---+---+---+---+---+
| I | N | T | E | O | D |
+---+---+---+---+---+---+
| O | H | T | W | O | F |
+---+---+---+---+---+---+
| U | S | A | E | I | G |
+---+---+---+---+---+---+
| # | # | N | D | # | H |
+---+---+---+---+---+---+

Words:
  FOOD
  WEIGH
  CORNEA
  INTERIM
  THOUSAND
```

### pinpoint
```
  1. Odyssey
  2. Galaxy
  3. Kart
  4. 64
  5. Bros. 3

  answer: Terms that come after “Super Mario” in video game titles!
```

### crossclimb
```
game      : crossclimb
number    : 836
date      : 2026-08-14
difficulty: None

Ladder (word : clue, top -> bottom):
  gasp : The top + bottom rows = Two words meaning to breathe quickly and loudly.
  wasp : Outdoor pest that has a powerful sting
  warp : Become misshapen, often under heat
  carp : To complain, or a type of fish like koi
  cart : Vehicle used for hauling
  part : Component of a larger whole
  pant : The top + bottom rows = Two words meaning to breathe quickly and loudly.
```
<!-- DAILY-GAMES-END -->
