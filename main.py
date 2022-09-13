try:
    import time
    from pyrogram import *
    from pyrogram.types import *
    import requests

    api_id = 8
    api_hash = ""
    bot = ""

    channel = -111 # id canale

    b = requests.get("https://blockchain.info/ticker").json()
    dollar = b["USD"]["last"]
    minutes = 104

    client = Client("btcsourceclone", api_id, api_hash, bot_token=bot)
    client.start()

    while True:
        client.send_message(channel, f"{dollar}$")
        time.sleep(int(minutes))
except KeyboardInterrupt:
    exit("Script successfully stopped ...")

