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
## Today's games (2026-08-13)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    8   ..    7   ..    6    4   .. |
+          ---- ---- ---- ----          +
| ..    9 | ..   ..   ..   .. | ..   .. |
+         +     ---- ----     +         +
| ..   .. | ..   ..   ..   .. | ..   .. |
+         +          ---- ----+         +
| ..   .. | ..   .. | ..   ..   ..   .. |
+         +         +                   +
| ..   .. | ..   .. | ..   ..    2   .. |
+         +         +                   +
| ..   10    5   ..    3   ..    1   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| M | M | . | M | S | . |
+---+---+---+---+---+---+
| . | . x . | . | . x . |
+---+---+---+---+---+---+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | . | . | . x . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧🟧🟧
🟥🟨🟨🟧🟧🟧🟧🟧🟧
🟥🟥🟥🟧🟩🟩🟧🟧🟧
🟦🟦🟧🟧🟩🟩🟧🟧🟧
🟦🟧🟧🟧🟧🟧🟧🟧🟧
🟦🟧🟧🟧🟪🟧🟧🟫🟧
🟦🟧🟧🟪🟪🟧🟧🟫🟫
🟦🟧🟧🟪⬛🟧⬜⬜⬜
🟦🟧🟧⬛⬛🟧⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 2 │ 3 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │ 3 │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 2 │ 3 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 3 │ 4 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | |2 | .. | .. | |6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |2 | .. | .. | .. | |  |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | |8 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |10 | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| L | A | A | L | U | M |
+---+---+---+---+---+---+
| E | C | # | # | # | R |
+---+---+---+---+---+---+
| N | M | E | L | C | O |
+---+---+---+---+---+---+
| D | I | D | D | H | F |
+---+---+---+---+---+---+
| A | # | # | # | O | R |
+---+---+---+---+---+---+
| R | P | L | U | M | D |
+---+---+---+---+---+---+

Words:
  PLUM
  CHORD
  MIDDLE
  FORMULA
  CALENDAR
```

### pinpoint
```
  1. The Sun
  2. Dominoes
  3. Leopards
  4. Dalmations
  5. Ladybirds / ladybugs (🐞)

  answer: Things that have spots!
```

### crossclimb
```
game      : crossclimb
number    : 835
date      : 2026-08-13
difficulty: None

Ladder (word : clue, top -> bottom):
  time : The top + bottom rows = A compound word describing a type of membership that never needs to be renewed. Keep in mind: The first word may be at the bottom.
  tame : Domesticated, like a household pet
  same : “In the ___ boat” (sharing a difficult situation)
  sake : Japanese rice wine
  lake : A large body of water surrounded by land
  like : Thumbs-up response on social media
  life : The top + bottom rows = A compound word describing a type of membership that never needs to be renewed. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
