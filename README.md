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
## Today's games (2026-09-03)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    3   ..    1   ..    2   .. |
+     ---- ---- ---- ---- ----     +
| ..   ..   ..   ..   ..   ..   .. |
+     ----                         +
| ..    6   ..    5   ..    4   .. |
+                         ----     +
| ..   ..   ..   ..   ..   ..   .. |
+     ---- ---- ---- ---- ----     +
| ..    7   ..    9   ..    8   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+-=-+-x-+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | S | M | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟨🟧🟧🟧🟩🟩🟩🟩
🟥🟨🟦🟧🟧🟩🟩🟩🟩
🟪🟨🟦🟧🟧🟧🟧🟧🟩
🟪🟪🟦🟧🟧🟧🟧🟧🟧
🟫🟪🟪🟪🟪🟧⬛🟧🟧
🟫🟫🟫🟫🟪⬜⬛🟧🟧
🟫🟫🟫🟫🟪⬜⬛🟧🟧
🟪🟪🟪🟪🟪⬜🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃ 1 │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │ 3 ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | -6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +8 | .. | .. | .. |
+----+----+----+----+----+----+----+
| =4 | .. | .. | .. | .. | .. | +3 |
+----+----+----+----+----+----+----+
| .. | +2 | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+
| +6 | .. | .. | .. | .. | .. | |3 |
+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -2 | .. | +3 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| N | E | O | N | # | N |
+---+---+---+---+---+---+
| T | X | M | A | # | I |
+---+---+---+---+---+---+
| U | E | N | N | # | R |
+---+---+---+---+---+---+
| R | # | N | N | I | V |
+---+---+---+---+---+---+
| O | # | E | L | C | A |
+---+---+---+---+---+---+
| N | # | N | I | A | N |
+---+---+---+---+---+---+

Words:
  NEXT
  LINEN
  NEURON
  NIRVANA
  CINNAMON
```

### pinpoint
```
  1. Make
  2. Wrong
  3. Right of
  4. Milky
  5. Look the other

  answer: Words that come before “way”!
```

### crossclimb
```
game      : crossclimb
number    : 856
date      : 2026-09-03
difficulty: None

Ladder (word : clue, top -> bottom):
  hall : The top + bottom rows = A two-word phrase for a municipal government building. Keep in mind: The first word may be at the bottom.
  hill : Raised bit of land that's smaller than a mountain
  till : Drawer that stores money in a cash register
  toll : You may pay it to go over a bridge
  tool : Screwdriver, chisel, or hammer
  toon : Colloquial term for an animated TV show
  town : The top + bottom rows = A two-word phrase for a municipal government building. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
