import logging
import time

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "5607703434:AAHk7FVVBxEzIVwDffm4VgGEW39cUqhD5Rw"
SESSION_STRING = "1BVtsOGYBu1eiW3ENPWp8cYG1LLObsb7WrRy9F1Vb1k8XaeDLXkNXk0f6QPMZKaxivxFd74VroeyKia-tu4yrKSK5CeV8blvsTVmI3tx_TDbdpzlwBfLeqpHYWNsuonxPOFuT8eE0Bp1pLmlEaRub7C5LMFIArp0oK8jRgePnCR2k5PAwtz_S69mVu1Bte7SqRc4SFDnPpBzidj0uZC0ng5Cxchqvk3YMs-bD-C7yex3NU15iHPPKOEFSJaZYCubD7F8mfoXX9yMSkqap6L19mjYmRbYnFDombHaRgZWLB-CzCR-hDvKCWdein5m8UoWV9L993wLPtXNqkbrd6BT0amXtDSG17GQ="

SUPPORT_CHAT = "spiralsupport"
SUPPORT_ID = -1001842751614 #-1001553284045
GBAN_CHANNEL_ID = -1001842751614 #-1001833557507
SPAM_GROUP = -1001842751614 #-1001833557507
FBAN_SPAM = -1001842751614 #-1001833557507


DOWNLOAD_DIRECTORY = "./"

OWNER_ID = [5030730429, 1793699293]
SUDOLIST = [] #Inspectors
SUPPORTLIST = [] #Enforcer
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Inspectors
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Enforcer


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
