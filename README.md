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
## Today's games (2026-07-30)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| .. | ..   .. | ..   .. | ..   .. |
+    +         +         +         +
|  3 | ..   .. | ..   .. | ..   .. |
+    +----     +----     +----     +
| ..    1   ..   ..   ..    2   .. |
+     ----      ----      ----     +
| ..   .. | ..   .. | ..   .. |  4 |
+         +         +         +    +
| ..   .. | ..   .. | ..   .. | .. |
+         +         +         +    +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
| . | . | . | . | M | M |
+---+---+---+---+---+---+
| M | M | . | . | . = . |
+---+---+---+---+---+---+
| . x . | . | . | S | M |
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧🟧🟧
🟥🟥🟧🟧🟧🟧🟨🟨🟧
🟧🟧🟧🟩🟦🟦🟦🟨🟧
🟧🟧🟩🟩🟪🟦🟦🟧🟧
🟧🟧🟧🟪🟪🟪🟦🟧🟧
🟧🟧🟧🟧🟪🟫🟫🟧🟧
🟧🟧🟧🟧🟧🟫🟧⬛🟧
🟧🟧🟧⬜🟧🟧🟧⬛⬛
🟧🟧🟧⬜⬜🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 1 │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 3 │ 5 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | =4 | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | +9 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -3 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | -8 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +12 | .. | .. | .. | |2 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. | |8 | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | # | N | L | L | # |
+---+---+---+---+---+---+
| R | E | O | O | A | B |
+---+---+---+---+---+---+
| E | O | # | # | O | K |
+---+---+---+---+---+---+
| T | O | # | # | O | B |
+---+---+---+---+---+---+
| S | T | O | O | T | E |
+---+---+---+---+---+---+
| # | P | H | N | # | # |
+---+---+---+---+---+---+

Words:
  PHOTO
  STEREO
  BALLOON
  NOTEBOOK
```

### pinpoint
```
  1. Iron
  2. Wood
  3. Wedge
  4. Driver
  5. Putter

  answer (5 blanks): Types of golf club!
```

### crossclimb
```
  hard    
  herd    
  here    
  hire    
  dire    
  dare    
  ware    

Clues (middle rows):
  - Extremely serious, like some consequences
  - Large group of animals like cows or sheep
  - Employ for a job
  - Challenge someone to complete a task
  - In this location

Phrase (top+bottom): The top + bottom rows = A compound word for the physical components of a computer. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
