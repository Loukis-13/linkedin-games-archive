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
## Today's games (2026-08-09)

### zip
```
+----+----+----+----+----+----+----+
| ..   11 |  3    4   ..   ..   .. |
+         +                        +
| ..   .. | ..   ..   ..    1   .. |
+         +                        +
| ..   .. | .. | .. | ..    2   .. |
+         +    +    +              +
| ..   12   .. | .. | ..    6   .. |
+              +    +              +
| ..   10   .. | .. | .. | ..   .. |
+              +    +    +         +
| ..    9   ..   ..   .. | ..   .. |
+                        +         +
| ..   ..   ..    8    7 |  5   .. |
+---- ---- ---- ---- ----+---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | S | . | . | . |
+---+---+---+---+---+---+
| . | . | . x . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | S | S | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥⬜⬜⬜⬜⬜
🟧🟦🟦🟦🟦🟦🟦🟦⬜
🟧🟦🟧🟦🟪🟪🟪🟦⬜
🟧🟦🟧🟦🟦🟦🟪🟦🟦
🟧🟧🟧🟦🟪🟪🟪🟦🟫
🟦🟦🟨🟦🟦🟦🟩🟦🟫
⬛🟦🟨🟨🟦🟩🟩🟩🟫
⬛🟦🟦🟦🟦🟦🟦🟦🟫
⬛⬛⬛⬛⬛⬛🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | +8 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |  | .. | +3 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +2 | .. | +2 | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
| +8 | .. | .. | .. | +6 | .. | +6 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +3 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +3 | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| C | A | T | # | C | A | T |
+---+---+---+---+---+---+---+
| O | G | E | L | O | O | I |
+---+---+---+---+---+---+---+
| R | I | E | S | E | N | C |
+---+---+---+---+---+---+---+
| E | # | C | A | T | # | E |
+---+---+---+---+---+---+---+
| D | G | I | F | I | T | R |
+---+---+---+---+---+---+---+
| U | N | I | E | D | O | H |
+---+---+---+---+---+---+---+
| C | A | T | # | C | A | T |
+---+---+---+---+---+---+---+

Words:
  CATHODE
  LOCATION
  EDUCATING
  CATEGORIES
  CERTIFICATE
```

### pinpoint
```
  1. Strength
  2. Temperance
  3. The Moon
  4. The High Priestess
  5. Wheel of Fortune

  answer (5 blanks): Tarot cards from the Major Arcana!
```

### crossclimb
```
  train   
  brain   
  brawn   
  brown   
  crown   
  crows   
  cross   

Clues (middle rows):
  - Human organ that takes up only 2% of a body’s weight but uses about 20% of its energy
  - Cook until the color changes, as onions
  - Black birds that collectively form a “murder”
  - The top part of the head, or something one might put there
  - Muscular strength

Phrase (top+bottom): The top + bottom rows = A hyphenated word meaning to engage in different sporting activities to balance health and muscular development. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
