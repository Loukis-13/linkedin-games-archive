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
## Today's games (2026-08-03)

### zip
```
+----+----+----+----+----+----+
| ..    9   ..   ..    2   .. |
+                             +
| ..   10    1   12   11   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+     ---- ---- ---- ----     +
| ..   ..   ..   ..   ..   .. |
+                             +
| ..    6    7    4    5   .. |
+                             +
| ..    8   ..   ..    3   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+-=-+-x-+---+---+
| . | S | . | . | S | . |
+---+---+---+---+---+---+
| . | M | M | S | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟨🟨
🟥🟥🟧🟩🟧🟧🟨
🟥🟥🟩🟩🟩🟧🟧
🟦🟩🟩🟪🟩🟩🟩
🟦🟦🟩🟩🟩🟦🟩
🟫🟦🟦🟩🟦🟦🟦
🟫🟫🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 4 │   ┃   │ 1 │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 5 │   ┃   │ 3 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 1 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +3 | +8 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +8 | +3 |
+----+----+----+----+----+----+
| +3 | +8 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| I | M | I | L | H |
+---+---+---+---+---+
| T | # | # | # | C |
+---+---+---+---+---+
| N | I | # | I | T |
+---+---+---+---+---+
| S | # | # | # | B |
+---+---+---+---+---+
| I | S | T | T | I |
+---+---+---+---+---+

Words:
  BIT
  ITCH
  LIMIT
  INSIST
```

### pinpoint
```
  1. Date
  2. Lychee
  3. Apricot
  4. Peach
  5. Cherry

  answer (5 blanks): Names of stone fruits (drupes)!
```

### crossclimb
```
  road    
  toad    
  told    
  toll    
  tall    
  tail    
  rail    

Clues (middle rows):
  - Amphibian creature similar to a frog
  - Opposite of short
  - “I ___ you so!” (expression when someone didn’t listen to a prior warning)
  - Part of a dog that might wag
  - Payment to cross a bridge

Phrase (top+bottom): The top + bottom rows = A compound word for a system of transportation by train, or one of the physical tracks used for it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
