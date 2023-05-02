from samurai import pbot, tbot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT, SUPPORT_USERS
from samurai.utils.token_help import token_save, check_token
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update
import requests

api_url = ""
api_token = ""

def create_token(user_id):
    user_id = str(user_id)
    a = random.randint(0, 5)
    b = random.randint(0, 5)
    c = ["blade-", "katana-", "dagger-", "poisen-"]
    d = ["a-division", "b-division", "c-division", "d-division", "e-division", "f-divison"]
    e = random.randint(999, 9999)
    f = e*e+e*e*e+e-e*e+e
    aa = "samurai-" + str(f) + "-" + user_id + "-" + c[a] + d[b]
    return aa


@Client.on_message(filters.command("token"))
async def token_gen(_, message: Message):
    user_id = message.from_user.id

    result, level, api_token = check_token(str(user_id))
    if result == True:
        return await message.reply_text(f"Your {level} level token:\n`{api_token}`")
    else:
        tokenn = create_token(user_id)
        level = "ENFORCER"

        token_save(str(user_id), tokenn, level)
        await message.reply_text(f"INSPECTOR level Token created successfully!\n\n`{tokenn}`")

        creation = token_save(str(user_id), tokenn, level)
        if creation != "DONE!!":
            await message.reply_text(f"Opps!!\nTechnical error, please inform the [developers](https://t.me/{SUPPORT_CHAT}] that your token not activated!")
        else:
            await message.reply_text(f"YOUR TOKEN ACTIVATED!!")
