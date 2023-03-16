import logging
import time

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = ""
API_ID = 5
BOT_TOKEN = ""
SESSION_STRING = ""

SUPPORT_CHAT = ""
SUPPORT_ID = -100
GBAN_CHANNEL_ID = -100
SPAM_GROUP = -100
FBAN_SPAM = -100


DOWNLOAD_DIRECTORY = "./"

OWNER_ID = [5030730429]
SUDOLIST = [] #Enforcers
SUPPORTLIST = [] #Inspectors
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Inspectors


REQUEST_IMG = ""

MONGO_DB = ""
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
LOGGER.info("SAMURAI Scanner is starting...")
LOGGER.info("Handled by: IShIkkI AKABANE")


pbot = Client("samurai", API_ID, API_HASH, bot_token=BOT_TOKEN)
ubot = Client("Client", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)


pbot.start()
ubot.start()

bot = pbot.get_me()
BOT_ID = bot.id
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
BOT_USERNAME = bot.username


tbot = TelegramClient(MemorySession(), API_ID, API_HASH)