    System,
    system_cmd,
    make_collections,
    INSPECTORS,
    ENFORCERS,
    Sibyl_logs,
)
from telethon import TelegramClient, events, Button, types, functions, errors
from samurai.strings import on_string
import logging
import importlib
import asyncio
import time


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
System.on(system_cmd(pattern=r"sysinfo", allow_enforcer=True))
async def sysinfo(event):
    msg = await event.reply("Hold on have Give me a second Featching the Node Status.")
    time.sleep(1)
    await msg.edit("CONNECTING to Team samurai X scanner ■□□□□□")
    time.sleep(1)
    await msg.edit("CONNECTING ■■□□□□")
    time.sleep(1)
    await msg.edit("CONNECTING TO TEAM SAMURAI ■■■□□□")
    time.sleep(1)
    await msg.edit("CONNECTING TO TEAM SAMURAI ■■■■□□")
    time.sleep(1)
    await msg.edit(" CONNECTION SUCESSFULL ■■■■■□")
    time.sleep(1)
    await msg.edit("❇ 『YOU ARE VERYFIED USER』 ❇")
    time.sleep(1)
    await msg.edit("*Version = v16.9.1\n\n*Codename = Gallium\n\n*Status = LTS\n\n*Total Core = 2")
    time.sleep(2)
    sender = await event.get_sender()
    user_status = "Inspector" if sender.id in INSPECTORS else "Enforcer"
    time.sleep(1)
    await msg.edit("Welcome to Team Samurai system\n\n¤ 💎You Are Veryfied user💎\n\n Scan with proof.")
    
    await msg.edit(on_string.format(Enforcer=user_status, name=sender.name))
 
