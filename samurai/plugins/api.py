import requests
import json

api_key = "samuraiapimadebyishikki"

#target_id, target_name, reason, proof, bancode, user_name
def scan_api(uid, name, reason, proof, bancode, enforcer):
    post_dict = {
        "_id": str(uid),
        "name": name,
        "reason": reason,
        "proof": proof,
        "bancode": bancode,
        "enforcer": enforcer,
    }
    headers = {'API-KEY': api_key}
    url = "https://blue-ishikki.vercel.app/scan2"

    response = requests.post(url, headers=headers, json=post_dict)
    return response.text


def revert_api(user_id):
    headers = {'API-KEY': api_key}
    user_id = str(user_id)

    url = f"https://blue-ishikki.vercel.app/revert2/{user_id}"
    response = requests.delete(url, headers=headers)
    return response.text


def token_gen_api(user_id, tokenn, level):
    post_dict = {
        'user_id': str(user_id),
        'token': tokenn,
        'level': level
    }
    headers = {'API-KEY': api_key}
    url = "https://blue-ishikki.vercel.app/approve2"
    response = requests.post(url, headers=headers, json=post_dict)
    return response.tex

def records():
    url = "https://blue-ishikki.vercel.app/records2"
    headers = {'API-KEY': api_key}
    response = requests.get(url, headers=headers)
    SAMURAI_DB = {}
    SAMURAI_DB = json.loads(response.text)
    return SAMURAI_DB