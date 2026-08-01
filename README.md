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
## Today's games (2026-08-01)

### zip
```
+----+----+----+----+----+----+----+----+
|  6   ..   ..   ..   ..   ..   ..   .. |
+          ---- ---- ---- ----          +
| ..   ..   ..   ..   ..   ..   ..   .. |
+               ---- ---- ----          +
| .. | .. |  3   ..   ..   ..   .. |  1 |
+    +    +     ----               +    +
| .. |  5 | ..   ..   .. | .. | .. | .. |
+    +    +              +    +    +    +
| .. | .. | .. | ..   ..   .. |  2 | .. |
+    +    +    +     ----     +    +    +
|  7 | ..   ..   ..   ..    4 | .. | .. |
+    +     ---- ---- ----     +    +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+          ---- ---- ---- ----          +
| ..   ..   ..   ..   ..   ..   ..    8 |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | M | M | S |
+---+---+---+---+---+---+
| . | . | . | M | . | M |
+---+---+---+---+---+---+
| . | . | . | S | M | S |
+---+---+---+---+---+---+
| . | . x . | . | . | . |
+-=-+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+-=-+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜🟩🟩🟩🟩🟫⬛⬛
⬜🟩🟩🟦🟩🟫🟫🟫⬛
⬜🟩🟦🟦🟦🟩🟫🟩⬛
⬜🟩🟩🟦🟩🟩🟩🟩⬛
⬜🟩🟩🟩🟩🟪🟪🟩⬛
⬜⬜🟩🟩🟧🟪🟪🟨🟨
⬜⬜⬜⬜🟧🟨🟨🟨🟨
⬜⬜⬜🟥🟧🟥🟨🟨🟨
⬜⬜⬜🟥🟥🟥🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | +2 | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | -2 |
+----+----+----+----+----+----+----+
| .. | +2 | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| A | B | C | D | # | # |
+---+---+---+---+---+---+
| N | N | E | O | T | E |
+---+---+---+---+---+---+
| K | A | U | L | A | M |
+---+---+---+---+---+---+
| R | E | T | O | T | A |
+---+---+---+---+---+---+
| U | P | T | S | I | R |
+---+---+---+---+---+---+
| # | # | A | B | C | D |
+---+---+---+---+---+---+

Words:
  BANKRUPT
  ANECDOTE
  ABSOLUTE
  DRAMATIC
```

### pinpoint
```
  1. Wheel
  2. Ribs
  3. Glaze
  4. Clay
  5. Kiln

  answer (5 blanks): Things used when making pottery!
```

### crossclimb
```
  lands   
  lends   
  leads   
  loads   
  goads   
  grads   
  grass   

Clues (middle rows):
  - Potential customers who are interested in a company’s services
  - ___ a hand (helps out)
  - Urges on with a stick
  - Lots and lots
  - Alumni of a university, for short

Phrase (top+bottom): The top + bottom rows = A compound word describing biomes like prairies, steppes, and savannas. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
