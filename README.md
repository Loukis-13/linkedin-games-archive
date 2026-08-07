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
| ..   11   ..   12    7    8   .. |
+                                  +
| ..   10   ..    9   ..   ..   .. |
+                                  +
| ..   13   ..   14    4    3   .. |
+                                  +
| ..    6   ..    5   ..   ..   .. |
+                                  +
| ..    1   ..    2   ..   ..   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . x . | M | . | . |
+---+---+---+---+---+---+
| . | . | M | . | . | . |
+-x-+---+---+---+---+---+
| . | S | . | . | . | S |
+---+---+---+---+---+---+
| M | . | . | . | S | . |
+---+---+---+---+---+-=-+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
| . | . | S | . x . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟨🟨🟨
🟥🟥🟧🟧🟧🟨🟨🟨
🟩🟩🟧🟧🟦🟦🟨🟨
🟩🟩🟩🟪🟦🟦🟦🟨
🟨🟩🟩🟫🟫🟦🟦🟨
🟨🟨🟫🟫🟫⬛⬛🟨
🟨🟨🟫🟫🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │ 6 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | +8 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +5 | +2 | .. |
+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+----+
| .. | |  | -  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| T | C | A | J | O | B |
+---+---+---+---+---+---+
| E | K | # | # | C | W |
+---+---+---+---+---+---+
| U | X | A | R | D | E |
+---+---+---+---+---+---+
| L | # | Z | I | # | B |
+---+---+---+---+---+---+
| F | # | Q | L | # | M |
+---+---+---+---+---+---+
| N | I | U | O | R | U |
+---+---+---+---+---+---+

Words:
  JACKET
  COBWEB
  QUORUM
  LIZARD
  INFLUX
```

### pinpoint
```
  1. Balance
  2. Limits
  3. The wall
  4. The record
  5. The cuff

  answer (5 blanks): Words that come after "off"!
```

### crossclimb
```
  five    
  live    
  love    
  lore    
  fore    
  ford    
  fold    

Clues (middle rows):
  - “All is fair in ___ and war”
  - Word a golfer may shout when a ball is hit off course
  - Stories passed down between generations that may or may not be true
  - As it happens, like a news event being broadcast
  - Major automobile manufacturer based in the US in Michigan

Phrase (top+bottom): The top + bottom rows = A compound word that describes how much something has increased after it has quintupled. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
