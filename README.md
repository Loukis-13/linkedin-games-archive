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
## Today's games (2026-10-17)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   16    4   ..   ..    3    2 |
+                                  +
| ..   15   14   ..   ..   13    1 |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
|  8    7   ..   ..    5   12   .. |
+                                  +
|  9    6   ..   ..   10   11   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | S | M | S |
+---+---+---+---+---+---+
| . | . | . | . | M | M |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-x-+---+---+---+---+---+
| . = . | . | . | . | . |
+-=-+-x-+---+---+---+---+
| . x . = . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟧🟧🟧🟥🟥🟥🟥🟥🟥
🟧🟧🟨🟥🟥🟥🟥🟥🟥
🟨🟨🟨🟩🟩🟩🟥🟥🟥
⬜⬜⬜🟩🟦🟩🟫🟪🟪
⬜⬜⬜🟩🟦🟦🟫🟫🟪
⬜⬜⬜⬜⬜⬜🟫🟪🟪
⬜⬜⬛⬛⬜⬜⬜⬜⬜
⬜⬛⬛⬜⬜⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │ 1 ┃ 4 │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +2 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| L | A | W | A | R | E | T |
+---+---+---+---+---+---+---+
| L | # | F | L | L | L | I |
+---+---+---+---+---+---+---+
| L | # | U | L | O | G | I |
+---+---+---+---+---+---+---+
| I | # | # | L | # | T | S |
+---+---+---+---+---+---+---+
| F | D | N | A | # | I | C |
+---+---+---+---+---+---+---+
| L | # | L | A | # | # | A |
+---+---+---+---+---+---+---+
| U | L | L | C | O | L | L |
+---+---+---+---+---+---+---+

Words:
  LULL
  LOCAL
  LAWFUL
  LITERAL
  LANDFILL
  LOGISTICAL
```

### pinpoint
```
  1. Defibrillator
  2. Steamboat
  3. Canoe
  4. Atari 2600 (to play some Pong?)
  5. Table tennis (to hit the ball!)

  answer: Things with paddles!
```

### crossclimb
```
game      : crossclimb
number    : 900
date      : 2026-10-17
difficulty: None

Ladder (word : clue, top -> bottom):
  song : The top + bottom rows = A compound word for a volume that holds lots of lyrics. Keep in mind: The first word may be at the bottom.
  gong : Percussion instrument resembling a very large cymbal
  gone : Missing
  cone : Alternative to a cup in an ice cream parlor
  conk : ___ out (break down or fall asleep)
  cook : Their job might require an apron
  book : The top + bottom rows = A compound word for a volume that holds lots of lyrics. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
