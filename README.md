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
## Today's games (2026-10-08)

### zip
```
+----+----+----+----+----+----+
| ..    2    3   ..   ..   .. |
+                             +
|  1   ..   ..   ..    6   .. |
+                             +
| ..   ..    9   ..   ..   .. |
+                             +
| ..   ..   ..   10   ..   .. |
+                             +
| ..    8   ..   ..   ..    4 |
+                             +
| ..   ..   ..    7    5   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | . | . | . = . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | M | M |
+---+---+---+---+---+---+
| M | M | . | . | . x . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | M | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟨🟨
🟩🟥🟧🟧🟧🟧🟧🟧
🟩🟥🟦🟦🟧🟧🟧🟧
🟩🟩🟦🟪🟪🟪🟧🟧
🟩🟩🟦🟦🟪🟪🟧🟧
🟩🟩🟩🟩🟪🟪🟪🟧
🟩🟩🟩🟩🟩🟩🟫🟧
⬛⬛🟩🟩🟩🟩🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 2 │   ┃   │ 1 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │ 5 │   ┃   │ 2 │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+
| .. | .. | |6 | .. | |5 | .. | .. |
+----+----+----+----+----+----+----+
| |  | .. | .. | |  | .. | .. | |  |
+----+----+----+----+----+----+----+
| .. | |6 | .. | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+
| .. | .. | |  | .. | |  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| B | A | T | T | E | # |
+---+---+---+---+---+---+
| E | # | # | C | N | D |
+---+---+---+---+---+---+
| T | # | # | I | M | O |
+---+---+---+---+---+---+
| W | H | E | # | # | N |
+---+---+---+---+---+---+
| E | E | R | # | # | O |
+---+---+---+---+---+---+
| # | N | B | E | R | G |
+---+---+---+---+---+---+

Words:
  HERB
  ATTEND
  BETWEEN
  ERGONOMIC
```

### pinpoint
```
  1. Code
  2. Circuit
  3. Ice
  4. Deal
  5. Tie (used to avoid a draw)

  answer: Words that come before “breaker”!
```

### crossclimb
```
game      : crossclimb
number    : 891
date      : 2026-10-08
difficulty: None

Ladder (word : clue, top -> bottom):
  mama : The top + bottom rows = Two of the very first words a baby might speak, or the people who might hear them.
  maya : Mesoamerican civilization known for its calendar and pyramids, as at Chichén Itzá
  mays : Months after Aprils
  pays : Puts the money up, as for a meal
  pars : Expected scores on a golf course
  para : Prefix before "phrase," "medic," or "chute"
  papa : The top + bottom rows = Two of the very first words a baby might speak, or the people who might hear them.
```
<!-- DAILY-GAMES-END -->
