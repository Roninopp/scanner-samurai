from samurai import pbot, ubot, SUPPORT_CHAT, StartTime
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time


@Client.on_message(filters.command("start"))
async def start_all(_, message: Message):
    await message.reply_text("I'm alive my master")