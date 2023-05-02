import json
from samurai.database import token_db

def token_save(userid, token_api, level):
    user_id = str(userid)
    token_dict = {
        "user_id": user_id,
        "token": token_api,
        "level": level
    }
    try:
        token_db.insert_one(token_dict)
        lol = "DONE!!"
        retunr lol
    except:
        lol = "lol"
        return lol
        

def check_token(user_id):
    user_id = str(user_id)
    data = token_db.find_one({"user_id": user_id})
    if data:
        token = data["token"]
        level = data["level"]
        return True, level, token
    else:
        lol = "lol"
        return False, lol, lol
