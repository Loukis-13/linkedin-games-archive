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
## Today's games (2026-10-30)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..   .. | ..    1    4 |
+          ----+              +
| ..   ..   ..   ..    6   .. |
+                             +
|  3    2   ..   ..   ..   .. |
+               ----          +
| ..    5   .. | ..   ..   .. |
+              +              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . = . |
+---+---+---+---+-=-+---+
| M | S | . | . | . | . |
+---+---+---+---+-x-+---+
| . | S | . | . | . = . |
+---+---+---+---+-x-+---+
| S | M | . | . | . | . |
+---+---+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟧🟧⬛⬛
🟥🟨🟨🟧🟧⬛⬛⬛
🟨🟨🟧🟧⬛⬛⬛🟫
🟨🟧🟧⬛⬛⬛🟫🟫
🟨🟧⬛⬛⬛🟫🟫🟫
🟨⬛⬛⬛🟫🟫🟦🟦
⬛⬛⬛🟪🟪🟦🟦🟩
⬛⬛🟪🟪🟦🟦🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │ 2 ┃ 6 │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 3 ┃ 1 │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. | +4 |
+----+----+----+----+----+----+----+
| .. | -4 | .. | .. | |  | .. | .. |
+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -  | .. | -  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +3 |
+----+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+
| +6 | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| L | A | S | T | U | R |
+---+---+---+---+---+---+
| E | # | C | I | M | O |
+---+---+---+---+---+---+
| S | U | C | # | # | F |
+---+---+---+---+---+---+
| T | # | # | C | U | S |
+---+---+---+---+---+---+
| O | M | I | C | # | N |
+---+---+---+---+---+---+
| T | C | N | J | O | I |
+---+---+---+---+---+---+

Words:
  JOIN
  FORUM
  CUSTOM
  ELASTIC
  SUCCINCT
```

### pinpoint
```
  1. Wings
  2. House
  3. Pit
  4. Green room
  5. Stage (where the action is)

  answer: Parts of a theatre!
```

### crossclimb
```
game      : crossclimb
number    : 913
date      : 2026-10-30
difficulty: None

Ladder (word : clue, top -> bottom):
  deck : The top + bottom rows = A two-word phrase for a popular device for playing music in the 1980s. Keep in mind: The first word may be at the bottom.
  peck : Little kiss, as on the forehead
  pack : Get ready for a business trip
  pace : Average speed at which a runner runs
  pale : Definitely not bold, as a hue
  tale : Story often presented orally
  tape : The top + bottom rows = A two-word phrase for a popular device for playing music in the 1980s. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
