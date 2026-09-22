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
## Today's games (2026-09-22)

### zip
```
+----+----+----+----+----+----+
| ..   .. | ..   ..   ..   .. |
+         +                   +
| ..    1 | ..   ..    5   .. |
+         +                   +
| ..    3   ..   .. |  6   .. |
+                   +         +
| ..    2 | ..   ..    8   .. |
+         +                   +
| ..    4   ..   .. |  7   .. |
+                   +         +
| ..   ..   ..   .. | ..   .. |
+---- ---- ---- ----+---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | M | S | S | . |
+---+---+---+---+---+---+
| . | . x . | . | . | . |
+---+-=-+---+---+-x-+---+
| . | . | . | . x . | . |
+---+---+---+---+---+---+
| . | M | S | S | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛⬛⬛⬛⬛🟦
🟦🟦🟦🟨🟨🟦🟦🟦
🟦🟦🟦🟨🟨🟪🟪🟦
🟧🟧🟧🟨🟥🟪🟪🟦
🟧🟧🟧🟨🟥🟦🟦🟦
🟫🟫🟫🟨🟦🟦🟦🟦
🟩🟦🟦🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │ 4 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +9 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | R | E | R | E |
+---+---+---+---+---+
| T | U | T | A | T |
+---+---+---+---+---+
| X | # | I | # | R |
+---+---+---+---+---+
| E | # | L | # | I |
+---+---+---+---+---+
| T | E | L | I | X |
+---+---+---+---+---+

Words:
  ELIXIR
  TEXTURE
  LITERATE
```

### pinpoint
```
  1. Bacon
  2. Locke
  3. Confucius
  4. Plato and Socrates
  5. Descartes: “I think, therefore I am”

  answer: Famous philosophers!
```

### crossclimb
```
game      : crossclimb
number    : 875
date      : 2026-09-22
difficulty: None

Ladder (word : clue, top -> bottom):
  wide : The top + bottom rows = A word meaning "long from top to bottom," and a word meaning "long from side to side." Keep in mind: The first word may be at the bottom.
  wade : Walk in knee-deep water
  wage : Living ___ (fair salary)
  page : Either side of a sheet in a book
  pale : Drained of color
  tale : Fairy ___ (bedtime story)
  tall : The top + bottom rows = A word meaning "long from top to bottom," and a word meaning "long from side to side." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
