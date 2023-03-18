from samurai import pbot, tbot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT, SUPPORT_USERS, ubot

from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update


@Client.on_message(filters.command("fscan", prefixes="?") & ~filters.private)
async def fscan(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Inspectors can use this.")
    
    stext = message.text
    if len(stext.split(" ")) < 2:
        await message.reply_text("Atleast give something to revert\nusage: ?fscan <id> <reason>")
        return

    try:
        splitted = stext.split(None, 1)[1]
        target_id = splitted.split(" ")[0]
        reason = splitted.split(None, 1)[1]
        target_id = int(target_id)
    except:
        await message.reply_text("Wrong format!!\n: ?fscan <id> <reason>")
        return

    await message.reply_text(f"FScanning [the user](tg://openmessage?user_id={target_id}) !!!")

    try:
        await ubot.send_message(SPAM_GROUP, f"/fban {target_id} {reason}")
    except Exception as e:
        return await message.reply_text(f"ERROR!!")


@Client.on_message(filters.command("frevert", prefixes="?") & ~filters.private)
async def unfscan(_: Update, message: Message):
    user_id = message.from_user.id
    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Inspectors can use this.")
    
    stext = message.text
    if len(stext.split(" ")) < 2:
        await message.reply_text("Atleast give something to revert\nusage: ?frevert <id>")
        return
    
    try:
        splitted = stext.split(None, 1)[1]
        target_id = int(splitted)
    except:
        await message.reply_text(f"wrong format!!\nusage: /unfscan **id**")
        return
    
    try:
        await ubot.send_message(SPAM_GROUP, f"/unfban {target_id}")
    except Exception as e:
        return await message.reply_text(f"ERROR")
    await message.reply_text(f"unfscanning is completed!! [User](tg://openmessage?user_id={target_id}) is now unfbanned in our Samurai Federation")