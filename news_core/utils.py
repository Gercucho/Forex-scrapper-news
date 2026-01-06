import random
import asyncio

async def escribir_humano(page, texto):
    """Teclea como una persona."""
    for char in texto:
        delay = random.uniform(0.05, 0.15) 
        await page.keyboard.type(char, delay=delay * 1000) 

async def mover_mouse_erratico(page):
    """Mueve el mouse para despertar antibots."""
    x = random.randint(100, 800)
    y = random.randint(100, 600)
    await page.mouse.move(x, y, steps=15)