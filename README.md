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
## Today's games (2026-11-16)

### zip
```
+----+----+----+----+----+----+
|  4   ..   ..   ..   ..    9 |
+                             +
| .. |  1   ..   ..   10 | .. |
+    +----           ----+    +
| ..   .. | ..   .. | ..   .. |
+         +         +         +
| ..   .. |  2    3 | ..   .. |
+     ----+         +----     +
| .. |  6   ..   ..    7 | .. |
+    +                   +    +
|  5   ..   ..   ..   ..    8 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+-=-+
| S | M | M | . = . x . |
+---+---+---+---+---+---+
| . x . x . | M | S | S |
+-x-+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟧🟥🟥🟨🟨🟨
🟦🟦🟩🟥🟥🟨🟨
🟦🟦🟩🟪🟥🟥🟨
🟦🟦🟦🟪🟫🟥🟨
🟦🟦🟦🟪🟫🟥🟨
🟦🟦🟦🟦🟫🟥🟨
🟦🟦🟦🟦🟫🟥🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │ 6 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │ 3 ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃ 4 │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 2 │   │ 6 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +6 | =4 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +9 | .. |
+----+----+----+----+----+----+
| .. | .. | -2 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -3 | .. | .. |
+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |3 | +3 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| I | # | # | # | I |
+---+---+---+---+---+
| R | A | S | D | N |
+---+---+---+---+---+
| A | F | # | E | X |
+---+---+---+---+---+
| N | K | K | I | W |
+---+---+---+---+---+
| I | # | # | # | I |
+---+---+---+---+---+

Words:
  INK
  KIWI
  INDEX
  SAFARI
```

### pinpoint
```
  1. Foundation
  2. Concealer
  3. Blush
  4. Eyeliner
  5. Mascara

  answer: Types of makeup!
```

### crossclimb
```
game      : crossclimb
number    : 930
date      : 2026-11-16
difficulty: None

Ladder (word : clue, top -> bottom):
  help : The top + bottom rows = A compound word for a telephone service that provides assistance. Keep in mind: The first word may be at the bottom.
  held : Gripped in the hands
  meld : Fuse into one
  mild : Pleasant and not extreme, as weather
  mind : "My ___ is made up" ("I've decided")
  mine : Place for extracting valuable material from the earth
  line : The top + bottom rows = A compound word for a telephone service that provides assistance. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
