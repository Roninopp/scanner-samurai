from samurai import pbot, ubot, SUPPORT_CHAT, SUPPORT_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import time


@ubot.on_message(filters.command("help", prefixes="?"))
async def start_all(_, message: Message):
    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Enforcers can use this.")

    try:
        tex = message.text.split(" ")[1]
    except:
        textt = """
HELP: use like this-
?help <command name>

COMMANDS:
```scan
revert
dev
whois
flags
extra```
"""
        return await message.reply_text(textt)
    if tex.upper() in ["SCAN"]:
        textt = """
Help:

scan: **?scan <flag> <id> <reason> <bancode> <prooflink>**
eg: 
```?scan -f 9829035992 spamming TSX01 https://proof```

fscan: **?fscan <id> <reason>**
eg:
```?fscan 9829035992 spamming```

for flags, see ?help flags
"""
    elif tex.upper() in ["REVERT"]:
        textt = """
Help:

revert: **?revert <id>**
eg:
```?revert 9829035992```

frevert: **?frevert <id>**
eg:
```?frevert 9829035992```
"""
    elif tex.upper() in ["DEV"]:
        textt = """
Help:

Eval : ONLY DEVELOPERS AND OWNER COMMAND
sudolist: Shows the list of disasters
scanlist: Shows the list of people who are scanned
logs: Only for developers
"""
    elif tex.upper() in ["WHOIS"]:
        textt = """
Help:

id: Shows the user_id
Whois: Shows the info about the user in the database
"""
    elif tex.upper() in ["EXTRA"]:
        textt = """
Help:

token: Use it to get your token for the api
bancode: sends you the bancode
report, appeal:
sends a appeal to enforcers to scan that user
"""
    elif tex.upper() in ["FLAGS"]:
        textt = """
Help:

-f : Force the bot to scan the user, even if he is not identified by the bot
-r : Request a scan(For inspectors)
-g : Noraml Scan
"""
    else:
        textt = "Invalid!! help"
    await message.reply_text(textt)
