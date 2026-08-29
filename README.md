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
## Today's games (2026-08-29)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    9   ..    1    3   ..   .. |
+                                  +
| 10   ..   ..   ..   ..    4   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    5   ..   ..   ..   ..    2 |
+                                  +
| ..   ..    6    7   ..    8   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-x-+-=-+-=-+-x-+-x-+-x-+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . x . | . = . |
+---+---+---+---+---+---+
| S | M | S | M | M | S |
+---+---+---+---+---+---+
```

### queens
```
🟨🟨🟨🟨🟥🟪🟪🟫🟫
🟨🟨🟨🟥🟥🟥🟪🟪🟫
🟨🟨🟧🟧🟧🟧🟧🟪🟫
🟨🟨🟨🟦🟦🟦🟫🟫🟫
🟨🟩🟩🟩🟦🟫🟫⬜⬜
🟩🟩🟩🟩🟦🟫⬜⬜⬜
🟩🟩🟩🟩⬛🟫⬜⬜⬜
🟩🟩🟩🟩⬛🟫🟫⬜⬜
🟩🟩🟩⬛⬛⬛⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │ 5 │ 6 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │ 6 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 2 │ 4 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | |6 |
+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | +5 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -6 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| D | N | T | N | E | T | U |
+---+---+---+---+---+---+---+
| E | U | O | V | I | R | N |
+---+---+---+---+---+---+---+
| D | N | B | E | # | # | # |
+---+---+---+---+---+---+---+
| # | U | # | N | # | N | # |
+---+---+---+---+---+---+---+
| # | # | # | U | E | U | C |
+---+---+---+---+---+---+---+
| U | O | F | I | O | N | L |
+---+---+---+---+---+---+---+
| N | D | A | T | S | U | E |
+---+---+---+---+---+---+---+

Words:
  VENUE
  NUCLEUS
  NUTRIENT
  UNBOUNDED
  FOUNDATION
```

### pinpoint
```
  1. Tents
  2. Skiers
  3. Barber shops
  4. Olympic vaulters
  5. Flags (as attached here: 🏁)

  answer: All associated with poles!
```

### crossclimb
```
game      : crossclimb
number    : 851
date      : 2026-08-29
difficulty: None

Ladder (word : clue, top -> bottom):
  mile : The top + bottom rows = A two-word phrase for a running competition that might take about four minutes for elite athletes to complete. Keep in mind: The first word may be at the bottom.
  milk : Nutrient-rich drink produced by mammals
  mink : Relative of the weasel
  rink : Ice skating venue
  rank : Assign items an order based on their relative quality
  rack : Where Scrabble tiles may sit before they're played
  race : The top + bottom rows = A two-word phrase for a running competition that might take about four minutes for elite athletes to complete. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
