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
## Today's games (2026-11-23)

### zip
```
+----+----+----+----+----+----+
|  1   ..   .. | ..   ..    4 |
+              +              +
|  2   .. | .. | ..   ..    5 |
+         +    +              +
| ..   .. | ..   .. | ..   .. |
+         +         +         +
| ..   .. | ..   .. | ..   .. |
+         +         +         +
|  3   ..   .. | .. | ..    6 |
+              +    +         +
|  8   ..   .. | ..   ..    7 |
+---- ---- ----+---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+-=-+---+---+---+
| . | . = . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+-x-+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | S | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟥🟨🟥🟥🟥🟥
🟥🟧🟧🟨🟨🟥🟥🟥
🟥🟥🟩🟩🟥🟥🟥🟥
🟥🟥🟥🟩🟦🟥🟪🟥
🟥🟥🟥🟦🟦🟪🟪🟥
🟫🟥🟥🟥⬛⬛🟥🟥
🟫🟫🟥🟥⬛🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 5 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃ 1 │ 3 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 3 ┃ 4 │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │ 5 │ 1 ┃ 2 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| -2 | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+
| .. | |2 | .. | .. | =  | .. |
+----+----+----+----+----+----+
| .. | .. | |2 | |2 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |3 | |3 | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | |3 | .. |
+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | |3 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| U | O | A | D | E |
+---+---+---+---+---+
| B | D | # | D | R |
+---+---+---+---+---+
| L | # | # | # | O |
+---+---+---+---+---+
| E | M | # | E | M |
+---+---+---+---+---+
| # | E | R | G | # |
+---+---+---+---+---+

Words:
  ADD
  MORE
  MERGE
  DOUBLE
```

### pinpoint
```
  1. Rail
  2. Swift
  3. Quail
  4. Owl
  5. Eagle

  answer: Types of birds!
```

### crossclimb
```
game      : crossclimb
number    : 937
date      : 2026-11-23
difficulty: None

Ladder (word : clue, top -> bottom):
  hand : The top + bottom rows = What the 👋 emoji depicts, and the gesture it represents. Keep in mind: The first word may be at the bottom.
  land : Touch down, as a plane
  lane : Division of a wide roadway
  lake : Body of water such as Erie, Victoria, or Ladoga
  sake : "Oh, for goodness' ___!"
  save : Success for a goalkeeper
  wave : The top + bottom rows = What the 👋 emoji depicts, and the gesture it represents. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
