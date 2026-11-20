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
## Today's games (2026-11-20)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ----      ----      ----     +
| ..   10    3   ..    2    1   .. |
+                                  +
| ..   ..   ..    4   ..   ..   .. |
+          ----      ----          +
| ..   ..   ..    5   ..   ..   .. |
+          ----      ----          +
| ..   ..   ..    8   ..   ..   .. |
+                                  +
| ..    6    7   ..    9   11   .. |
+     ----      ----      ----     +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | . = . | M | . |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+-=-+---+-=-+-x-+---+-x-+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | S | . = . | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟨🟨🟨🟨🟨🟨🟨🟨⬜
🟨🟨🟨🟪🟪🟪🟪⬜⬜
🟨🟨🟫🟪🟩🟩🟩🟩⬜
⬛⬛🟫🟧🟧🟧🟧🟩⬜
⬛🟫🟫🟧🟦🟧🟩🟩⬜
⬛🟫🟧🟧🟧🟧🟩⬛⬜
⬛🟫🟫🟫🟥🟩🟩⬛⬜
⬛⬛🟥🟥🟥🟩⬛⬛⬜
⬛⬛⬛⬛⬛⬛⬛⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │ 3 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │ 5 ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃ 1 │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 5 │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 4 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | .. | |  |
+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | .. | +2 |
+----+----+----+----+----+----+----+
| .. | =4 | .. | =  | .. | |3 | .. |
+----+----+----+----+----+----+----+
| +5 | .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+----+
| -  | .. | -  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +5 | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | # | # | G | L | I | C |
+---+---+---+---+---+---+---+
| # | A | C | A | R | L | E |
+---+---+---+---+---+---+---+
| # | L | I | E | # | B | I |
+---+---+---+---+---+---+---+
| # | G | # | R | # | N | G |
+---+---+---+---+---+---+---+
| # | # | # | D | # | E | I |
+---+---+---+---+---+---+---+
| T | A | N | E | # | G | L |
+---+---+---+---+---+---+---+
| N | E | G | L | # | # | # |
+---+---+---+---+---+---+---+

Words:
  GARLIC
  GLACIER
  ENTANGLED
  NEGLIGIBLE
```

### pinpoint
```
  1. Tan
  2. Cot
  3. Sin
  4. Sec
  5. Cos (short for cosine)

  answer: Abbreviations of trigonometry functions!
```

### crossclimb
```
game      : crossclimb
number    : 934
date      : 2026-11-20
difficulty: None

Ladder (word : clue, top -> bottom):
  turn : The top + bottom rows = A two-word phrase for a friendly deed, as in the expression "one ___ ___ deserves another." Keep in mind: The first word may be at the bottom.
  torn : Troubled by a dilemma
  born : Introduced to the world
  boon : Hugely beneficial thing
  moon : It's full usually once a month, but occasionally twice
  mood : How someone is feeling at the moment
  good : The top + bottom rows = A two-word phrase for a friendly deed, as in the expression "one ___ ___ deserves another." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
