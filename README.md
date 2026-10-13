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
## Today's games (2026-10-13)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+     ---- ---- ---- ----     +
| ..   ..    3 |  5   ..   .. |
+              +              +
| ..    8   .. | ..    4   .. |
+              +              +
| ..    1   .. | ..    7   .. |
+              +              +
| ..   ..    2 |  6   ..   .. |
+     ---- ----+---- ----     +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-=-+-x-+-x-+---+---+---+
| . | M | . | . | . | . |
+-x-+---+-=-+---+---+---+
| . = . x . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . x . |
+---+---+---+-=-+---+-x-+
| . | . | . | . | M | . |
+---+---+---+-x-+-=-+-=-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟨🟨🟨🟨🟨🟨🟨
🟥🟥🟨🟨🟨🟨🟨🟧🟨
🟨🟨🟩🟩🟨🟨🟨🟧🟧
🟨🟨🟩🟨🟨🟦🟦🟨🟨
🟪🟨🟨🟨🟨🟦🟫🟨🟨
🟪🟨🟨🟨🟨🟨🟫🟫🟨
🟨⬛⬛🟨⬜⬜🟨🟨🟨
🟨⬛🟨🟨⬜⬜🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 2 │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │ 5 ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +5 | .. | .. | .. | .. | |5 |
+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. |
+----+----+----+----+----+----+
| =4 | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| A | R | C | A | P |
+---+---+---+---+---+
| M | Y | P | # | K |
+---+---+---+---+---+
| I | D | # | # | C |
+---+---+---+---+---+
| T | # | # | # | O |
+---+---+---+---+---+
| I | E | R | B | L |
+---+---+---+---+---+

Words:
  CAP
  TIER
  BLOCK
  PYRAMID
```

### pinpoint
```
  1. Amethyst
  2. Mauve
  3. Lilac
  4. Plum
  5. Lavender (looks like 🪻)

  answer: Shades of purple or violet!
```

### crossclimb
```
game      : crossclimb
number    : 896
date      : 2026-10-13
difficulty: None

Ladder (word : clue, top -> bottom):
  post : The top + bottom rows = Two verbs meaning to drop in the mail.
  most : Opposite of least
  mist : Fine spray of water
  mint : Herb name that often follows “pepper” or “spear”
  mind : Keep in ___ (take into account)
  mend : Repair, as a hole in a garment
  send : The top + bottom rows = Two verbs meaning to drop in the mail.
```
<!-- DAILY-GAMES-END -->
