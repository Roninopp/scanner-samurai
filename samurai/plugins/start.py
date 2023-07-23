from samurai import pbot, ubot, SUPPORT_CHAT, StartTime
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time

bancodes = """
HERE IS A HELP BANCODES OF SAMURAI SCANNER:-
• `{SERx00}` - Scammer
• `{SERx01}` - SPAM ADDING MEMBER
• `{SERx02}` - CHILD ABUSE
• `{SERx03}` - ILLEGAL
• `{SERx04}` - FRAUD PROMOTION OR[ANY KIND]
• `{SERx05}` - PHISHING
• `{SERx06}` - BAN EVASION
• `{SERx07}` - RAID/SPAM INFLAMED
• `{SERx08}` - ADDING SPAMBOTS/RAIDERS
• `{SERx09}` - KRIMINALANT
• `{SERx10}` - SCAMMER
• `{SERx11}` - ABUSE SPAM
• `{SERx12}` - IMPERSONATION
• `{SERx13}` - MD/BTC SCAM
• `{SERx14}` - RAID INITIALIZER
• `{SERx15}` - RAID PARTICIPANT
• `{SERx16}` - SPAMBOT
• `{SERx17}` - CYBER THREATENING / CYBER BULLY
• `{SERx18}` - NSFW SPAMMER

𖣘POWERED BY𖣘 - @TEAMSAMURAII
"""


@Client.on_message(filters.command("start") & filters.private)
async def start_all(_, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bb = await message.reply_text("`Checking Your Information Please wait...`")
    await asyncio.sleep(1)
    await message.reply_video(
        video="https://telegra.ph/file/56e50c3613bf7a02e31b7.mp4",
        caption=f"""
WELCOME!! [{user_name}](tg://openmessage?user_id={user_id})
─────────────────
I'm an Advanaced Anti-Spam Cymatic Scanner based on API
Created and developed For removing toxic people from telegram
𖣘 I can protecc you from potential threats on telegram.
𖣘 You can request gban/scan for anyone in our Support Group
𖣘 clash mania can be connected with any bots

⍟ Powered by Team Samurai network
─────────────────""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="about_call"),
                    InlineKeyboardButton(text="ʙᴀɴᴄᴏᴅᴇꜱ⁪⁬⁮⁮⁮⁮", callback_data="bancode_call")
                ],
                [
                    InlineKeyboardButton(text="ɴᴇᴛᴡᴏʀᴋ", url="https://t.me/teamsamuraii"),
                    InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ-ɢʀᴏᴜᴘ", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )
    await bb.delete()



@Client.on_callback_query(filters.regex("about_call"))
async def about_commands_callbacc(_, CallbackQuery):
    await CallbackQuery.message.edit_caption(
        f"""
━━━━━━━━━━━━━━━━━━
THIS SCANNER IS CREATED FOR REMOVE TOXIC PEOPLE'S FROM TELEGRAM THIS ISS OFFICIAL SCANNER OF @TEAM_SAMURAII OUR SUPPORT @spiralsupport
YOU CAN SEND REPORT OF USER BY USING /report bancodes + telegraph proof WE WILL APPROVE YOUR REQUEST SOON
━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Team Samurai", url="https://t.me/teamsamuraii")
                ],
                [
                    InlineKeyboardButton(text="【OWNER】", url="https://t.me/DushmanXRonin"),
                    InlineKeyboardButton(text="𖣘DEV𖣘", url="https://t.me/ishikki_akabane")
                ],
                [
                    InlineKeyboardButton(text="Back", callback_data="home_call")
                ]
            ]
        )
    )

@Client.on_message(filters.command("bancode"))
async def bancode(_, message: Message):
    await message.reply_text(bancode_text)


@Client.on_callback_query(filters.regex("bancode_call"))
async def bancodes_commands_callbacc(_, CallbackQuery):
    await CallbackQuery.message.edit_caption(
        caption=bancodes,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Back", callback_data="home_call")
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("home_call"))
async def home_commands_callbacc(_, CallbackQuery):
    await CallbackQuery.message.edit_caption(
        """
WELCOME!!
─────────────────
I'm an Advanaced Anti-Spam Cymatic Scanner based on API
Created and developed For removing toxic people from telegram
𖣘 I can protecc you from potential threats on telegram.
𖣘 You can request gban/scan for anyone in our Support Group
𖣘 clash mania can be connected with any bots

⍟ Powered by Team Samurai network
─────────────────""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="『ABOUT』⁪⁬⁮⁮⁮⁮", callback_data="about_call"),
                    InlineKeyboardButton(text="『BANCODES』⁪⁬⁮⁮⁮⁮", callback_data="bancode_call")
                ],
                [
                    InlineKeyboardButton(text="『NETWORK』⁪⁬⁮⁮⁮⁮", url="https://t.me/team_samuraii"),
                    InlineKeyboardButton(text="『SUPPORT GROUP』⁪⁬⁮⁮⁮⁮", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Client.on_message(filters.command(["start", "ping"], prefixes="?") & ~filters.private)
async def start_grp(_, message: Message):
    user_id = message.from_user.id
    uptime = get_readable_time((time.time() - StartTime))
    await message.reply_text("𝙰𝙻𝙸𝚅𝙴 𝚂𝚒𝚗𝚌𝚎:\n`{}`".format(uptime))


@ubot.on_message(filters.command(["start", "ping"], prefixes="?") & ~filters.private)
async def ubstart_grp(_, message: Message):
    user_id = message.from_user.id
    uptime = get_readable_time((time.time() - StartTime))
    await message.reply_text("𝙰𝙻𝙸𝚅𝙴 𝚂𝚒𝚗𝚌𝚎:\n`{}`".format(uptime))
