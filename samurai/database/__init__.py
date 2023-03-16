#MONGO
from pymongo import MongoClient

from samurai import LOGGER
from samurai import MONGO_DB


client = MongoClient(MONGO_DB)

db = client["samurai_scanner"]

scan_db = db["scan_db"]
token_db = db["token_db"]
fban_db = db["fban_db"]
misc_db = db["misc_db"]

def get_gban_list():
    return [x for x in scan_db.find()]