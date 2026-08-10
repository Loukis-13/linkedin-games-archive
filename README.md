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
## Today's games (2026-08-10)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    1   ..   .. |
+     ----      ---- ----     +
| .. |  4   .. | ..   .. | .. |
+    +         +         +    +
| .. | .. | ..   ..   .. | .. |
+    +    +              +    +
| .. | ..   ..   .. | .. | .. |
+    +              +    +    +
| .. | ..   .. | ..    3 | .. |
+    +---- ----+     ----+    +
| ..   ..    2   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . x . | . = . |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+---+---+---+---+
| . | S | . | . | S | . |
+-=-+---+---+---+---+-x-+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . = . | . = . | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟪🟧🟧🟧🟩🟦🟦
🟪🟧🟨🟧🟨🟦🟦
🟪🟧🟨🟧🟨🟨🟦
🟪🟥🟨🟨🟨🟦🟦
🟪🟪🟨🟪🟨🟫🟫
🟪🟨🟨🟪🟨🟨🟫
🟪🟪🟪🟪🟪🟪🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 3 │   ┃   │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃ 5 │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃ 1 │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │ 6 │ 4 ┃ 3 │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 6 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +2 | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |5 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |8 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | +6 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | L | # | R | # |
+---+---+---+---+---+
| # | L | # | R | # |
+---+---+---+---+---+
| Y | A | # | U | W |
+---+---+---+---+---+
| E | U | P | P | O |
+---+---+---+---+---+
| L | L | A | R | R |
+---+---+---+---+---+

Words:
  ALL
  PURR
  ARROW
  PULLEY
```

### pinpoint
```
  1. Brick
  2. Maroon
  3. Tomato
  4. Scarlet
  5. Cherry

  answer (5 blanks): Shades of red!
```

### crossclimb
```
game      : crossclimb
number    : 832
date      : 2026-08-10
difficulty: None
Ladder (word : clue, top -> bottom):
  book : The top + bottom rows = A compound word for where a student might write down info for their classes. Keep in mind: The first word may be at the bottom.
  hook : Curved item at the end of a fishing line
  hoot : Make a sound like an owl
  host : Emcee of a television show
  hose : Attachment to a fire hydrant
  nose : Where eyeglasses might rest
  note : The top + bottom rows = A compound word for where a student might write down info for their classes. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
