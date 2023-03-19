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