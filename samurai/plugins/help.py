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
fscan: **?fscan <id> <reason>**
frevert: **?frevert <id>**
id: Shows the user_id
Whois: Shows the info about the user in the database
token: Use it to get your token for the api
Eval : ONLY INSPECTORS AND OWNER COMMAND
sudolist: Shows the list of disasters
scanlist: Shows the list of people who are scanned
logs: Only for developers
"""
    await message.reply_text(textt)
