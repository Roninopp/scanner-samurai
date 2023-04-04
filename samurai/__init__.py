import logging
import time

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "5137683296:AAHHib5JAImz2bCEuOD_5PPPXbesf5kSzho"
SESSION_STRING = "BQC_xKVnSfrOVLA_wPgThws8HARDK9UCvPe1Pa6LNoiztwF0DDKTTXu2c0XTr2e3KXZcOgkYg0JhE2wBVceoM-IHOdIqamvqAB8gvMPqAF3E-PzOpr3G3Z-mwuGUyztHidQRZGUSLh8qOz2y6ZU6ZoP6hVF8QmrZvOpXbfgule4MjouoGCf5FiDgFM1ALjYmHdjSeEatoOOJGaft-7CJdhfYvYYstx4qj_3OsLR5nmVhN6xT-SL5j1IiPNFfj6N7CAYMSt0jU85ybpBJijFRfwAAMIERANy5OhdWw9h8iolEPnToUfb8HNaWWmB_sB8cn6XZ5P-wbiEtZERk3YPIuXggAAAAAVYVPZwA"

SUPPORT_CHAT = "spiralsupport"
SUPPORT_ID = -1001842751614 #-1001553284045
GBAN_CHANNEL_ID = -1001842751614 #-1001833557507
SPAM_GROUP = -1001842751614 #-1001833557507
FBAN_SPAM = -1001842751614 #-1001833557507


DOWNLOAD_DIRECTORY = "./"

OWNER_ID = [5030730429, 1793699293]
SUDOLIST = [] #Enforcers
SUPPORTLIST = [] #Inspectors
DEV_LIST = []

DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Inspectors


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
