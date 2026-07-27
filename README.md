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
## Today's games (2026-07-26)

### zip
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   12   13   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   10    9   ..   15   14   .. |
+                                       +
| ..   ..   ..   ..   ..   ..    4    1 |
+                                       +
|  2   11   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    3    8   ..   16    5   ..   .. |
+                                       +
| ..   ..   ..   ..   ..    7    6   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+

### tango
+---+---+---+---+---+---+
| . | . | . | . | M | M |
+---+---+---+---+---+---+
| . | . = . | . | . | M |
+---+---+-x-+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+---+-=-+---+
| M | M | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+---+---+

### queens
🟩🟩🟦🟦🟦🟦🟦🟦🟦
🟩🟥🟥🟥⬜⬜⬜⬜🟦
🟩🟩🟩🟥⬜⬜⬜⬜🟪
🟩🟥🟥🟥⬜🟧🟧🟧🟪
🟩🟥⬜⬜⬜🟧🟪🟪🟪
🟩🟥🟥🟥⬜🟧🟧🟧🟫
🟩⬜⬜⬜⬜🟧🟨🟧🟫
🟩⬜⬜⬜⬜🟧🟧🟧🟫
🟩🟩⬛⬛⬛⬛⬛🟫🟫

### minisudoku
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 3 ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃ 2 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛

### patches
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +4 | .. | +4 | .. |
+----+----+----+----+----+----+----+----+
| +2 | .. | +4 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |6 | .. | -2 | .. |
+----+----+----+----+----+----+----+----+
| +6 | .. | +  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +  | .. | +6 |
+----+----+----+----+----+----+----+----+
| .. | |6 | .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +2 | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | +4 | .. | +4 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+

### wend
+---+---+---+---+---+---+---+
| O | K | H | # | K | S | T |
+---+---+---+---+---+---+---+
| D | U | O | A | C | O | R |
+---+---+---+---+---+---+---+
| U | S | O | B | C | K | E |
+---+---+---+---+---+---+---+
| O | # | K | # | O | # | K |
+---+---+---+---+---+---+---+
| U | O | O | K | O | K | O |
+---+---+---+---+---+---+---+
| T | L | I | C | H | B | O |
+---+---+---+---+---+---+---+
| A | R | T | # | O | K | E |
+---+---+---+---+---+---+---+

Words:
  HOOK
  SUDOKU
  OUTLOOK
  COOKBOOK
  ARTICHOKE
  BACKSTROKE

### pinpoint
  1. Bell
  2. Valves
  3. Tuning slide
  4. Mouthpiece
  5. Metal tubing (muted gold/yellow)

  answer (5 blanks): Parts of a brass instrument (like a trumpet)!

### crossclimb
  cold    
  told    
  toed    
  teed    
  teen    
  keen    
  keep    

Clues (middle rows):
  - Open-___ shoes
  - Someone older than twelve but younger than twenty
  - Relayed, as a story
  - Very interested in something
  - Ready to be hit, as a golf ball

Phrase (top+bottom): The top + bottom rows = A two-word phrase meaning "to refrigerate." Keep in mind: The first word may be at the bottom.
<!-- DAILY-GAMES-END -->
