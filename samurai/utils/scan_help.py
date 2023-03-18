import json
from samurai.database import scan_db

def check_gban(user_id):
    user_id = str(user_id)
    data = scan_db.find_one({"user_id": user_id})
    if data:
        return True
    else:
        return False


gban_save

revert_save