from samurai import pbot, tbot, OWNER_ID, SUDOLIST, DEV_LIST, SUPPORTLIST
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import random
from samurai.utils.scan_help import check_gban


@Client.on_message(filters.command(["info", "check"]))
async def info(_, message: Message):
    if len(message.text.split(" ")) < 2:
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            user_id = user.id
            user_first_name = user.first_name
            try:
                user_last_name = user.last_name
                user_name = user_first_name + " " + user_last_name
            except:
                user_name = user_first_name
        else:
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name
            try:
                user_last_name = message.from_user.last_name
                user_name = user_first_name + " " + user_last_name
            except:
                user_name = user_first_name
    else:
        splitted = message.text.split(" ")
        try:
            user = await pbot.get_users(int(splitted[1]))
        except:
            await message.reply_text(f"I dont know that user!!!")
            return

        user_id = user.id
        user_first_name = user.first_name
        try:
            user_last_name = user.last_name
            user_name = user_first_name + " " + user_last_name
        except:
            user_name = user_first_name

    check = check_gban(user_id)
    if check == False:
        crime = random.randint(100, 175)
        textt = f"""
> INFO:-

> User ID: {user_id}
> Name: {user_name}
> Crime Co.: {crime}
> Status: Not Scanned
"""
        await message.reply_text(textt)
    else:
        crime = "Above 200"
        textt = f"""
> INFO:-

> User ID: {user_id}
> Name: {user_name}
> Crime Co.: {crime}
> Status: Scanned
"""