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
## Today's games (2026-10-22)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| 11    9   ..   ..    4   12 |
+                             +
| ..   10   ..   ..   ..    5 |
+                             +
|  8   ..   ..   ..    3   .. |
+                             +
|  7    1   ..   ..    2    6 |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | M | . | M |
+---+---+---+---+---+---+
| . | . | . | M | . | S |
+---+---+---+---+---+---+
| . | . | . | S | M | M |
+---+---+---+---+---+---+
| . x . = . | . | . | . |
+-=-+---+-=-+---+---+---+
| . | . | . | . | . | . |
+-x-+---+-x-+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟧🟧🟧🟥
🟥🟨🟨🟨🟩🟩🟧🟧
🟥🟥🟨🟨🟦🟧🟧🟧
🟪🟪🟫🟨🟦🟦🟧🟧
🟪🟫🟫🟫🟦🟦🟦🟪
🟪🟪⬛⬛⬛⬛⬛🟪
🟪🟪🟪🟪🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 3 ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃ 2 │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | |6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | .. | |6 |
+----+----+----+----+----+----+----+
| .. | .. | .. | |5 | .. | .. | .. |
+----+----+----+----+----+----+----+
| |6 | .. | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | # | P | M | O | C |
+---+---+---+---+---+---+
| # | # | I | L | R | Y |
+---+---+---+---+---+---+
| # | P | R | E | D | # |
+---+---+---+---+---+---+
| # | P | O | E | D | # |
+---+---+---+---+---+---+
| S | O | E | F | # | # |
+---+---+---+---+---+---+
| A | L | N | D | # | # |
+---+---+---+---+---+---+

Words:
  DRY
  DEFEND
  COMPILE
  PROPOSAL
```

### pinpoint
```
  1. Game
  2. Poker
  3. Baby
  4. Clock
  5. Smiley (😊)

  answer: Types of “face”!
```

### crossclimb
```
game      : crossclimb
number    : 905
date      : 2026-10-22
difficulty: None

Ladder (word : clue, top -> bottom):
  worm : The top + bottom rows = A compound word for a wriggly creature that many birds eat. Keep in mind: The first word may be at the bottom.
  work : What you might do from home or in an office
  pork : Pig meat
  perk : Part of an incentive package
  peak : Top of a mountain
  peal : Ring, like a bell
  meal : The top + bottom rows = A compound word for a wriggly creature that many birds eat. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
