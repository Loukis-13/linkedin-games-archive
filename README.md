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
## Today's games (2026-10-18)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| .. | ..   ..   ..   .. | ..    3   .. |
+    +                   +              +
| .. |  1   ..   .. |  2   .. | .. | .. |
+    +              +         +    +    +
| ..    4   .. |  5   ..   .. | ..   .. |
+              +              +         +
| ..   .. | ..   ..    8 | ..    7   .. |
+         +              +              +
| .. | .. | ..   10 | ..   ..    9 | .. |
+    +    +         +              +    +
| .. |  6   .. | ..   ..   ..   .. | .. |
+    +         +                   +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | M | M | . | . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . | . |
+---+---+---+---+-x-+---+
| . | . | . | . | . | . |
+---+-x-+---+---+-x-+---+
| . | . | . | . | . | . |
+---+-x-+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+---+---+---+---+
| . | . | . | S | M | M |
+---+---+---+---+---+---+
```

### queens
```
🟪🟪🟪🟪⬛⬛⬛⬛⬛
🟪⬜⬜⬜⬜🟫🟫🟫⬛
🟪⬜🟦🟦🟦🟦🟦🟫⬛
🟪⬜🟦🟦🟦🟦🟦🟫⬛
🟪🟨🟦🟦🟦🟦🟦🟫⬛
🟪🟨🟦🟦🟦🟦🟦🟫🟧
🟥🟨🟦🟦🟦🟦🟦🟩🟧
🟥🟨🟨🟦🟦🟦🟩🟩🟧
🟥🟥🟧🟧🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +2 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -  | +2 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | -  | =  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| |  | |  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | |  | |  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  | -  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +8 | -  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +5 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| W | E | L | L | K | S | T |
+---+---+---+---+---+---+---+
| D | N | K | O | R | T | A |
+---+---+---+---+---+---+---+
| T | O | # | W | # | I | K |
+---+---+---+---+---+---+---+
| U | Q | E | # | N | O | C |
+---+---+---+---+---+---+---+
| I | E | # | D | # | B | A |
+---+---+---+---+---+---+---+
| N | C | N | R | A | W | E |
+---+---+---+---+---+---+---+
| O | X | A | R | U | D | N |
+---+---+---+---+---+---+---+

Words:
  KNOT
  DWELL
  EQUINOX
  DRAWBACK
  ENDURANCE
  WORKSTATION
```

### pinpoint
```
  1. Mail
  2. Assignment
  3. Hang up
  4. Fence pole
  5. After/subsequent (as a prefix)

  answer: Different definitions of “post”!
```

### crossclimb
```
game      : crossclimb
number    : 901
date      : 2026-10-18
difficulty: None

Ladder (word : clue, top -> bottom):
  cries : The top + bottom rows = A two-word phrase for what a person sometimes does when receiving overwhelmingly good news. Keep in mind: The first word may be at the bottom.
  cribs : Baby beds
  crabs : Ten-legged creatures
  crams : Studies hard right before a test
  trams : Streetcars
  teams : Microsoft's video messaging app, or groups of coworkers it might bring together
  tears : The top + bottom rows = A two-word phrase for what a person sometimes does when receiving overwhelmingly good news. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
