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
## Today's games (2026-10-02)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
|  9    5   ..   ..   ..   ..   .. |
+                                  +
| ..    6   ..   ..    1    4   .. |
+                                  +
| ..    8   ..   ..   ..    3   .. |
+                                  +
| ..   11    7   ..   ..    2   .. |
+                                  +
| ..   ..   ..   ..   ..   12   10 |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . | M | . |
+---+---+---+---+---+---+
| M | M | S | M | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . x . x . = . x . |
+---+-=-+---+---+---+-=-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟨🟨
🟥🟩🟩🟩🟩🟧🟧🟨
🟦🟩🟩🟩🟩🟩🟧🟨
🟦🟦🟦🟩🟩🟩🟩🟩
🟦🟩🟩🟩🟩🟩🟩🟩
🟪🟩🟩🟩🟫🟩🟩🟩
🟪🟩🟩🟩🟫🟩🟩⬛
🟪🟪🟫🟫🟫⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 2 │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │ 3 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | +  | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+
| .. | .. | +2 | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | # | E | R | # | # |
+---+---+---+---+---+---+
| # | P | F | A | B | # |
+---+---+---+---+---+---+
| L | I | O | O | B | L |
+---+---+---+---+---+---+
| F | K | B | T | W | O |
+---+---+---+---+---+---+
| # | C | A | I | F | # |
+---+---+---+---+---+---+
| # | # | H | S | # | # |
+---+---+---+---+---+---+

Words:
  BAREFOOT
  BLOWFISH
  BACKFLIP
```

### pinpoint
```
  1. Golf
  2. Whiskey
  3. Bagpipes
  4. Haggis
  5. The Loch Ness Monster

  answer: Things associated with Scotland (🏴󠁧󠁢󠁳󠁣󠁴󠁿)!
```

### crossclimb
```
game      : crossclimb
number    : 885
date      : 2026-10-02
difficulty: None

Ladder (word : clue, top -> bottom):
  coal : The top + bottom rows = Two sources of energy, one that's burned and one that blows. Keep in mind: The first word may be at the bottom.
  cool : Trendy or acceptable
  fool : Play the ___ (act like a court jester)
  food : Necessary source of nutrients
  fond : Having a warm, positive opinion (of)
  find : Locate, as something lost
  wind : The top + bottom rows = Two sources of energy, one that's burned and one that blows. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
