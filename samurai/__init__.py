import logging
import time
import os

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "6205032906:AAEzeNQaGwFKLvUQ3r9l7sB7mkh31RHgpU8"
SESSION_STRING = "BQCRejBwh3bOIugsqXDfKojKj10BHkN0O_lXb312pcVs5ojBFsLuNw42Dz3N0PHItvnJfb-FcA9DpLFNUgvyjDcFkH0hOAmi2ZR-M4oB47NpR7qoRPmnyRX1hSKs_4kCvPjvMfJpCIbDwqupo9-Pdld5XcnjWQih2Vr7F4UVYyHQq3leJaZB8aqEoxiJj-19DQOYF7bT7523bWlXZi1ySdzNy36iar_Ero4FkSmD1kg_cWu_Rs1FgNmAETYlgKoizZ5yminh_bx-JovXOiGinwIbKTOzTFLl4uZgb8QWULXzqiBk6XTdwoqsxctATrmPZmXGE4rRqSW1W0GQHulbk34kAAAAAVYVPZwA"

SUPPORT_CHAT = "serenity_support"
SUPPORT_ID = -1001553284045 #-1001553284045
GBAN_CHANNEL_ID = -1001709251588 #-1001564289796 -1001907155128
SPAM_GROUP = -1001564289796 #-1001564289796 -1001907155128
FBAN_SPAM = -1001564289796 #-1001833557507


DOWNLOAD_DIRECTORY = "./"

SUDOLIST = set(int(x) for x in os.environ.get("SUDO_USERS", "5362824958 5163444566 1435293433 5476036315 2005266280 1109460378 5298587903").split())
SUPPORTLIST = set(int(x) for x in os.environ.get("SUPPORT_USERS", "5715764478 5764124248 5849705782 5348193047").split())

OWNER_ID = [5030730429, 1793699293]
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = list(SUDOLIST) + DEV_USERS #Inspectors
SUPPORT_USERS = list(SUPPORTLIST) + SUDO_USERS #Enforcer


REQUEST_IMG = "https://telegra.ph/file/9ed4c2423cb907046f254.jpg"

MONGO_DB = "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#===================================

StartTime = time.time()

# enable logging
FORMAT = "[SAMURAI] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[SAMURAI]')
LOGGER.info("SAMURAI Scanner is Booting...")
LOGGER.info("created by: IShIkkI AKABANE")


pbot = Client("samurai", API_ID, API_HASH, bot_token=BOT_TOKEN)
ubot = Client("Client", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)


pbot.start()
ubot.start()


tbot = TelegramClient(MemorySession(), API_ID, API_HASH)
