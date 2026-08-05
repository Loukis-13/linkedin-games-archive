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
## Today's games (2026-08-05)

### zip
```
+----+----+----+----+----+----+
| ..   ..    1    2   ..   .. |
+                             +
| ..   ..   ..   ..   10   .. |
+                             +
| ..   ..    9   ..    4   .. |
+                             +
| ..    6   ..    5   ..   .. |
+                             +
| ..    7   ..   ..   ..   .. |
+                             +
| ..   ..    8    3   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | S | M | . | . |
+---+---+---+---+---+---+
| . | . | M | S | . | . |
+---+---+---+---+---+---+
| S | S | . | . | . = . |
+---+---+---+---+---+---+
| M | S | . | . | . x . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟨🟨🟨🟩
🟥🟦🟥🟧🟨🟪🟨🟩
🟥🟦🟥🟧🟨🟪🟨🟩
🟥🟥🟥🟧🟨🟨🟨🟩
🟥🟥🟥🟧🟥🟥🟫🟫
🟥🟥🟥🟧🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥⬛
⬛⬛⬛⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 5 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 3 │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +15 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +25 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | E | E | # | # | # |
+---+---+---+---+---+---+
| A | T | X | A | # | # |
+---+---+---+---+---+---+
| U | Q | K | M | E | # |
+---+---+---+---+---+---+
| # | E | N | P | L | A |
+---+---+---+---+---+---+
| # | # | I | F | R | E |
+---+---+---+---+---+---+
| # | # | # | E | A | # |
+---+---+---+---+---+---+

Words:
  AREA
  KNIFE
  EQUATE
  EXAMPLE
```

### pinpoint
```
  1. Drill
  2. Marmoset
  3. Capuchin
  4. Macaque
  5. Baboon

  answer (5 blanks): Types of monkey!
```

### crossclimb
```
  cape    
  tape    
  taps    
  tans    
  tons    
  tows    
  town    

Clues (middle rows):
  - Sticky strip that can be used instead of glue
  - Gets a lot of rays at the beach
  - Pulls an automobile to a repair shop
  - A great amount, or units to describe something weighing 10,000 pounds
  - Light hits

Phrase (top+bottom): The top + bottom rows = A two-word name for a port city that is the legislative capital of South Africa. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
