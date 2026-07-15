#!/usr/bin/env python3
import os
import asyncio
from datetime import date

from src.client import send_command


class GetGame:
    def __init__(self, game, attempts=10, board_selector=None):
        self.game = game
        self.url = f"https://www.linkedin.com/games/{game}"
        self.board_selector = board_selector
        self.today = date.today().strftime("%Y-%m-%d")
        self.attempts = attempts

    async def goto(self):
        return await send_command("goto", {"url": self.url})

    async def goto_desktop(self):
        return await send_command("goto", {"url": f"https://www.linkedin.com/games/view/{self.game}/desktop"})

    async def click(self, selector):
        return await send_command("click", {"target": selector})

    async def click_start_game(self):
        texts = ["Iniciar jogo", "Start game"]
        for _ in range(self.attempts):
            for text in texts:
                find = await send_command("find", {"text": text})
                for e in (find.get("data") or {}).get("elements", []):
                    if e.get("tag") in ("a", "button") and text in (e.get("text") or ""):
                        await send_command("click", {"target": e["selector"]})
                        return
            await asyncio.sleep(1)

    async def wait_for_board(self):
        if not self.board_selector:
            return True
        for _ in range(self.attempts):
            r = await send_command( "eval", {"expression": f"!!document.querySelector({self.board_selector!r})"})
            if (r.get("data") or {}).get("result"):
                return True
            await asyncio.sleep(1)
        return False

    async def html(self):
        return await send_command("html")

    async def save_html(self):
        resp = await self.html()
        html = resp.get("data") if isinstance(resp, dict) else resp
        os.makedirs(f"cache/{self.today}", exist_ok=True)
        with open(f"cache/{self.today}/{self.game}.html", "w", encoding="utf-8") as f:
            f.write(html or "")


# ---------------------------------------------------------------------------
# Per-game capture (kept explicit on purpose -- game-specific logic stays here)
# ---------------------------------------------------------------------------

async def zip():
    game = GetGame("zip", board_selector="div[data-cell-idx]")
    await game.goto_desktop()
    await asyncio.sleep(2)
    await game.wait_for_board()
    await game.save_html()


async def tango():
    game = GetGame("tango", board_selector="div[data-cell-idx]")
    await game.goto_desktop()
    await asyncio.sleep(2)
    await game.wait_for_board()
    await game.save_html()


async def queens():
    game = GetGame("queens", board_selector="div[data-cell-idx]")
    await game.goto_desktop()
    await asyncio.sleep(2)
    await game.wait_for_board()
    await game.save_html()


async def mini_sudoku():
    game = GetGame("mini-sudoku", board_selector="div[data-cell-idx]")
    await game.goto_desktop()
    await asyncio.sleep(2)
    await game.wait_for_board()
    await game.save_html()


async def patches():
    game = GetGame("patches", board_selector='div[data-testid="patches-game-board"]')
    await game.goto()
    await asyncio.sleep(2)
    await game.click_start_game()
    await game.wait_for_board()
    await game.save_html()


async def wend():
    game = GetGame("wend", board_selector='div[data-testid="wend-game-board"]')
    await game.goto()
    await asyncio.sleep(2)
    await game.click_start_game()
    await game.wait_for_board()
    # TODO: after the board is solved, the answer WORDS are shown in the DOM
    # (or revealed via a button). Extract them here once we automate solving.
    await game.save_html()


async def pinpoint():
    game = GetGame("pinpoint")
    await game.goto_desktop()
    await game.click_start_game() # "#launch-footer-start-button"
    for _ in range(5):
        await send_command("type", {"target": '.pinpoint__input', "text": '_'})
        await send_command("press", {"key": "Enter"}) 
    await game.save_html()


async def crossclimb():
    game = GetGame("crossclimb")
    await game.goto_desktop()
    await game.click_start_game()      # #launch-footer-start-button
    await game.click("#ember49")       # close the tutorial overlay
    for _ in range(5):
        await game.click("#ember46")   # reveal line
    return
    # TODO: order lines
    for _ in range(2):
        await game.click("#ember46")   # reveal line
    await game.save_html()


async def main():
    await zip()
    await tango()
    await queens()
    await mini_sudoku()
    await patches()
    await wend()
    # await pinpoint()
    # await crossclimb()


if __name__ == "__main__":
    asyncio.run(main())


GAME_NUMBER_ANCHOR = {
    "zip": (date(2026, 7, 13), 483),
    "tango": (date(2026, 7, 13), 644),
    "queens": (date(2026, 7, 13), 804),
    "wend": (date(2026, 7, 13), 35),
    "patches": (date(2026, 7, 13), 118),
    "mini-sudoku": (date(2026, 7, 15), 338),
}


def game_number(game, d=None):
    """Daily puzzle number = anchor_number + days since the anchor date."""
    anchor = GAME_NUMBER_ANCHOR.get(game)
    if not anchor:
        return None
    base_date, base_num = anchor
    d = d or date.today()
    return base_num + (d - base_date).days
