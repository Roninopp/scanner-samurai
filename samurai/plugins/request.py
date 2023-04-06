from samurai import pbot, OWNER_ID, REQUEST_IMG, SUDOLIST, DEV_LIST, SUPPORT_ID
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User

REQUEST_STRING = """
──────────────────
USER ID: `{}`
NAME: [{}](tg://openmessage?user_id={})
TARGET USER: {}
TARGET NAME: [{}](tg://openmessage?user_id={})
REASON: {}
──────────────────
"""

@Client.on_message(filters.command(["appeal", "reqgban"], prefixes="?"))
async def request(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    if message.from_user.id in DEV_LIST:
        return await message.reply_text("LMAO, why dev requesting for scanning???")
    elif message.from_user.id in SUDOLIST:
        return await message.reply_text("LOL, why disturbing me for this small things ?")
    elif message.from_user.id in OWNER_ID:
        return await message.reply_text("WOW LAZYYYYYY!!! Get your ass moving and give the scan command by yourself")
    
    if len(message.text.split(" ")) < 2:
        return await message.reply_text("Usage:\n/request **userid** **reason** **proof**")
    else:
        try:
            split_id = int(message.text.split(" ")[1])
        except:
            return await message.reply_text("user id invalid!!!\n/request *userid* *reason*")
        try:
            spliting = message.text.split(None, 1)[1]
            reason = spliting.split(None, 1)[1]
        except:
            return await message.reply_text("Provide a reason also\n/request *userid* *reason*")
        try:
            user = pbot.get_users(split_id)
            target_id = user.id
            target_name = user.first_name
        except:
            target_id = split_id
            target_name = "None"
        
        await message.reply_text("Request successfully sent!!\nYou may get a pm message or reply by one of the admin for Inspection\nThankYou :)")
        await pbot.send_message(SUPPORT_ID, REQUEST_STRING.format(user_id, user_name, user_id, target_id, target_name, target_id, reason))