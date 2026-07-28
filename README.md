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
## Today's games (2026-07-28)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
|  8   ..    9 |  2    1   10 |
+              +              +
| ..   ..   .. | ..   ..   .. |
+     ---- ----+---- ----     +
| ..   ..   .. | ..   ..   .. |
+              +              +
|  7    6    5 |  3   ..    4 |
+              +              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . x . | . |
+---+---+---+---+---+---+
| . | . | . | S | S | . |
+---+---+---+---+---+-=-+
| . | . | . | S | M | . |
+---+---+---+---+---+---+
| . | S | S | . | . | . |
+-x-+---+---+---+---+---+
| . | M | S | . | . | . |
+---+---+---+---+---+---+
| . | . x . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
⬛🟥🟨🟨🟨🟩🟩🟩
🟥🟥🟨🟩🟩🟩🟦🟦
🟥🟨🟨🟩🟦🟦🟦🟪
🟥🟨🟩🟩🟦🟪🟪🟪
🟥🟨🟩🟦🟦🟪🟫🟫
🟥🟨🟩🟦🟪🟪🟧🟧
🟥🟨🟩🟦🟦🟪🟪🟧
🟥🟥🟩🟩🟦🟦🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 6 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +5 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +5 | .. | +5 |
+----+----+----+----+----+----+
| .. | +5 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+
| |  | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | D | D | X | O |
+---+---+---+---+---+
| C | E | O | # | D |
+---+---+---+---+---+
| P | E | # | R | A |
+---+---+---+---+---+
| S | # | P | A | S |
+---+---+---+---+---+
| # | A | T | L | A |
+---+---+---+---+---+

Words:
  ODD
  ATLAS
  SPEECH
  PARADOX
```

### pinpoint
```
  1. Batman
  2. Samsun
  3. Antalya
  4. Ankara
  5. Istanbul

  answer (5 blanks): Cities in Türkiye!
```

### crossclimb
```
  fore    
  fork    
  pork    
  port    
  post    
  cost    
  cast    

Clues (middle rows):
  - Common piece of tableware, or a branch in the road
  - Place to plug in a USB device on a laptop
  - Price to pay
  - Ham or bacon
  - Share an update on social media

Phrase (top+bottom): The top + bottom rows = A compound word for a prediction made ahead of time, such as what the weather will be tomorrow. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
