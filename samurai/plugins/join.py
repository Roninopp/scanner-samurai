import asyncio
import json

from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant, FloodWait

from samurai import pbot, ubot, SPAM_GROUP, SUDO_USERS


@pbot.on_message(
    filters.command(["userbotjoin", "botjoin", "join"]) & ~filters.private & ~filters.bot
)
async def joinchat(client, message):
    if message.from_user.id not in SUDO_USERS:
        await message.reply_text(
            "You need to be part of the Samurai to use this",
        )
        return

    if "@" in message.text:
        Test = message.text.split(" ")
        username = Test[1].replace("@", "")
    else:
        await message.reply_text("Format: /join @username")
        return

    try:
        user = await ubot.get_me()
    except:
        user.first_name = "Samurai"
    try: 
        await ubot.join_chat(f"@{username}")
    except UserAlreadyParticipant:
        await message.reply_text(
            f"🔴 **{user.first_name} already join this group !!**",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"❌ **Assistant ({user.first_name}) can't join your group due to many join requests for userbot!**\n‼️ Make sure the user is not banned in the group."
            f"\n\n» `Manually add the {user.first_name} to your group`",
        )
        return
    

@pbot.on_message(
    filters.command(["joinhere"]) & ~filters.private & ~filters.bot
)
async def addchannel(client, message):
    if message.from_user.id not in SUDO_USERS:
        await message.reply_text(
            "You need to be part of the Samurai to use this",
        )
        return
    try:
        invite_link = await message.chat.export_invite_link()
        if "+" in invite_link:
            kontol = (invite_link.replace("+", "")).split("t.me/")[1]
            link_bokep = f"https://t.me/joinchat/{kontol}"
    except:
        await message.reply_text(
            "**Add me admin first**",
        )
        return

    try:
        user = await ubot.get_me()
    except:
        user.first_name = "Samurai"

    try:
        await ubot.join_chat(link_bokep)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"🔴 **{user.first_name} already join this group !!**",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"❌ **Assistant ({user.first_name}) can't join your group due to many join requests for userbot!**\n‼️ Make sure the user is not banned in the group."
            f"\n\n» `Manually add the {user.first_name} to your group`",
        )
        return


@ubot.on_message(filters.group & command(["userbotleave", "leave"]))
async def rem(USER, message):
    if message.from_user.id not in SUDO_USERS:
        await message.reply_text(
            "You need to be part of the Samurai to use this",
        )
        return
    try:
        await ubot.send_message(
            message.chat.id,
            "✅ ᴜsᴇʀʙᴏᴛ ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ....",
        )
        await ubot.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **Assistant can't leave your group! probably waiting for floodwaits**\n\n» Manually remove me from your group</b>"
        )

        return

