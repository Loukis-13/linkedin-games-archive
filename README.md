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
## Today's games (2026-07-27)

### zip
```
+----+----+----+----+----+----+
| ..    1   ..   ..   ..   .. |
+                             +
| ..    8   ..   ..   ..   .. |
+                             +
|  2   ..   ..   .. | ..    7 |
+---- ----          +---- ----+
|  3   .. | ..   ..   ..    5 |
+         +                   +
| ..   ..   ..   ..    6   .. |
+                             +
| ..   ..   ..   ..    4   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | S | . | . | S | S |
+---+---+---+---+---+---+
| M | S | . | . | M | S |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | M | M | S | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟧🟧🟧
🟥🟨🟩🟩🟧🟧🟧
🟥🟩🟩🟩🟧🟧🟧
🟦🟩🟩🟩🟩🟩🟪
🟦🟩🟩🟩🟩🟩🟪
🟦🟩🟩🟩🟩🟫🟪
🟦🟦🟦🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 5 ┃ 2 │ 6 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| |6 | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |5 | .. | +3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +6 | .. | |4 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | |5 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | T | M | R | A |
+---+---+---+---+---+
| O | O | M | C | I |
+---+---+---+---+---+
| M | # | M | # | M |
+---+---+---+---+---+
| E | # | A | # | I |
+---+---+---+---+---+
| M | # | M | # | M |
+---+---+---+---+---+

Words:
  ARM
  MEMO
  MIMIC
  MAMMOTH
```

### pinpoint
```
  1. Sat
  2. Wed
  3. Sun
  4. Fri
  5. Mon

  answer (5 blanks): Abbreviations for days of the week!
```

### crossclimb
```
  chin    
  coin    
  corn    
  core    
  cone    
  none    
  nose    

Clues (middle rows):
  - Edible holder for ice cream
  - Piece of metal currency that may be flipped
  - Part of an apple that contains its seeds
  - “A friend to all is a friend to ___” (Aristotle)
  - Cereal crop that might appear at breakfast in “flake” form

Phrase (top+bottom): The top + bottom rows = Two parts of the face.
```
<!-- DAILY-GAMES-END -->
