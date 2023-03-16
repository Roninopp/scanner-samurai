from samurai import pbot, tbot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT, SUPPORT_USERS
from samurai.utils.idform import createform

from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update
import random
from datetime import datetime
import time
from PIL import Image, ImageOps, ImageDraw

from samurai.strings import scan_request_u
#from samurai.utils.scan_help import check_gban, gban_save1, gban_save2, gban_save3, revert_save
#from samurai.plugins.api_key import scan_api, revert_api
#from samurai.utils.bancode_help import bancode_convo
import asyncio

datetime_fmt = "%Y-%m-%d"


#/scan -f 243475585 spamming my gc for fun KCBX021 https://gdfhgjdfg
def splitting(text):
    text = text.upper()
    remove_cmd = text.split(None, 1)[1]
    flag = remove_cmd.split(" ")[0]
    remove_flag = remove_cmd.split(None, 1)[1]
    target_id = remove_flag.split(" ")[0]
    remove_id = remove_flag.split(None, 1)[1]
    dividee = remove_id.partition("KCBX")
    reason = dividee[0]
    divide_reason = remove_id.partition(reason)[2]
    bancode = divide_reason.split(" ")[0]
    proof = divide_reason.split(None, 1)[1]
    proof = proof.lower()
    reason = reason.lower()
    target_id = int(target_id)
    return flag, target_id, reason, bancode, proof


@Client.on_message(filters.command("scan") & ~filters.private)
async def scan(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Inspectors can use this.")

    user_name = message.from_user.first_name
    stext = message.text
    if len(stext.split(" ")) < 2:
        await message.reply_text("Atleast give something to scan\nbruhh -_-\nusage: ?scan *id* *reason* *bancode* *prooflink*")
        return
    try:
        flag, target_id, reason, bancode, proof = splitting(stext)
        bancode = bancode.upper()
    except Exception as e:
        await message.reply_text(f"wrong format!!\nusage: ?scan **id** **reason** **bancode** **prooflink**")
        print(e)
        return

    try:
        target = await pbot.get_users(target_id)
        target_name = target.first_name
        tuser_id = await tbot.get_entity(target_id)
    except Exception as e:
        await message.reply_text(f"I dont know that user!!!\nPlease forward his/her message here and do ?info first")
        print(e)
        return

    try:
        pfp = await tbot.download_profile_photo(target_id, file="user_pfp.jpg", download_big=True)
        result1 = createform(target_name, pfp=True)
    except:
        result1 = createform(target_name, pfp=None)

    if flag == "-R":
        user_idint = int(target_id)
        case = user_idint//100000 + 1928
        crime_co = 200
        await _.send_photo(
            chat_id=GBAN_CHANNEL_ID,
            photo="user_form.png",
            caption=scan_request_u.format(case_id, user_name, target_name, target_id, reason, proof, bancode),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Accept", callback_data="accept_call"),
                        InlineKeyboardButton(text="Reject", callback_data="reject_call")
                    ],
                    [
                        InlineKeyboardButton(text="Event", url=f"https://t.me/{SUPPORT_CHAT}/{message.id}")
                    ]
                ]
            )
        )