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
## Today's games (2026-10-28)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..    1    8   .. |
+                                  +
|  2   12 | ..   ..   ..   ..   .. |
+         +                        +
| ..   .. | ..    9   10 | ..   .. |
+         +              +         +
| ..   .. | ..   ..   .. | ..   .. |
+         +              +         +
| ..   .. | 11    5   .. | ..   .. |
+         +              +         +
| ..   ..   ..   ..   .. |  7    6 |
+                        +         +
| ..    3    4   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | M | . | . | . | . |
+---+---+-=-+---+---+---+
| M | S | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+-x-+-=-+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟨🟩🟩
🟥🟥🟧🟧🟨🟨🟨
🟥🟥🟧🟧🟨🟦🟦
🟪🟧🟧🟧🟨🟨🟨
🟪🟫🟫🟧🟧🟧🟧
🟪🟪🟫🟫🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 4 ┃ 1 │ 6 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +5 | +  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +  | +3 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | A | D | O | # |
+---+---+---+---+---+
| O | C | T | H | G |
+---+---+---+---+---+
| V | N | E | F | I |
+---+---+---+---+---+
| A | S | P | R | E |
+---+---+---+---+---+
| # | E | X | E | # |
+---+---+---+---+---+

Words:
  FREIGHT
  AVOCADO
  EXPENSE
```

### pinpoint
```
  1. Grate
  2. Damper
  3. Mantel
  4. Hearth
  5. Chimney (to vent the smoke)

  answer: Parts of a fireplace!
```

### crossclimb
```
game      : crossclimb
number    : 911
date      : 2026-10-28
difficulty: None

Ladder (word : clue, top -> bottom):
  shot : The top + bottom rows = An attempt to score in soccer/football, and the target of that attempt. Keep in mind: The first word may be at the bottom.
  slot : Time ___ (when to book a meeting)
  blot : Blemish that ink often causes
  boot : Item of footwear worn in soccer/football
  boat : Something that floats and rhymes with "float"
  goat : Farm animal that bleats
  goal : The top + bottom rows = An attempt to score in soccer/football, and the target of that attempt. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
