from samurai import pbot, ubot, SUPPORT_CHAT, StartTime
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import time

bancodes = """
Bro i dont know what to set here, please you set it
"""


@Client.on_message(filters.command("start", prefixes="/") & filters.private)
async def start_all(_, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    bb = await message.reply_text("`COLLECTING YOUR DB...`")
    await asyncio.sleep(1)
    await message.reply_photo(
        photo="https://graph.org/file/982ad57f6a06f5325e6bd.jpg",
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
                    InlineKeyboardButton(text="ABOUT", callback_data="about_call"),
                    InlineKeyboardButton(text="Bancodes", callback_data="bancode_call")
                ],
                [
                    InlineKeyboardButton(text="Network", url="https://t.me/team_samuraii"),
                    InlineKeyboardButton(text="Support Group", url=f"https://t.me/{SUPPORT_CHAT}")
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
                    InlineKeyboardButton(text="Team Samurai", url="https://t.me/team_samuraii")
                ],
                [
                    InlineKeyboardButton(text="Owner", url="https://t.me/DushmanXRonin"),
                    InlineKeyboardButton(text="Dev", url="https://t.me/ishikki_akabane")
                ],
                [
                    InlineKeyboardButton(text="Back", callback_data="home_call")
                ]
            ]
        )
    )

@Client.on_message(filters.command("bancode"))
async def bancode(_, message: Message):
    bancode_text = "Bancodes for Kazuma Clan:\n"
    bancode_text += bancodes
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
                    InlineKeyboardButton(text="ABOUT", callback_data="about_call"),
                    InlineKeyboardButton(text="Bancodes", callback_data="bancode_call")
                ],
                [
                    InlineKeyboardButton(text="Network", url="https://t.me/team_samuraii"),
                    InlineKeyboardButton(text="Support Group", url=f"https://t.me/{SUPPORT_CHAT}")
                ]
            ]
        )
    )


@Client.on_message(filters.command(["start", "ping"], prefixes="?") & ~filters.private)
async def start_grp(_, message: Message):
    user_id = message.from_user.id
    uptime = get_readable_time((time.time() - StartTime))
    await message.reply_text("𝙰𝙻𝙸𝚅𝙴 𝚂𝚒𝚗𝚌𝚎:\n`{}`".format(uptime))
