from samurai import pbot, ubot, SUPPORT_CHAT
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import time


@Client.on_message(filters.command("help", prefixes="?"))
async def start_all(_, message: Message):
    textt = """
Help:

scan: **?scan <flag> <id> <reason> <bancode> <prooflink>**
revert: **?revert <id>**

"""
    await message.reply_text(textt)