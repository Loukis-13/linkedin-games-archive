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
## Today's games (2026-09-07)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..    7 |
+     ---- ---- ---- ----     +
| .. |  9    1    3    4 | .. |
+    +                   +    +
| ..   ..   ..   ..    5 | .. |
+                        +    +
| ..   ..   ..    2   .. | .. |
+                        +    +
| ..   ..   ..    6   .. | .. |
+                        +    +
| ..   ..    8   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | S | S | M | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-=-+-=-+-=-+-=-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟧🟧🟧🟥🟥
🟥🟨🟧🟩🟧🟦🟥
🟥🟨🟨🟩🟦🟦🟥
🟥🟨🟨🟦🟦🟥🟥
🟥🟪🟪🟫🟫🟥🟥
🟪🟪🟪🟫🟫🟫🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │ 6 │   ┃   │ 1 │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │ 1 │   ┃   │ 6 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │ 6 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| |2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +10 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | -3 | .. | |  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | =  | .. | =4 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -2 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| S | U | C | X | E |
+---+---+---+---+---+
| # | G | E | E | # |
+---+---+---+---+---+
| # | A | # | D | # |
+---+---+---+---+---+
| # | R | F | L | # |
+---+---+---+---+---+
| P | O | H | A | T |
+---+---+---+---+---+

Words:
  HOP
  FLAT
  SUGAR
  EXCEED
```

### pinpoint
```
  1. Keycards
  2. Electric kettles / coffee makers
  3. Toiletries
  4. Continental breakfast
  5. Room service

  answer: Things associated with hotels!
```

### crossclimb
```
game      : crossclimb
number    : 860
date      : 2026-09-07
difficulty: None

Ladder (word : clue, top -> bottom):
  hide : Two antonyms that form the name of the children’s game “___-and-___” where one person is “it” and looks for the other players. Keep in mind: The first word may be at the bottom.
  side : One of eight in an octagon
  site : Page to visit on the internet
  sits : Uses a chair
  sets : Drops below the horizon, like the sun at the end of the day
  sees : Lays eyes upon
  seek : Two antonyms that form the name of the children’s game “___-and-___” where one person is “it” and looks for the other players. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
