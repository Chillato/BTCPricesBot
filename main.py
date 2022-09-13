try:
    import time
    from pyrogram import *
    from pyrogram.types import *
    import asyncio, requests

    api_id = 8
    api_hash = ""
    bot = ""

    canale = -111 # id canale

    b = requests.get("https://blockchain.info/ticker").json()
    dollar = b["USD"]["last"]
    minuti = 104

    client = Client("btcsourceclone", api_id, api_hash, bot_token=bot)
    client.start()

    while True:
        client.send_message(canale, f"{dollar}$")
        time.sleep(int(minuti))
except KeyboardInterrupt:
    exit("Script fermato con successo...")

