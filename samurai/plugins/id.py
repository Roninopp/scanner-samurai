from samurai import pbot
from pyrogram import Client, enums, filters
from pyrogram.types import Message, Chat, User

@Client.on_message(filters.command("id", prefixes="?"))
async def user_id(_, message: Message):
    if message.reply_to_message:
        replied_user_id = message.reply_to_message.from_user.id
        await message.reply_text(f"The replied user ID is: `{replied_user_id}`")
        return

    if message.forward_from:
        forwarded_user_id = message.forward_from.id
        await message.reply_text(f"The forwarded user ID is: `{forwarded_user_id}`")
        return

    if len(message.text.split(" ")) < 2:
        user_id = message.from_user.id
        chat_id = message.chat.id
        await message.reply_text(f"Your user ID is: `{user_id}`\nThis chat ID is: `{chat_id}`")
        return

    username = message.text.split(None, 1)[1]
    try:
        users = pbot.get_users(username)
        user_id = users[0].id
        await message.reply_text(f"User id of {username} is: `{user_id}`")
        return

    except:
        await message.reply_text("Not found!!!\nforward me some message of him")