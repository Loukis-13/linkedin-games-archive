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
## Today's games (2026-08-19)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..    4   ..    6   ..   .. |
+          ----           ----     +
| .. |  1   .. | .. | ..    8 | .. |
+    +         +    +         +    +
| .. | ..   .. | .. | ..   .. | .. |
+    +         +    +         +    +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| .. | ..   .. | .. | ..   .. | .. |
+    +         +    +         +    +
| .. |  2   .. | .. | ..    7 | .. |
+    +----     +    +----     +    +
| ..   ..    3   ..    5   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | M | . | M |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+-=-+---+
| M | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+-x-+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | M | . | . | M |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧🟨
🟥🟧🟥🟥🟥🟧🟨🟨
🟥🟥🟥🟫🟥🟥🟥🟨
🟥🟫🟫🟫🟫🟫🟥🟨
🟥🟥🟫🟦🟫🟪🟪🟪
🟥🟫🟫🟩🟫🟫⬛🟪
🟥🟫🟩🟩🟩🟫⬛🟪
🟩🟩🟩⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 5 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 3 │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 2 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | +5 | .. | +9 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+
| |6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -3 |
+----+----+----+----+----+----+
| .. | .. | .. | +2 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +3 | .. | +4 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| O | L | I | A | O |
+---+---+---+---+---+
| C | N | C | # | C |
+---+---+---+---+---+
| C | U | # | C | O |
+---+---+---+---+---+
| U | O | C | # | C |
+---+---+---+---+---+
| P | Y | C | I | H |
+---+---+---+---+---+

Words:
  CHIC
  COCOA
  OCCUPY
  COUNCIL
```

### pinpoint
```
  1. William and Caroline Herschel
  2. Tycho Brahe
  3. Carl Sagan
  4. Nicolaus Copernicus
  5. Galileo Galilei

  answer: Famous astronomers!
```

### crossclimb
```
game      : crossclimb
number    : 841
date      : 2026-08-19
difficulty: None

Ladder (word : clue, top -> bottom):
  mini : The top + bottom rows = A compound word for a downscaled version of a sport where one only uses a putter to get a ball in a hole. Keep in mind: The first word may be at the bottom.
  mind : “___ over matter” (mental focus can overcome physical obstacles)
  find : Locate a lost item by searching
  fond : Enamored, with “of”
  fold : Common step in origami
  gold : Top medal at the Olympics
  golf : The top + bottom rows = A compound word for a downscaled version of a sport where one only uses a putter to get a ball in a hole. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
