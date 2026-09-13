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
## Today's games (2026-09-13)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+               ----               +
| ..    7   .. |  8 | ..    5   .. |
+              +    +              +
| ..   ..   ..   ..    4   ..   .. |
+          ----      ----          +
| ..   ..   ..   ..   ..   ..   .. |
+          ----      ----          +
| ..   ..    3   ..   ..   ..   .. |
+                                  +
| ..    2   .. |  1 | ..    6   .. |
+              +----+              +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-=-+---+---+-x-+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . x . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | M | S |
+---+---+---+---+---+---+
| . | . | . | . | S | S |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟦🟦🟨🟨🟨🟦
🟦🟥🟦🟥🟦🟨🟦🟨🟦
🟦🟥🟥🟥🟦🟦🟦🟦🟦
🟦🟦🟦🟧🟧🟧⬛⬛🟦
🟦🟦🟦🟧🟩🟧🟩⬛🟦
🟦⬜🟦⬜🟩🟩🟩⬛⬛
🟦⬜⬜⬜🟫🟫🟫⬛⬛
🟦🟦🟦🟦🟫🟪🟫🟪⬛
🟦🟦🟦🟦🟦🟪🟪🟪⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +8 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | +5 | +6 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +3 | +4 | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| I | D | P | T | P | B | O |
+---+---+---+---+---+---+---+
| S | R | U | # | U | C | A |
+---+---+---+---+---+---+---+
| O | P | # | P | # | D | R |
+---+---+---+---+---+---+---+
| P | # | P | U | P | # | P |
+---+---+---+---+---+---+---+
| U | O | U | # | P | M | U |
+---+---+---+---+---+---+---+
| L | R | G | N | E | P | R |
+---+---+---+---+---+---+---+
| A | T | I | O | T | E | E |
+---+---+---+---+---+---+---+

Words:
  PUMP
  GROUP
  DISRUPT
  CUPBOARD
  PUPPETEER
  POPULATION
```

### pinpoint
```
  1. Factory
  2. Inside agent
  3. Introduce subtly, as an idea
  4. Tree or shrub
  5. Put seeds in the ground

  answer: Different definitions of “plant”!
```

### crossclimb
```
game      : crossclimb
number    : 866
date      : 2026-09-13
difficulty: None

Ladder (word : clue, top -> bottom):
  house : The top + bottom rows = A place to live, and a piece of furniture often found in it. Keep in mind: The first word may be at the bottom.
  rouse : Awaken, or stir to action
  rouge : Cosmetics purchase for the cheeks
  rough : ___ and tumble (turbulent)
  tough : Hard to chew, like low-quality meat
  touch : Affect one's heartstrings
  couch : The top + bottom rows = A place to live, and a piece of furniture often found in it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
