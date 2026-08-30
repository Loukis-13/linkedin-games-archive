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
## Today's games (2026-08-30)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    3    2   ..    6    8   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    4   ..    7   ..    1   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    5    9   ..   10   11   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+---+
| S | M | . | . | . | . |
+---+---+---+---+---+---+
| M | S | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . = . |
+---+---+---+---+-x-+-=-+
| . | . | . | . | . | . |
+---+---+---+---+-=-+-x-+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🟥🟥🟧⬛⬛⬜
⬜⬜🟥🟥🟧🟧⬛⬛⬜
⬜⬜🟥🟧🟧🟨⬛⬛⬜
⬜🟩🟩🟩🟩🟨🟨⬛⬛
⬜🟩🟩🟩🟫🟫🟨🟨⬛
🟩🟩🟦🟦🟪🟫🟫⬛⬛
🟩🟦🟦🟪🟪⬛🟫⬛⬛
🟩🟦🟪🟪⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃ 4 │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 5 ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | +6 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +6 | .. | +3 | .. | .. | +3 | .. | +3 |
+----+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. | +9 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| G | N | G | T | H | D | S |
+---+---+---+---+---+---+---+
| A | I | O | U | E | A | E |
+---+---+---+---+---+---+---+
| U | # | # | O | # | # | T |
+---+---+---+---+---+---+---+
| D | I | O | U | A | E | R |
+---+---+---+---+---+---+---+
| R | A | E | I | O | U | U |
+---+---+---+---+---+---+---+
| A | E | P | C | A | S | B |
+---+---+---+---+---+---+---+
| N | C | P | A | N | E | T |
+---+---+---+---+---+---+---+

Words:
  AUDIO
  BUREAU
  HEADSET
  OUTGOING
  TENACIOUS
  APPEARANCE
```

### pinpoint
```
  1. Everything
  2. Anchor
  3. A hint
  4. A line
  5. The ball

  answer: Words that follow “drop” in common sayings!
```

### crossclimb
```
game      : crossclimb
number    : 852
date      : 2026-08-30
difficulty: None

Ladder (word : clue, top -> bottom):
  rover : The top + bottom rows = What NASA's Perseverance is, and what it photographed from Mars on October 4, 2025. Keep in mind: The first word may be at the bottom.
  river : Mississippi or Nile, for example
  diver : Scuba ___
  dover : City in England with white cliffs
  cover : Perform a new version of a song originally by another artist
  covet : Have a strong desire for something that belongs to someone else
  comet : The top + bottom rows = What NASA's Perseverance is, and what it photographed from Mars on October 4, 2025. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
