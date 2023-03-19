from samurai import pbot, OWNER_ID, SUDOLIST, SUPPORT_USERS, SUPPORTLIST, DEV_LIST, DEV_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message


@Client.on_message(filters.command("sudolist", prefixes="?"))
async def disaster(_, message: Message):
    if message.from_user.id not in SUPPORT_USERS:
        return await message.reply_text("ONLY FOR APPROVED USERS!!")

    final = "Members of the Team Samurai:\n\nENFORCERS:\n"
    for dev in DEV_LIST:
        try:
            user = pbot.get_users(dev)
            devname = user.first_name
        except:
            devname = "Dev"

        final += f"✯ [{devname}](tg://openmessage?user_id={dev})\n"
    for enforcer in SUDOLIST:
        try:
            user = pbot.get_users(enforcer)
            devname = user.first_name
        except:
            devname = "Dragon"

        final += f"✯ [{devname}](tg://openmessage?user_id={enforcer})\n"
    final += "\nINSPECTORS:\n"
    for inspector in SUPPORTLIST:
        try:
            user = pbot.get_users(inspector)
            devname = user.first_name
        except:
            devname = "Demon"

        final += f"۞ [{devname}](tg://openmessage?user_id={inspector})\n"
    
    await message.reply_text(final)


@Client.on_message(filters.command("logs", prefixes="?"))
async def logs(_, message: Message):
    if message.from_user.id in DEV_USERS:
        chat = message.chat
        user = message.from_user
        with open("logs.txt", "rb") as f:
            await pbot.send_document(document=f, chat_id=user.id)
            await message.reply_text("`Logs sent, check your pm`")
    
    else:
        await message.reply_text("ᴏɴʟʏ ᴅEvs ᴄᴀɴ ᴅᴏ ᴛʜɪs !!")