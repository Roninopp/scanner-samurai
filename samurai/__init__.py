import logging
import time
import os

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "7307409890:AAFPJfxlPd2wua6kx0rFN6Sx7Bx9Z9t0Vyk"
SESSION_STRING = "BQAnNdBwhhW9_NR-SatuMCaV6n_b04VypSkMavGpMpN1b9kBqJ_Zp2_JuOuv6h6bj0FxqMY91OVlXn0uPS_MaNHT-JdGTloSJdIBmM6slAtgVV9Lp5kwAq0Hhtw4EKBvOh-0baquCz8DR54ZGbcPkhKzHWUrAoUgjrr6xym66sQ-yWMcHZa7kF7nWUXUD10CtSvZ5Ov1wXPqOJvKK2EsV1nVxXBc1aF3BmFIAQIYuYFWeryMgsx0fMp1UXn_e6kvtby_WOVQSmyrpMuZ1KrVna8W2CSOAf4QqmBlv4G-Gd27zOGdbh3lKVNjeXiQe0XXW0OKXsjnK9lDM_rc18ziFzRKAAAAAaWSgN0A"
SUPPORT_CHAT = "logs_sh"
SUPPORT_ID = -4252223920 #-1002189185102
GBAN_CHANNEL_ID = -1002147765430 #-1002189185102 -1002189185102
SPAM_GROUP = -1002147765430 #-1002210296980 -1002210296980
FBAN_SPAM = -1002147765430 #-1002210296980


DOWNLOAD_DIRECTORY = "./"

SUDOLIST = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
SUPPORTLIST = set(int(x) for x in os.environ.get("SUPPORT_USERS", "2095867247 1737646273").split())

OWNER_ID = [5030730429, 6837532865]
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = list(SUDOLIST) + DEV_USERS #Inspectors
SUPPORT_USERS = list(SUPPORTLIST) + SUDO_USERS #Enforcer


REQUEST_IMG = "https://telegra.ph/file/9ed4c2423cb907046f254.jpg"

MONGO_DB = "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority"
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
