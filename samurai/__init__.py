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
SESSION_STRING = "BQA42On4MNpzTER87ID54MkGSfFI125H-iwY20Uq2dHQCWPLtRbECFW6Dk51ini9b9bA9gOM12KI4AS21vpXSoeDxNdPIMug682yE5N34PsUvAX6W8jgB0d8AxEXJlfcj3VQULF0fauPHfczmfZFJSk7a2e9EGe2H2l6_INe_QI7yDqJLItqF4J3RlBbOXr_Yj0T7YrWCMwPapsd4z2xzaSUdOgohBfiFpg6e6wC9B28f7UpVDJeVJ0NomsU5cL0NtiDrytsr2sGM6x-oe1MCU8rcXluWrBQNO1_CNGu1uYejZFRvMlb14uSWY6kN5YJLDQ9p8F4gOJ025lREcEXLWUPAAAAAVYVPZwA"

SUPPORT_CHAT = "serenity_support"
SUPPORT_ID = -1001553284045 #-1001553284045
GBAN_CHANNEL_ID = -1001709251588 #-1001564289796 -1001907155128
SPAM_GROUP = -1001564289796 #-1001564289796 -1001907155128
FBAN_SPAM = -1001564289796 #-1001833557507


DOWNLOAD_DIRECTORY = "./"

SUDOLIST = set(int(x) for x in os.environ.get("SUDO_USERS", "5362824958 5298587903 1109460378 2005266280 5978107653").split())
SUPPORTLIST = set(int(x) for x in os.environ.get("SUPPORT_USERS", "1257742127 5274479443 5715764478").split())

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
