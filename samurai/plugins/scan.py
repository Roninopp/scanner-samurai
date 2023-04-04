from samurai import pbot, tbot, ubot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT, SUPPORT_USERS
from samurai.utils.idform import createform

from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update
import random
from datetime import datetime
import time
from PIL import Image, ImageOps, ImageDraw

from samurai.strings import scan_request_string, forced_scan_string, scan_approved_string, reject_string, scan_string
from samurai.utils.scan_help import check_gban, gban_save, revert_save
#from samurai.plugins.api import scan_api, revert_api
#from samurai.utils.bancode_help import bancode_convo



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


@Client.on_message(filters.command("scan", prefixes="?") & ~filters.private)
async def scan(_: Update, message: Message):

    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Inspectors can use this.")

    user_name = message.from_user.first_name
    stext = message.text
    if len(stext.split(" ")) < 2:
        await message.reply_text("Atleast give something to scan\nusage: ?scan **flag** **id** **reason** **bancode** **prooflink**")
        return

    try:
        flag, target_id, reason, bancode, proof = splitting(stext)
        bancode = bancode.upper()
    except Exception as e:
        await message.reply_text("wrong format!!\nusage: ?scan **flag** **id** **reason** **bancode** **prooflink**")
        print(e)
        return
    
    check = check_gban(target_id)
    if check == True:
        await message.reply_text("this user is already scanned in our database!")
        return

    user_idint = int(target_id)
    case = user_idint//100000 + 1928
    case_id = "#T" + str(case)

    if flag == "F":
        try:
            target = await pbot.get_users(target_id)
            target_name = target.first_name
        except:
            target_name = "Nodata"

        if user_id not in SUDO_USERS:
            return await message.reply_text("Only Enforcers can force me to scan!!!")

        await message.reply_text("Connecting to Host team-samurai-X for a Force CYBER gban scan........")

        gban_save(target_id, target_name, reason, proof, bancode, user_name)
        await _.send_photo(
            chat_id=GBAN_CHANNEL_ID,
            photo="sample1.png",
            caption=forced_scan_string.format(case_id, target_name, target_id, reason, proof, bancode, user_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Event", url=f"https://t.me/{SUPPORT_CHAT}/{message.id}")
                    ]
                ]
            )
        )
        await message.reply_text(scan_approved_string.format("#LethalEliminator", target_name, target_id, reason, user_name))
        await ubot.send_message(
            chat_id=SPAM_GROUP,
            text=f"/gban {target_id} {reason} Proof:{proof}"
        )
        return    
            
    try:
        target = await pbot.get_users(target_id)
        target_name = target.first_name
        tuser_id = await tbot.get_entity(target_id)
    except Exception as e:
        await message.reply_text("I dont know that user!!!\nPlease forward his/her message here and do ?info first\nor\nuse flag -f to do a force scan with just user id")
        print(e)
        return

    await message.reply_text("Connecting to Host team-samurai-X for a CYBER gban scan........")

    try:
        pfp = await tbot.download_profile_photo(target_id, file="user_pfp.jpg", download_big=True)
        result1 = createform(target_name, pfp=True)
    except:
        result1 = createform(target_name, pfp=None)

    crime_co = 200

    if flag == "-R":
        await _.send_photo(
            chat_id=GBAN_CHANNEL_ID,
            photo="user_form.png",
            caption=scan_request_string.format(case_id, target_name, target_id, reason, proof, bancode, user_name),
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
        await message.reply_text("Request Sent!!")
        return

    elif flag == "-G":
        if user_id not in SUDO_USERS:
            return await message.reply_text("Only Enforcers can make me scan!!!")

        gban_save(target_id, target_name, reason, proof, bancode, user_name)
        await _.send_photo(
            chat_id=GBAN_CHANNEL_ID,
            photo="user_form.png",
            caption=scan_string.format(case_id, target_name, target_id, reason, proof, bancode, user_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Event", url=f"https://t.me/{SUPPORT_CHAT}/{message.id}")
                    ]
                ]
            )
        )
        await message.reply_text(scan_approved_string.format("#LethalEliminator", target_name, target_id, reason, user_name))
        await ubot.send_message(
            chat_id=SPAM_GROUP,
            text=f"/gban {target_id} {reason} Proof:{proof}"
        )
    else:
        await message.reply_text("Invalid Flag!!!")


@Client.on_callback_query(filters.regex("accept_call"))
async def about_commands_callbacc(_, CallbackQuery):
    sender_id = CallbackQuery.from_user.id
    if sender_id in SUDO_USERS:
        stext = CallbackQuery.message.text
        flag, target_id, reason, bancode, proof = splitting(stext)
        user_name = CallbackQuery.from_user.first_name
        target = await pbot.get_users(target_id)
        target_name = target.first_name
        gban_save(str(target_id), target_name, reason, proof, bancode, user_name)
        await ubot.send_message(
            chat_id=SPAM_GROUP,
            text=f"/gban {target_id} {reason} Proof:{proof}"
        )
        await CallbackQuery.message.edit_caption(
            scan_approved_string.format("#LethalEliminator", target_name, target_id, reason, user_name),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Event", url=f"https://t.me/{SUPPORT_CHAT}/{message.id}")
                    ]
                ]
            )
        )


@Client.on_callback_query(filters.regex("reject_call"))
async def about_commands_callbacc(_, CallbackQuery):
    sender_id = CallbackQuery.from_user.id
    if sender_id in SUDO_USERS:
        await CallbackQuery.message.edit_caption(
            reject_string,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="Event", url=f"https://t.me/{SUPPORT_CHAT}/{message.id}")
                    ]
                ]
            )
        )


@Client.on_message(filters.command("revert", prefixes="?") & ~filters.private)
async def revert(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Inspectors can use this.")

    user_name = message.from_user.first_name
    stext = message.text
    if len(stext.split(" ")) < 2:
        await message.reply_text("Atleast give something to revert\nusage: ?revert **id**")
        return
    try:
        splitted = stext.split(None, 1)[1]
        target_id = int(splitted)
    except:
        await message.reply_text(f"wrong format!!\nusage: ?revert **id**")
        return
    
    check = check_gban(target_id)
    if check == False:
        await message.reply_text("this is user is not scanned in our database!")
        return

    revert_save(target_id)
    await ubot.send_message(
        chat_id=SPAM_GROUP,
        text=f"/ungban {target_id}"
    )
    await pbot.send_message(SPAM_GROUP, f"USER [{target_id}](tg://openmessage?user_id={target_id}) UNSCANNED by {user_name}")
    await message.reply_text(f"Revert completed!!\n[User](tg://openmessage?user_id={target_id}) is Now free!!")