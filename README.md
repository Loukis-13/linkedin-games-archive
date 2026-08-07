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
## Today's games (2026-08-07)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   12    5    4   10   11   .. |
+                                  +
| ..   13   ..   ..   ..    9   .. |
+                                  +
| ..   16   ..   ..   ..    1   .. |
+                                  +
| ..   15   ..   ..   ..    8   .. |
+                                  +
| ..   14    6    3    2    7   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | S | . | . | . |
+---+-x-+---+-x-+---+---+
| . x . | M | . | . | . |
+---+---+---+---+---+---+
| M | M | S | . | . | . |
+---+---+---+-x-+---+---+
| . x . | . x . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬜⬜🟧🟧🟧🟨🟨
⬜🟩🟩🟩🟩🟩🟧🟩🟨
⬜🟩🟪🟪🟪🟩🟦🟩🟨
⬜🟩🟪🟩🟪🟩🟦🟩🟫
⬜🟩🟪🟩🟪🟩🟦🟩🟫
⬛🟩🟥🟩🟩🟩🟦🟩🟫
⬛🟩🟥🟥🟥🟦🟦🟩🟫
⬛🟩🟩🟩🟩🟩🟩🟩🟫
⬛⬛⬛⬛⬛⬛🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │ 3 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │ 5 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | +7 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +7 | .. | .. |
+----+----+----+----+----+----+----+
| +7 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +7 | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| R | O | # | # | U | X |
+---+---+---+---+---+---+
| C | S | D | E | L | E |
+---+---+---+---+---+---+
| # | S | R | N | W | # |
+---+---+---+---+---+---+
| # | T | O | S | O | # |
+---+---+---+---+---+---+
| E | C | A | D | N | U |
+---+---+---+---+---+---+
| X | A | # | # | K | N |
+---+---+---+---+---+---+

Words:
  EXACT
  DELUXE
  UNKNOWN
  CROSSROADS
```

### pinpoint
```
  1. Hook
  2. Jaws
  3. War Horse
  4. Jurassic Park
  5. Schindler’s List

  answer (5 blanks): Films directed by Steven Spielberg!
```

### crossclimb
```
  come    
  code    
  mode    
  mole    
  hole    
  hone    
  gone    

Clues (middle rows):
  - Burrowing animal, or a unit of measurement in chemistry
  - A system to encrypt words to send a secret message
  - Sharpen, as one’s skills
  - The most frequently appearing value in a data set
  - Something that can be dug in the ground

Phrase (top+bottom): The top + bottom rows = Two words with opposite meanings that often appear together idiomatically, as in the sentence “The opportunity has ___ and ___.” Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
