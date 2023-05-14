from samurai import pbot, OWNER_ID, SUDOLIST, SUPPORT_USERS, SUPPORTLIST, DEV_LIST, DEV_USERS, StartTime, ubot
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from samurai.database import get_gban_list
import time

@ubot.on_message(filters.command("sudolist", prefixes="?"))
async def disaster(_, message: Message):
    if message.from_user.id not in SUPPORT_USERS:
        return await message.reply_text("ONLY FOR APPROVED USERS!!")

    final = "Members of the Team Samurai:\n\nINSPECTOR:\n"
    for enforcer in SUDOLIST:
        try:
            user = await pbot.get_users(enforcer)
            devname = user.first_name
        except:
            devname = "Dragon"

        final += f"✯ [{devname}](tg://openmessage?user_id={enforcer})\n"
    final += "\nENFORCER:\n"
    for inspector in SUPPORTLIST:
        try:
            user = await pbot.get_users(inspector)
            devname = user.first_name
        except:
            devname = "Demon"

        final += f"۞ [{devname}](tg://openmessage?user_id={inspector})\n"
    
    await message.reply_text(final)


@ubot.on_message(filters.command("scanlist", prefixes="?"))
async def scanlist(_, message: Message):
    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Enforcers can use this.")
        
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


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@ubot.on_message(filters.command("stats", prefixes="?"))
async def stats(_, message: Message):
    uptime = get_readable_time((time.time() - StartTime))
    user_id = message.from_user.id

    if user_id not in SUPPORT_USERS:
        return await message.reply_text("Only Enforcers can use this.")

    total = len(get_gban_list())
    enf = ""
    ins = ""
    for enforcer in SUDOLIST:
        try:
            user = await pbot.get_users(enforcer)
            devname = user.first_name
        except:
            devname = "Dragon"
        enf += f"✯ [{devname}](tg://openmessage?user_id={enforcer})\n"
    for inspector in SUPPORTLIST:
        try:
            user = await pbot.get_users(inspector)
            devname = user.first_name
        except:
            devname = "Demon"

        ins += f"۞ [{devname}](tg://openmessage?user_id={inspector})\n"
    text = f"""
[「✪」Bᴏᴛ Sᴛᴀᴛɪsᴛɪᴄs「✪」](https://telegra.ph/file/ab422614c78919a7b8fb1.jpg) :
     
  ✦┈➤ Scanned Users: {total}
  
  ✦┈➤ ALIVE SINCE: `{uptime}`

  
  ✦   [SUPPORT](https://t.me/SpiralSupport)      ✦

   ✦    [NETWORK](https://t.me/TEAMSAMURAII)       ✦

⊂ ✭I𝙽𝚂𝙿𝙴𝙲𝚃𝙾𝚁𝚂
{enf}
⊂ ✭𝙴𝙽𝙵𝙾𝙲𝚁𝙴𝚁𝚂 
{ins}
"""
    await message.reply_photo(
        photo="https://telegra.ph/file/ab422614c78919a7b8fb1.jpg",
        caption=text
    )
