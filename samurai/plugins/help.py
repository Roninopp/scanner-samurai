from samurai import pbot, ubot, SUPPORT_CHAT, SUPPORT_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import time


@ubot.on_message(filters.command("help", prefixes="?"))
async def start_all(_, message: Message):
    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return

    try:
        tex = message.text.split(" ")[1]
    except:
        textt = """
HELP: use like this-
?help <command name>

COMMANDS:
```scan
REVERT
DEV
WHOIS
FLAGS
BANCODES
EXTRAS```
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
    elif tex.upper() in ["BANCODES"]:
        textt = """
HERE IS A HELP BANCODES OF SAMURAI SCANNER:-
• `{TSSx00}` - Scammer
• `{TSSx01}` - SPAM ADDING MEMBER
• `{TSSx02}` - CHILD ABUSE
• `{TSSx03}` - ILLEGAL
• `{TSSx04}` - FRAUD PROMOTION  [ANY KIND]
• `{TSSx05}` - PHISHING
• `{TSSx06}` - BAN EVASION
• `{TSSx07}` - RAID/SPAM INFLAMED
• `{TSSx08}` - ADDING SPAMBOTS/RAIDERS
• `{TSSx09}` - KRIMINALANT
• `{TSSx10}` - SCAMMER
• `{TSSx11}` - ABUSE SPAM
• `{TSSx12}` - IMPERSONATION
• `{TSSx13}` - MD/BTC SCAM
• `{TSSx14}` - RAID INITIALIZER
• `{TSSx15}` - RAID PARTICIPANT
• `{TSSx16}` - SPAMBOT
• `{TSSx17}` - CYBER THREATENING / CYBER BULLY
• `{TSSx18}` - NSFW SPAMMER
"""
    else:
        textt = "Invalid!! help"
    await message.reply_text(textt)
