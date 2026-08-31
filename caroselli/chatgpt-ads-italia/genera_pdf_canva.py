# -*- coding: utf-8 -*-
"""Converte l'HTML del carosello in un PDF di 8 pagine da 1080x1350 px.

Canva importa il PDF mantenendo il testo come livello modificabile: e' la via
piu' compatibile quando l'import da HTML non e' disponibile.
"""

import asyncio
import os

from playwright.async_api import async_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "chatgpt_ads_italia_canva.html")
OUT = os.path.join(BASE, "chatgpt_ads_italia_canva.pdf")

# Su questa macchina Chromium e' gia' installato: si evita "playwright install".
CHROME = os.environ.get("VG_CHROME", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome")


async def main():
    async with async_playwright() as p:
        avvio = {"executable_path": CHROME} if os.path.exists(CHROME) else {}
        browser = await p.chromium.launch(**avvio)
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        await page.goto(f"file://{SRC}")
        await page.wait_for_timeout(1500)
        await page.pdf(path=OUT, width="1080px", height="1350px",
                       print_background=True, margin={"top": "0", "right": "0",
                                                      "bottom": "0", "left": "0"})
        await browser.close()
    print("OK", OUT, os.path.getsize(OUT), "byte")


asyncio.run(main())
