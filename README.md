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
## Today's games (2026-09-24)

### zip
```
+----+----+----+----+----+----+
| ..    5   ..   ..    4   .. |
+                             +
| ..    6   ..   ..    9   .. |
+                             +
| ..    1   ..   ..   10   .. |
+                             +
| ..    7   ..   ..    8   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
| ..    2   ..   ..    3   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
| . | S | S | . | . | . |
+---+---+---+---+-=-+---+
| . | S | . | . | . | . |
+---+---+---+---+-x-+---+
| . | M | . | . | . | . |
+---+---+---+---+-=-+---+
| . | S | . | . x . | . |
+---+---+---+-=-+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟩🟩🟨🟨🟨🟥
🟥🟧🟩🟩🟩🟩🟩🟨🟥
🟥🟧🟩🟩🟩🟩🟩🟨⬜
🟥🟥🟥🟩🟪🟩⬜⬜⬜
🟥🟫🟩🟩🟩🟩🟩⬛⬜
🟥🟫🟩🟩🟩🟩🟩⬛🟦
🟥🟫🟫🟫🟩🟩⬛⬛🟦
🟥🟥🟥🟥🟥🟥🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 2 │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃   │ 2 │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | |6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +10 | .. |
+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +7 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+----+
| .. | +12 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| Q | E | # | # | S | L |
+---+---+---+---+---+---+
| U | S | P | A | N | E |
+---+---+---+---+---+---+
| E | N | # | # | A | L |
+---+---+---+---+---+---+
| E | C | # | # | B | L |
+---+---+---+---+---+---+
| C | S | P | A | N | E |
+---+---+---+---+---+---+
| R | I | # | # | I | R |
+---+---+---+---+---+---+

Words:
  CRISP
  PANELS
  SEQUENCE
  BALLERINA
```

### pinpoint
```
  1. Iron
  2. Iron horse (old-style train)
  3. Sauna
  4. Pressure cooker
  5. Tea kettle (when whistling)

  answer: Things associated with steam!
```

### crossclimb
```
game      : crossclimb
number    : 877
date      : 2026-09-24
difficulty: None

Ladder (word : clue, top -> bottom):
  bona : The top + bottom rows = A two-word Latin phrase meaning "genuine" or "authentic." Keep in mind: The first word may be at the bottom.
  bone : Part of a skeleton
  bane : ___ of one's existence (nemesis)
  mane : Hair on a horse's neck
  made : Created
  fade : Gradually become invisible
  fide : The top + bottom rows = A two-word Latin phrase meaning "genuine" or "authentic." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
