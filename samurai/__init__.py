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
SESSION_STRING = "BQBo8J-25RjInz4xG-4UJEBIsskcmysSyPTCmtYmQ68L0QL2mgshZMhMwUw5qV2wVtzmDceBybo8ug39qxqBq1Lxx21pH_TDkLj1La5OY2Y3OnNgSdBUCrcjQmumt12AJ77b42LYoocSo3C2RHUjz6EzpdLkFjfoUdr4KNlVXDhfEEsmCfX4bo71zBwBF0nmnmVsMUYtunqVPbJa5XNEJ8kixljFSND-ThJFnGqk8TrGWhkRm8it_raoqY09O7DrZd9idv87yZPsO2BcfYbal1djqu2A2PXZb_2rKiFMM-Pa2nYC25Ch6GIV4-LSJP-BZq05-N4wHm1MMEy9jFaqj7LaAAAAAWOMJpYA"

SUPPORT_CHAT = "samurai_botsupport"
SUPPORT_ID = -1001553284045 #-1001553284045
GBAN_CHANNEL_ID = -1001966188512 #-1001564289796 -1001907155128
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
