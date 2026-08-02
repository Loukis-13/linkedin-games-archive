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
## Today's games (2026-08-02)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..    3    7   ..   ..   ..   .. |
+          ---- ----      ----          +
| ..   ..   ..   ..   ..    8   ..   .. |
+          ---- ----      ----          +
| ..   ..   ..   ..   ..    1   ..   .. |
+          ---- ---- ---- ----          +
| ..   ..    2   ..   ..   ..   ..   .. |
+          ----      ---- ----          +
| ..   ..    5   ..   ..   ..   ..   .. |
+          ----      ---- ----          +
| ..   ..   ..   ..    4    6   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . | . | M |
+---+---+---+---+---+---+
| . | . x . | . = . | . |
+---+---+---+---+---+---+
| . | . = . | . = . | . |
+---+---+---+---+---+---+
| . | . = . | . x . | . |
+---+---+---+---+---+---+
| . | . x . | . = . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥⬛🟫🟫🟫🟦
🟦🟦🟦🟥⬛⬛🟫🟪🟦
🟦🟦🟧🟧⬛⬛🟫🟪🟦
🟦🟦🟦🟧⬛⬛🟪🟪🟦
🟦🟨🟨🟧🟧⬛⬛🟪🟦
🟦🟨⬛⬛⬛⬛⬛⬜🟦
🟦🟨⬛🟩🟩🟩⬛⬜🟦
🟦🟨🟩🟩🟦⬜⬜⬜🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | .. | -2 | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +  | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +2 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +2 | +2 | |2 | .. | .. |
+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| A | G | R | I | N | L | A |
+---+---+---+---+---+---+---+
| H | # | P | P | A | # | U |
+---+---+---+---+---+---+---+
| C | N | I | E | H | H | G |
+---+---+---+---+---+---+---+
| S | E | S | L | E | T | B |
+---+---+---+---+---+---+---+
| S | # | M | I | R | # | A |
+---+---+---+---+---+---+---+
| E | A | # | # | # | T | S |
+---+---+---+---+---+---+---+
| B | M | Y | O | J | E | K |
+---+---+---+---+---+---+---+

Words:
  JOY
  BEAM
  SMILE
  BASKET
  CHAGRIN
  LAUGHTER
  HAPPINESS
```

### pinpoint
```
  1. First
  2. Pin
  3. Net
  4. Valve
  5. In numbers

  answer (5 blanks): Words that come after “safety”!
```

### crossclimb
```
  gild    
  gill    
  mill    
  mild    
  wild    
  wily    
  lily    

Clues (middle rows):
  - ___-goose chase (lengthy and usually fruitless pursuit)
  - Breathing organ used by a fish to get oxygen from water
  - Gentle or moderate
  - Cunning and shrewd
  - Place where grain is ground into flour

Phrase (top+bottom): The top + bottom rows = Two words that complete the saying “___ the ___” meaning to embellish or overdecorate something that is already beautiful. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
