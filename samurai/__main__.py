import asyncio
import requests
import random
import os
from pyrogram import Client
from pytgcalls import idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from samurai import LOGGER, pbot, tbot, ubot, BOT_TOKEN, API_HASH, API_ID, SUPPORT_CHAT, SUPPORT_ID, DOWNLOAD_DIRECTORY, GBAN_CHANNEL_ID 


async def load_start():
    LOGGER.info("[INFO]: STARTED")
    
    try:
        await pbot.send_message(
            int(SUPPORT_ID),
            f"BOT STARTED SUCCESSFULLY..!\nPyorgram Version: `2.0.97`\nScanner Version = `L.9.2`/n Total Storage = `70.6Mb`",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Scan report", url=f"https://t.me/serenity_systembot"),
                        InlineKeyboardButton(text="My LOGS", url=f"https://t.me/Serenity_log")
                    ]
                ]
            )
        )
        await pbot.send_message(GBAN_CHANNEL_ID, f"Pyrogram Client Started Successfully!!")
        LOGGER.info("[INFO]: PYROGRAM BOT STARTED")
    except Exception as e:
        LOGGER.info(f"Bot wasn't able to send message in your log channel\n\nERROR: {e}")

    try:
        await ubot.send_message(
            int(SUPPORT_ID), f"Assistant Started Successfully!!"
        )
        LOGGER.info("[INFO]: PYROGRAM USERBOT STARTED")
    except Exception as e:
        LOGGER.info(f"UserBot wasn't able to send message in your log channel.\n\nERROR: {e}")


loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

tbot.start(bot_token=BOT_TOKEN)

Client(
    name="ISHIKKI",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=min(32, os.cpu_count() + 4),
    workdir=DOWNLOAD_DIRECTORY,
    sleep_threshold=60,
    in_memory=True,
    plugins={"root": "samurai.plugins"},
).start()

idle()
loop.close()
