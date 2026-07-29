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
## Today's games (2026-07-29)

### zip
```
+----+----+----+----+----+----+
| 10   ..    9    8   ..    6 |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
|  7   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..    5 |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
|  4   ..    1    2   ..    3 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . x . | . | . | . | . |
+---+---+---+---+-=-+-x-+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+---+---+---+---+
| . | M | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . = . |
+-=-+-x-+---+---+---+---+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟧🟧🟪🟪🟨🟨
🟨🟧🟧🟪🟪🟪🟨🟨
🟨🟫🟫🟨🟨🟨🟦🟦
🟨🟨🟫🟨🟨🟨🟦🟦
🟨🟨🟫🟨🟨🟨🟦🟩
🟨🟨🟨🟨🟥🟥🟩🟩
⬛⬛⬛🟥🟥🟥🟥🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 4 │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 6 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 6 │   │   ┃   │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +4 | +3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | +4 | .. |
+----+----+----+----+----+----+
| .. | -  | .. | .. | +6 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +6 | +5 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | I | L | M | N |
+---+---+---+---+---+
| G | F | # | # | O |
+---+---+---+---+---+
| U | O | D | # | P |
+---+---+---+---+---+
| A | B | C | O | U |
+---+---+---+---+---+
| H | I | T | A | T |
+---+---+---+---+---+

Words:
  FILM
  DOUGH
  COUPON
  HABITAT
```

### pinpoint
```
  1. Merry
  2. Sam
  3. Boromir
  4. Frodo
  5. Gandalf the Grey

  answer (5 blanks): Members of the Fellowship of the Ring (J.R.R. Tolkien)!
```

### crossclimb
```
  foot    
  boot    
  boos    
  bots    
  both    
  bath    
  path    

Clues (middle rows):
  - Best of ___ worlds (enjoy two things simultaneously)
  - Type of shoe that extends up the lower leg to offer more protection
  - Software programs that crawl the web to analyze web pages
  - Protesting sounds heard after a controversial sports call
  - Relaxing soak in a tub

Phrase (top+bottom): The top + bottom rows = A compound word for a narrow walkway used by pedestrians and not vehicles. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
