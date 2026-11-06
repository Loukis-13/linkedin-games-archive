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
## Today's games (2026-11-06)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..    7 |
+                                  +
| ..   ..   ..   ..    5    6   .. |
+                                  +
| ..   ..   12   ..   ..   ..   .. |
+                                  +
|  8    4   ..   ..   ..    1   11 |
+                                  +
| ..   ..   ..   ..    3   ..   .. |
+                                  +
| ..    9    2   ..   ..   ..   .. |
+                                  +
| 10   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | S | S | . x . x . |
+-x-+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| M | . | . | . | . | S |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+-x-+
| . x . x . | M | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟪🟪🟪🟪🟦🟦🟦🟦
🟪🟪🟫🟪🟦🟨🟨🟨
🟪🟪🟫🟫🟦🟨🟩🟩
🟪🟧🟥🟥🟥🟨🟨🟩
🟪🟧🟥🟧🟥🟩🟩🟩
🟪🟧🟧🟧🟥🟪🟪⬛
🟪🟪🟪🟪🟪🟪🟪⬛
🟪🟪🟪🟪🟪🟪⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃   │   │ 6 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| |6 | .. | -6 | .. | .. | .. | |6 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | +3 | .. | +2 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| E | E | E | N | S | I |
+---+---+---+---+---+---+
| # | T | T | # | G | L |
+---+---+---+---+---+---+
| I | N | U | # | O | O |
+---+---+---+---+---+---+
| O | A | # | D | W | D |
+---+---+---+---+---+---+
| P | P | # | I | I | # |
+---+---+---+---+---+---+
| E | T | U | L | L | L |
+---+---+---+---+---+---+

Words:
  DILUTE
  UTENSIL
  GOODWILL
  APPOINTEE
```

### pinpoint
```
  1. Argument
  2. Street
  3. Vinyl record
  4. Sheet of paper
  5. Coin (heads and tails)

  answer: Things that have two sides!
```

### crossclimb
```
game      : crossclimb
number    : 920
date      : 2026-11-06
difficulty: None

Ladder (word : clue, top -> bottom):
  wood : The top + bottom rows = A two-word phrase for what someone working in forestry might do with an axe. Keep in mind: The first word may be at the bottom.
  hood : It's attached to some jackets
  hoot : Sound an owl makes
  soot : Black stuff in a chimney
  shot : Opportunity
  shop : Place to make a purchase
  chop : The top + bottom rows = A two-word phrase for what someone working in forestry might do with an axe. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
