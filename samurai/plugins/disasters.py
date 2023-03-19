from samurai import pbot, OWNER_ID, SUDOLIST, SUPPORT_USERS, SUPPORTLIST, DEV_LIST, DEV_USERS
from pyrogram import Client, enums, filters
from pyrogram.types import Message


@Client.on_message(filters.command("sudolist", prefixes="?"))
async def disaster(_, message: Message):
    if message.from_user.id not in SUPPORT_USERS:
        return await message.reply_text("ONLY FOR APPROVED USERS!!")

    final = "Members of the Team Samurai:\n\nENFORCERS:\n"
    for dev in DEV_LIST:
        try:
            user = pbot.get_users(dev)
            devname = user.first_name
        except:
            devname = "Dev"

        final += f"✯ [{devname}](tg://openmessage?user_id={dev})\n"
    for enforcer in SUDOLIST:
        try:
            user = pbot.get_users(enforcer)
            devname = user.first_name
        except:
            devname = "Dragon"

        final += f"✯ [{devname}](tg://openmessage?user_id={enforcer})\n"
    final += "\nINSPECTORS:\n"
    for inspector in SUPPORTLIST:
        try:
            user = pbot.get_users(inspector)
            devname = user.first_name
        except:
            devname = "Demon"

        final += f"۞ [{devname}](tg://openmessage?user_id={inspector})\n"
    
    await message.reply_text(final)


@Client.on_message(filters.command("scanlist", prefixes="?"))
async def scanlist(_, message: Message):
    banned_users = get_gban_list()
    
    if not banned_users:
        await message.reply_text(
            "NOBODY IS SCANNED",
        )
        return

    banfile = "Screw you guys...\n[x] USER ID  |BANCODE | NAME - ENFORCER\n"
    count = 0
    for user in banned_users:
        banfile += f"[{count + 1}] {user['user_id']} - "
        banfile += f"{user['bancode']} - "
        banfile += f"{user['name']} - "
        banfile += f"{user['enforcer']}\n"

    with BytesIO(str.encode(banfile)) as output:
        output.name = "gbanlist.txt"
        await message.reply_document(
            document=output,
            file_name="gbanlist.txt",
            caption="Here is the list of people who are scanned",
        )