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
## Today's games (2026-10-07)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..    1    3    5    8   .. |
+                             +
| ..    2    4    6    7   .. |
+                             +
| ..   ..   .. | ..   ..   .. |
+     ---- ----+---- ----     +
| ..   ..   .. | ..   ..   .. |
+              +              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | . = . | M | . |
+---+---+---+---+---+---+
| S | . = . | S | . | . |
+---+-x-+---+---+---+---+
| . | . | M | . | . | . |
+-=-+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧🟧🟧
🟨🟨🟥🟧🟧🟧🟧🟧🟧
🟨🟩🟦🟦🟦🟦🟧🟧🟧
🟩🟩🟪🟪🟪🟦🟫🟫🟫
🟩🟪🟪🟪🟦🟦⬛⬛🟫
🟪🟪🟪🟦🟦⬛⬛⬜🟪
🟪🟪🟪🟦🟪⬛⬜⬜🟪
🟪🟪🟪🟪🟪🟪⬜🟪🟪
🟪🟪🟪🟪🟪🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 3 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 4 │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃   │ 3 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| |  | |  | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | =  | |  | |  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +9 | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +4 | +4 | +7 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | # | R | # | E |
+---+---+---+---+---+
| G | U | O | L | L |
+---+---+---+---+---+
| R | D | O | E | H |
+---+---+---+---+---+
| I | G | A | Z | I |
+---+---+---+---+---+
| A | H | # | H | G |
+---+---+---+---+---+

Words:
  HIGH
  ROUGH
  HAIRDO
  GAZELLE
```

### pinpoint
```
  1. A+
  2. B-
  3. AB+
  4. O+ (the most common)
  5. O- (universal red cell donor)

  answer: Blood types!
```

### crossclimb
```
game      : crossclimb
number    : 890
date      : 2026-10-07
difficulty: None

Ladder (word : clue, top -> bottom):
  mark : The top + bottom rows = A two-word phrase meaning to discount, as a product for sale. Keep in mind: The first word may be at the bottom.
  bark : Sound that might come after you say "Who's a good dog? Is it you?"
  barn : Where a calf may be raised on a farm
  born : Brought into the world
  morn : Early part of the day, poetically
  mown : Like a well-trimmed yard
  down : The top + bottom rows = A two-word phrase meaning to discount, as a product for sale. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
