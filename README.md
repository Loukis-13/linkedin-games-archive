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
## Today's games (2026-08-04)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..    7 | ..    4 | .. |
+              +         +    +
| ..   ..    8 | ..    3 | .. |
+              +         +    +
| .. |  6   .. |  2   ..   .. |
+    +         +              +
| .. |  1   .. |  5   ..   .. |
+    +         +              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . = . | . |
+---+---+---+-=-+-=-+---+
| . | M | . | . = . | . |
+---+---+---+---+---+---+
| M | . | M | . | . | . |
+---+---+---+---+---+---+
| . | S | . | M | . | . |
+---+---+---+---+---+---+
| M | . | S | . | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟧🟨🟥🟨
🟩🟧🟦🟧🟨🟥🟨
🟩🟧🟧🟧🟨🟨🟨
🟩🟩🟩🟧🟪🟪🟪
🟩🟩🟩🟧🟧🟫🟫
🟩🟩🟩🟩🟩🟩🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃ 4 │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │ 6 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |  | =  | .. | .. |
+----+----+----+----+----+----+
| .. | +8 | .. | .. | +4 | .. |
+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| A | # | A | # | A |
+---+---+---+---+---+
| L | G | R | C | C |
+---+---+---+---+---+
| # | E | B | E | # |
+---+---+---+---+---+
| G | E | S | S | L |
+---+---+---+---+---+
| A | U | G | N | A |
+---+---+---+---+---+

Words:
  ACCESS
  ALGEBRA
  LANGUAGE
```

### pinpoint
```
  1. Ghosts in Pac-Man
  2. Grand Slams in tennis
  3. Bases in DNA
  4. Nations in the United Kingdom
  5. Train spaces in Monopoly (1/side)

  answer (5 blanks): Things that come in groups of four!
```

### crossclimb
```
  sets    
  sees    
  fees    
  feel    
  heel    
  heal    
  head    

Clues (middle rows):
  - Touch with one’s hand
  - Observes with one’s eyes
  - Part of the foot, and a homophone of another answer in this ladder
  - Get better, and a homophone of another answer in this ladder
  - Fixed prices for a service

Phrase (top+bottom): The top + bottom rows = A compound word for devices that might be worn during videos calls to both hear and be heard. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
