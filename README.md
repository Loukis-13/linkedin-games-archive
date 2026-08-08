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
## Today's games (2026-08-08)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..    7   ..   ..   .. |
+                                       +
| ..   ..    5 | ..   .. | ..   12   10 |
+              +         +              +
| ..   ..   .. | ..   .. | ..   ..   .. |
+              +         +              +
| ..    6   .. | ..   .. | ..   11   .. |
+              +         +              +
| ..    3   .. | ..   .. | ..    8   .. |
+              +         +              +
|  2   ..   .. | ..   .. | ..   ..   .. |
+              +         +              +
| ..    4   .. | ..   .. |  9   ..   .. |
+              +         +              +
| ..   ..   ..    1   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | S | . | . | . |
+-x-+---+---+---+---+---+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
| M | . | . | . | S | . |
+---+---+---+---+---+---+
| . | M | . | . | . | S |
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+-=-+
| . | . | . | S | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟫🟩🟩🟦🟦🟦⬜
🟫🟫🟩🟩🟩🟦🟦⬜⬜
🟧🟧🟩🟩🟨🟨⬜⬜⬜
🟧🟧🟧🟨🟨🟨🟪🟪⬜
⬛🟧🟧🟨🟨🟪🟪🟪⬜
⬛⬛⬛🟥🟥🟪🟪⬜⬜
⬛⬛🟥🟥🟥⬜⬜⬜⬜
⬜⬛🟥🟥⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │ 2 ┃   │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃ 5 │   │ 1 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +10 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +10 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +10 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| A | B | # | # | C | D | # |
+---+---+---+---+---+---+---+
| F | A | Q | T | I | E | # |
+---+---+---+---+---+---+---+
| F | L | U | A | I | L | # |
+---+---+---+---+---+---+---+
| # | E | F | # | G | H | # |
+---+---+---+---+---+---+---+
| # | N | U | S | T | T | F |
+---+---+---+---+---+---+---+
| # | G | O | Y | I | C | U |
+---+---+---+---+---+---+---+
| # | I | J | # | # | K | L |
+---+---+---+---+---+---+---+

Words:
  FUNGI
  BAFFLE
  AQUATIC
  JOYSTICK
  DELIGHTFUL
```

### pinpoint
```
  1. Back
  2. Eye
  3. Eaves
  4. Rain
  5. Drag-and-

  answer (5 blanks): Terms that before "drop"!
```

### crossclimb
```
  dunes   
  danes   
  vanes   
  vases   
  bases   
  basis   
  oasis   

Clues (middle rows):
  - People from the same country as Neils Bohr and Hans Christian Andersen
  - Pieces of pottery that may hold flowers
  - Foundation of an argument
  - Military installations
  - Parts of windmills

Phrase (top+bottom): The top + bottom rows = Two words associated with the desert; the first word describes things made from blowing sand while the second word describes a welcome, if rare, sight. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
