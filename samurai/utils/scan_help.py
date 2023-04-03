import json
from samurai.database import scan_db

def check_gban(user_id):
    user_id = str(user_id)
    data = scan_db.find_one({"user_id": user_id})
    if data:
        return True
    else:
        return False


def gban_save(user_id, target_name, reason, proof, bancode, enforcer):
    scan_dict = {
        "user_id": str(user_id),
        "name": target_name,
        "reason": reason,
        "proof": proof,
        "bancode": bancode,
        "enforcer": enforcer
    }
    scan_db.insert_one(scan_dict)


def revert_save(user_id):
    user_id = str(user_id)
    scan_db.delete_one({"user_id": user_id})


def gban_data(user_id):
    data = scan_db.find_one({"user_id": str(user_id)})
    if data:
        reason = data["reason"]
        proof = data["proof"]
        bancode = data["bancode"]
        enforcer = data["enforcer"]
        return True, reason, proof, bancode, enforcer
    else:
        a = "lol"
        return False, a, a, a, a