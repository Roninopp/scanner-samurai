from samurai import pbot, tbot, SUDO_USERS, GBAN_CHANNEL_ID, SPAM_GROUP, SUPPORT_CHAT
from samurai.utils.idform import createform
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User, InlineKeyboardMarkup, InlineKeyboardButton, Update
import random
from datetime import datetime
import time
from PIL import Image, ImageOps, ImageDraw


from samurai.utils.scan_help import check_gban, gban_save1, gban_save2, gban_save3, revert_save
from samurai.plugins.api_key import scan_api, revert_api
from samurai.utils.bancode_help import bancode_convo
import asyncio

datetime_fmt = "%Y-%m-%d"


#/scan 243475585 spamming my gc for fun KCBX021 https://gdfhgjdfg
def splitting(text):
    text = text.upper()
    remove_cmd = text.split(None, 1)[1]
    target_id = remove_cmd.split(" ")[0]
    remove_id = remove_cmd.split(None, 1)[1]
    dividee = remove_id.partition("KCBX")
    reason = dividee[0]
    divide_reason = remove_id.partition(reason)[2]
    bancode = divide_reason.split(" ")[0]
    proof = divide_reason.split(None, 1)[1]
    proof = proof.lower()
    reason = reason.lower()
    target_id = int(target_id)
    return target_id, reason, bancode, proof