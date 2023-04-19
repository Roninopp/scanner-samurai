import logging
import time

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import MemorySession

#===================================
API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"
API_ID = 7217645
BOT_TOKEN = "5137683296:AAHG9wsNL04ij7L5K_47MtLEhbf_4DAD6YU"
SESSION_STRING = "BQB0P2fZ1g-pdvUwHhyICdcG0ljX9pdtjZU6RSCDfH8RJw2jXJFk7JWb7-Zzxh21UtS2xnFYjiJHN3lQwo3alj7sV9qgRt4MK-GpCEFk389dCRasMbEuH_2p_td7aAqpwdfdlR2T6aK2dd2R8ZYbX77w-FJtOQ6aXL3yMPN2ez-Mk5NE_7NrnvFLXWZY7PqPCCDafTTrxjCX8Uu_FqR9PB3i66jrxfbAeRWBXJBlPoLJFh3Yfjp9H86ouRLpXuo4c70WrXKvDvYQusJiV62iSAR44k4_l8hVksrI3G4S6z409HAxQSE-oaIeApY0Gf2VNOuo43xj0mBnuBsIMwkQHw04AAAAAVYVPZwA"

SUPPORT_CHAT = "team_samurai_support"
SUPPORT_ID = -1001553284045 #-1001553284045
GBAN_CHANNEL_ID = -1001709251588 #-1001564289796
SPAM_GROUP = -1001564289796 #-1001564289796
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
