from samurai import pbot, tbot, ubot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT, SUPPORT_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update
import asyncio
import time


@ubot.on_message(filters.command("sysinfo", prefixes="?") & ~filters.private)
async def ubscan(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id in SUPPORT_USERS:
        msg = await message.reply_text("Hold on have Give me a second Featching the Node Status")
        await asyncio.sleep(1)
        await msg.edit_text("`CONNECTING to Team samurai X scanner ■□□□□□`")
        await asyncio.sleep(1)
        await msg.edit_text("`CONNECTING ■■□□□□`")
        await asyncio.sleep(1)
        await msg.edit_text("`CONNECTING ■■■□□□`")
        await asyncio.sleep(1)
        await msg.edit_text("`CONNECTING ■■■■□□`")
        await asyncio.sleep(1)
        await msg.edit_text("`CONNECTING ■■■■■□`")
        await asyncio.sleep(1)
        await msg.edit_text("**CONNECTION SUCESSFULL ■■■■■■**")
        await asyncio.sleep(1)
        await msg.edit_text("`❇ 『YOU ARE VERYFIED USER』 ❇`")
        await asyncio.sleep(2)
        await msg.edit_text("*Version = v16.9.1\n\n*Codename = Gallium\n\n*Status = LTS\n\n*Total Core = 2")
        await asyncio.sleep(3)
        await msg.edit_text("Welcome to Team Samurai system\n\n¤ 💎You Are Veryfied user💎\n\n Scan with proof.")
    else:
        msg = await message.reply_text("Hold on have Give me a second Featching the Node Status")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTING to Team samurai X scanner ■□□□□□")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTING ■■□□□□")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTING ■■■□□□")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTING ■■■■□□")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTING ■■■■■□")
        await asyncio.sleep(1)
        await msg.edit_text("CONNECTION SUCESSFULL ■■■■■■")
        await asyncio.sleep(1)
        await msg.edit_text("❇ 『YOU ARE NOT A VERYFIED USER』 ❇")

 
