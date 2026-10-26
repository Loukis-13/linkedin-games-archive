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
## Today's games (2026-10-26)

### zip
```
+----+----+----+----+----+----+
| ..    1   ..   ..    7   .. |
+                             +
| ..    8   ..   ..    9   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
|  2   ..   ..   ..   ..    6 |
+                             +
| ..    4   ..   ..   10   .. |
+                             +
| ..   ..    3    5   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . = . | . |
+---+---+---+---+-=-+---+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | . | S | M | . | . |
+---+-=-+---+---+---+---+
| . | . = . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟥🟥🟦
🟦🟦⬛⬛🟦🟦🟦🟦
🟦🟦🟦🟦🟨🟨🟦🟦
🟦🟪🟪🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟧🟧🟦
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟩🟩🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │ 3 ┃ 5 │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 4 ┃ 6 │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +2 | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |4 | .. |
+----+----+----+----+----+----+
| .. | .. | +2 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+
| .. | |8 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | +6 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| P | P | E | P | P |
+---+---+---+---+---+
| U | # | # | # | E |
+---+---+---+---+---+
| P | # | # | # | R |
+---+---+---+---+---+
| P | # | P | P | O |
+---+---+---+---+---+
| Y | T | E | Y | T |
+---+---+---+---+---+

Words:
  PET
  TYPO
  PUPPY
  PEPPER
```

### pinpoint
```
  1. Pewter
  2. Solder
  3. Brass
  4. Bronze
  5. Stainless steel (Fe + Cr + Ni)

  answer: Metal alloys!
```

### crossclimb
```
game      : crossclimb
number    : 909
date      : 2026-10-26
difficulty: None

Ladder (word : clue, top -> bottom):
  deal : The top + bottom rows = A word meaning to distribute playing cards, and a word for what each player then has. Keep in mind: The first word may be at the bottom.
  real : Actually existing
  read : Enjoy literature
  lead : Heavy metallic element that can block X-rays
  lend : ___ an ear (listen)
  land : Terrestrial animals live on it
  hand : The top + bottom rows = A word meaning to distribute playing cards, and a word for what each player then has. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
