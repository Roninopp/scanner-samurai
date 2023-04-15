from samurai import pbot, tbot, OWNER_ID, SUDOLIST, DEV_LIST, SUPPORTLIST, ubot, SUPPORT_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton
import random
from samurai.utils.scan_help import check_gban, gban_data


@ubot.on_message(filters.command(["whois", "tsinfo"], prefixes="?"))
async def info(_, message: Message):
    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Enforcers can use this.")

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
            usertag = user.username
            if usertag == None:
                usertag = "None"
            is_bot = user.is_bot
            is_restricted = user.is_restricted
            #bio = user.bio or "This User has no About"
        else:
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name
            try:
                user_last_name = message.from_user.last_name
                user_name = user_first_name + " " + user_last_name
            except:
                user_name = user_first_name
            usertag = message.from_user.username
            if usertag == None:
                usertag = "None"
            is_bot = message.from_user.is_bot
            is_restricted = message.from_user.is_restricted
            #bio = message.from_user.bio or "This User has no About"
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
        usertag = user.username
        if usertag == None:
            usertag = "None"
        is_bot = user.is_bot
        is_restricted = user.is_restricted
        #bio = user.bio or "This User has no About"

    dc_id = _.get_dc_id()
    check = check_gban(user_id)
    if check == False:
        crime = random.randint(100, 175)
        textt = f"""
USER INFO in team samurai Database:

𖣘 Name: {user_name}
𖣘 Username: @{usertag}
𖣘 ID: {user_id}
𖣘 Data Centre ID: {dc_id}
𖣘 Is Bot: {is_bot}
𖣘 Is Restricted: {is_restricted}
𖣘 Is Verified by Telegram: False
「✪」Is Scanned: False

𖣘 Permanent Link To Profile: [TS-USER](tg://openmessage?user_id={user_id})
"""
        await message.reply_text(textt)
    else:
        crime = "Above 200"
        reason, proof, bancode, enforcer = gban_data(user_id)
        textt = f"""
USER INFO in team samurai Database:

𖣘 Name: {user_name}
𖣘 Username: @{usertag}
𖣘 ID: {user_id}
𖣘 Data Centre ID: {dc_id}
𖣘 Is Bot: {is_bot}
𖣘 Is Restricted: {is_restricted}
𖣘 Is Verified by Telegram: False
「✪」Is Scanned: True

𖣘 Permanent Link To Profile: [TS-USER](tg://openmessage?user_id={user_id})
"""
        await message.reply_text(textt)
