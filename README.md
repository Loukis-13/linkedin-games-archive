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
## Today's games (2026-10-03)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   16   15   14    3    8    7   .. |
+                                       +
| ..    9   ..    1    2   ..    6   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   11   ..   ..   12   ..   .. |
+                                       +
| ..   ..   10   13    4    5   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | M | . | . | S | . |
+---+---+-=-+-x-+---+---+
| . | . x . | . x . | . |
+---+---+---+---+---+---+
| . | . x . | . = . | . |
+---+---+-=-+-x-+---+---+
| . | S | . | . | S | . |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟧🟧🟧
🟨🟨🟥🟨🟨🟩🟧🟩🟧
🟨🟨🟨🟨🟨🟩🟩🟩🟧
🟦🟨🟨🟨🟪🟪🟩🟪🟪
🟦🟫🟨🟫🟪🟪🟪🟪🟪
🟦🟫🟫🟫⬛🟪🟪🟪⬜
⬛⬛🟫⬛⬛⬛🟪⬜⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +7 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | |  | .. | +5 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | +7 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +5 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | # | # | # | D | V | A |
+---+---+---+---+---+---+---+
| # | # | A | A | R | K | R |
+---+---+---+---+---+---+---+
| # | G | M | E | E | T | S |
+---+---+---+---+---+---+---+
| C | N | I | I | X | A | E |
+---+---+---+---+---+---+---+
| O | A | Z | O | O | T | # |
+---+---+---+---+---+---+---+
| N | K | U | U | M | # | # |
+---+---+---+---+---+---+---+
| T | I | N | # | # | # | # |
+---+---+---+---+---+---+---+

Words:
  KAZOO
  ESTEEM
  TAXIING
  AARDVARK
  CONTINUUM
```

### pinpoint
```
  1. Ground
  2. Thread
  3. Sense
  4. Denominator
  5. Knowledge (most people know it!)

  answer: Words that come after “common”!
```

### crossclimb
```
game      : crossclimb
number    : 886
date      : 2026-10-03
difficulty: None

Ladder (word : clue, top -> bottom):
  ribs : The top + bottom rows = Bone-in meat items often served at a barbecue. Keep in mind: The first word may be at the bottom.
  rips : Damages, as a page in a book
  ripe : Ready to be picked, as fruit
  rope : Cord that may be climbed for exercise
  pope : Leo XIV, for one
  pore : Small skin opening
  pork : The top + bottom rows = Bone-in meat items often served at a barbecue. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
