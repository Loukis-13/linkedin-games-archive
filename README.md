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
## Today's games (2026-09-30)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+          ---- ----          +
| ..    1   ..   ..    2   .. |
+          ---- ----          +
| ..    4   ..   ..    3   .. |
+          ---- ----          +
| ..    6   ..   ..    5   .. |
+          ---- ----          +
| ..    8   ..   ..    7   .. |
+          ---- ----          +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | M | M |
+-x-+-=-+---+---+---+---+
| . | . | . | . | M | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | S | . | . | . | . |
+---+---+---+---+-=-+-=-+
| M | S | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟨🟩🟩🟩🟩🟩
🟥🟥🟨🟨🟩🟩🟩🟦
🟥🟥🟥🟨🟪🟩🟨🟦
🟥🟥🟨🟨🟪🟨🟨🟫
🟥🟨🟨🟨🟨🟨🟫🟫
🟨🟨⬛🟨🟨🟫🟫🟫
🟨⬛⬛⬛🟨🟨🟫🟫
⬛⬛⬛⬛⬛🟨🟨🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 2 │   ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │ 2 ┃   │ 3 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -3 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +16 | .. | +9 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -8 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. | =  |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | L | # | E | G |
+---+---+---+---+---+
| O | D | V | # | A |
+---+---+---+---+---+
| O | N | O | L | T |
+---+---+---+---+---+
| T | # | H | C | M |
+---+---+---+---+---+
| R | Y | # | R | A |
+---+---+---+---+---+

Words:
  TRY
  MARCH
  NOODLE
  VOLTAGE
```

### pinpoint
```
  1. Nose
  2. Napkin
  3. Mood
  4. Boxing
  5. Wedding (worn after “I dos”)

  answer: Types of rings!
```

### crossclimb
```
game      : crossclimb
number    : 883
date      : 2026-09-30
difficulty: None

Ladder (word : clue, top -> bottom):
  free : The top + bottom rows = A two-word phrase for a person's ability to make their own choices. Keep in mind: The first word may be at the bottom.
  fret : Constantly worry, or part of a guitar's neck
  feet : Body parts with arches and soles
  felt : Soft surface on a billiards table
  fell : Went to the ground, most likely accidentally
  fill : Pour liquid into, as a glass
  will : The top + bottom rows = A two-word phrase for a person's ability to make their own choices. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
