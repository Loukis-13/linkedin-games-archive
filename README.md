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
## Today's games (2026-07-31)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..    4 |
+     ---- ----                    +
| .. | ..   ..    1 | ..    3   .. |
+    +              +              +
| .. | ..   ..   .. | ..    6   .. |
+    +     ---- ----+              +
| ..   ..   ..   ..   ..   ..   .. |
+               ---- ----          +
| ..    2   .. | ..   ..   .. | .. |
+              +              +    +
| ..    8   .. |  5   ..   .. | .. |
+              +     ---- ----+    +
|  7   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | S | S | . | . |
+---+---+---+---+---+---+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-=-+---+---+---+---+-=-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | S | . |
+---+---+---+---+---+---+
| . | . | M | S | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟧🟧🟧
🟥🟨🟨🟨🟨🟥🟧⬜⬜
🟥🟨🟨🟨🟨🟥🟧⬜⬜
🟥🟥🟥🟧🟧🟧🟧⬜⬜
🟦🟦🟥🟥🟥🟥🟧⬜⬜
🟦🟦⬛🟥🟧🟧🟧🟧🟧
🟦🟦⬛🟫🟪🟪🟪🟪🟧
🟦🟦⬛🟫🟪🟪🟪🟪🟧
🟩🟩🟩🟫🟫🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 3 │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │ 6 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +8 | .. | .. | .. | .. | +6 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| =  | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| H | # | I | # | G | # | H |
+---+---+---+---+---+---+---+
| O | R | C | I | N | I | S |
+---+---+---+---+---+---+---+
| # | I | # | I | # | N | # |
+---+---+---+---+---+---+---+
| O | Z | O | M | A | I | F |
+---+---+---+---+---+---+---+
| N | # | W | # | G | # | A |
+---+---+---+---+---+---+---+
| T | A | N | R | I | O | V |
+---+---+---+---+---+---+---+
| # | L | # | O | # | W | # |
+---+---+---+---+---+---+---+

Words:
  OWN
  AVOW
  ICING
  FINISH
  ORIGAMI
  HORIZONTAL
```

### pinpoint
```
  1. Fair
  2. Asking
  3. Market
  4. Sale
  5. Name your

  answer (5 blanks): Words that come before “price”!
```

### crossclimb
```
  fine    
  fire    
  firs    
  airs    
  aims    
  arms    
  arts    

Clues (middle rows):
  - Classical element alongside earth, air, and water
  - Body parts attached to the shoulders
  - States publicly, as grievances
  - Evergreen trees known for needle-like leaves
  - Goals and objectives

Phrase (top+bottom): The top + bottom rows = Two words that complete the name of the degree “Bachelor of ___ ___” earned by a student pursuing visual works, performance, or other creative areas. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
