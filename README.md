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
## Today's games (2026-08-11)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    3    1    2 |
+                             +
| ..   ..    9   ..   ..   .. |
+                             +
| ..   10   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..    6   .. |
+                             +
| ..   ..   ..    7   ..   .. |
+                             +
|  4    5    8   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+-=-+---+---+
| M | M | . = . | . | . |
+---+---+---+-x-+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | M | . | . | . |
+---+---+---+---+---+-x-+
| . | . | M | M | . = . |
+---+---+---+---+---+-=-+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟨🟨
🟥🟧🟧🟧🟧🟧🟨
🟥🟧🟧🟧🟧🟧🟨
🟥🟩🟥🟦🟨🟨🟨
🟥🟥🟥🟦🟨🟨🟨
🟥🟥🟥🟦🟨🟨🟪
🟥🟥🟫🟫🟫🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │ 6 │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃ 5 │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 4 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │ 3 │ 6 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +5 | .. | .. | +4 | .. | +3 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +8 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +10 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| -  | .. | -  | .. | .. | -  |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| U | E | E | Z | E |
+---+---+---+---+---+
| Q | S | # | # | Y |
+---+---+---+---+---+
| U | S | # | S | K |
+---+---+---+---+---+
| R | # | # | S | I |
+---+---+---+---+---+
| E | E | L | P | M |
+---+---+---+---+---+

Words:
  SKY
  SURE
  SIMPLE
  SQUEEZE
```

### pinpoint
```
  1. Wedge
  2. Lever
  3. Pulley
  4. Inclined plane
  5. Wheel and axle

  answer (5 blanks): Types of simple machine!
```

### crossclimb
```
game      : crossclimb
number    : 833
date      : 2026-08-11
difficulty: None
Ladder (word : clue, top -> bottom):
  camp : The top + bottom rows = A compound word for where you might pitch a tent. Keep in mind: The first word may be at the bottom.
  came : Showed up, as to a party
  game : Word after "word," "board," or "video"
  gate : Entryway in a fence
  kate : Diminutive name for "Catherine" used by the Princess of Wales (___ Middleton)
  kite : Toy on a string that’s brought out on a windy day
  site : The top + bottom rows = A compound word for where you might pitch a tent. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
