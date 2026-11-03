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
## Today's games (2026-11-03)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    7 |  3   .. |
+                   +         +
| ..   ..   ..   .. | ..   .. |
+                   +         +
| ..    6 |  8   ..   ..   .. |
+         +                   +
| ..   ..   ..    2 |  1   .. |
+                   +         +
| ..   .. | ..   ..   ..   .. |
+         +                   +
| ..    5 |  4   ..   ..   .. |
+---- ----+---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+-=-+---+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+-x-+-=-+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+-=-+---+---+---+---+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟨🟨
🟧🟧🟧🟩🟧🟧🟨
🟧🟧🟩🟩🟧🟧🟧
🟦🟧🟧🟧🟧🟪🟧
🟦🟧🟧🟧🟪🟪🟧
🟦🟦🟦🟧🟧🟧🟧
🟦🟦🟦🟧🟧🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 2 │ 4 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 5 ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +4 | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | +3 | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | +2 | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | +6 | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| S | E | G | U | S |
+---+---+---+---+---+
| N | E | G | # | # |
+---+---+---+---+---+
| # | S | E | S | # |
+---+---+---+---+---+
| # | # | T | T | P |
+---+---+---+---+---+
| S | A | L | A | S |
+---+---+---+---+---+

Words:
  ASP
  SALT
  SENSE
  SUGGEST
```

### pinpoint
```
  1. Taiga
  2. Tundra
  3. Savanna
  4. Desert
  5. Rainforest

  answer: Types of biome!
```

### crossclimb
```
game      : crossclimb
number    : 917
date      : 2026-11-03
difficulty: None

Ladder (word : clue, top -> bottom):
  cone : The top + bottom rows = A two-word phrase for a certain evergreen tree's seed-bearing organ. Keep in mind: The first word may be at the bottom.
  tone : ___ of voice (indicator of emotion)
  tore : Accidentally did damage to, as a page of a book
  fore : Warning a golfer yells
  fire : Source of warmth in cold weather
  fine : High-quality, like some dining
  pine : The top + bottom rows = A two-word phrase for a certain evergreen tree's seed-bearing organ. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
