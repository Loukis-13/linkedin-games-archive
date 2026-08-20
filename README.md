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
## Today's games (2026-08-20)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   ..    8    7   10   ..   .. |
+                                  +
| ..    9   ..   ..   ..    2   .. |
+               ----               +
| ..   12   .. | ..   ..    1   .. |
+              +                   +
| ..    6   ..   ..   ..   11   .. |
+                                  +
| ..   ..    5    4    3   ..   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . | . | . | M |
+-=-+-=-+---+---+---+---+
| . = . | . | . | M | . |
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . = . |
+---+---+---+---+-x-+-=-+
| M | . | . | . | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟥🟥🟪🟥🟥
🟥🟥🟧🟥🟥🟪🟪🟥🟥
🟥🟥🟥🟥🟥🟥🟪🟥🟥
⬜⬜⬜🟥🟥🟥🟥🟥🟥
🟥⬜🟥🟥🟥🟥🟥🟦🟥
🟥🟥🟥🟥🟨🟨🟦🟦🟦
🟥🟥🟫⬛⬛🟨🟨🟨🟨
🟥🟥🟫🟫⬛⬛🟩🟨🟨
🟥🟥🟫⬛⬛🟩🟩🟩🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 6 ┃ 1 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +  | +  | .. |
+----+----+----+----+----+----+----+
| .. | -  | +2 | .. | +4 | |  | .. |
+----+----+----+----+----+----+----+
| .. | +  | +  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | W | W | O | R | # |
+---+---+---+---+---+---+
| R | O | # | # | K | M |
+---+---+---+---+---+---+
| R | O | # | # | T | O |
+---+---+---+---+---+---+
| O | M | # | # | O | R |
+---+---+---+---+---+---+
| T | B | # | # | O | M |
+---+---+---+---+---+---+
| # | L | O | S | S | # |
+---+---+---+---+---+---+

Words:
  WORK
  MOTOR
  BLOSSOM
  TOMORROW
```

### pinpoint
```
  1. Nori
  2. Jerky
  3. Instant coffee
  4. Prunes
  5. Raisins

  answer: Food items that are dehydrated!
```

### crossclimb
```
game      : crossclimb
number    : 842
date      : 2026-08-20
difficulty: None

Ladder (word : clue, top -> bottom):
  case : The top + bottom rows = A compound word for what a detective or government employee takes on. Keep in mind: The first word may be at the bottom.
  cask : Large barrel-shaped container for wine or other liquids
  mask : What a superhero wears to protect their other identity
  mark : “You're way off the ___” (far from accurate)
  park : Grassy area for public enjoyment
  pork : Type of meat served at a pig roast
  work : The top + bottom rows = A compound word for what a detective or government employee takes on. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
