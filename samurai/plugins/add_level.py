from pyrogram import filters, Client
from samurai import pbot, ubot, OWNER_ID, SUPPORT_USERS, SUDO_USERS


@Client.on_message(filters.command("addenf", prefixes="?") & ~filters.private)
async def addenf(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in OWNER_ID:
        return await message.reply_text("Only for Owners!")
    
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

    elif len(message.text) == 2:
        target_id = message.text.split(" ")[1]
        try:
            target_id = int(target_id)
        except:
            return await message.reply_text("invalid id!")
    else:
        return await message.reply_text("give me something to promote")
    
    try:
        SUPPORT_USERS.append(target_id)
        await message.reply_text("Successfully promoted the user to Enforcer level!")
    except:
        await message.reply_text("Something went wrong!!")
        
        
@Client.on_message(filters.command("addins", prefixes="?") & ~filters.private)
async def addins(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in OWNER_ID:
        return await message.reply_text("Only for Owners!")
    
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

    elif len(message.text) == 2:
        target_id = message.text.split(" ")[1]
        try:
            target_id = int(target_id)
        except:
            return await message.reply_text("invalid id!")
    else:
        return await message.reply_text("give me something to promote")
    
    try:
        SUDO_USERS.append(target_id)
        await message.reply_text("Successfully promoted the user to Inspector level!")
    except:
        await message.reply_text("Something went wrong!!")
        
        
        
@ubot.on_message(filters.command("addins", prefixes="?") & ~filters.private)
async def ubaddins(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in OWNER_ID:
        return await message.reply_text("Only for Owners!")
    
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

    elif len(message.text) == 2:
        target_id = message.text.split(" ")[1]
        try:
            target_id = int(target_id)
        except:
            return await message.reply_text("invalid id!")
    else:
        return await message.reply_text("give me something to promote")
    
    try:
        SUDO_USERS.append(target_id)
        await message.reply_text("Successfully promoted the user to Inspector level!")
    except:
        await message.reply_text("Something went wrong!!")
        
        
@ubot.on_message(filters.command("addenf", prefixes="?") & ~filters.private)
async def ubaddenf(_: Update, message: Message):

    user_id = message.from_user.id
    if user_id not in OWNER_ID:
        return await message.reply_text("Only for Owners!")
    
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

    elif len(message.text) == 2:
        target_id = message.text.split(" ")[1]
        try:
            target_id = int(target_id)
        except:
            return await message.reply_text("invalid id!")
    else:
        return await message.reply_text("give me something to promote")
    
    try:
        SUPPORT_USERS.append(target_id)
        await message.reply_text("Successfully promoted the user to Enforcer level!")
    except:
        await message.reply_text("Something went wrong!!")
