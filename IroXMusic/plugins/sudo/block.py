from pyrogram import filters, StopPropagation
from pyrogram.types import Message, User

from IroXMusic import app
from IroXMusic.misc import SUDOERS
from IroXMusic.utils.database import add_gban_user, remove_gban_user
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.extraction import extract_user

BANNED_USERS = set()

@app.on_message(filters.command(["block"]) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if message.from_user.id in BANNED_USERS:
        return await message.reply_text(_["block_1"].format(message.from_user.mention))
    
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id == message.from_user.id:
        return await message.reply_text(_["block_8"])
    if user.id in BANNED_USERS:
        return await message.reply_text(_["block_1"].format(user.mention))
    await add_gban_user(user.id)
    BANNED_USERS.add(user.id)
    await message.reply_text(_["block_2"].format(user.mention))


@app.on_message(filters.command(["unblock"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in BANNED_USERS:
        return await message.reply_text(_["block_3"].format(user.mention))
    try:
        await app.unban_chat_member(message.chat.id, user.id)
    except:
        return await message.reply_text(_["block_9"])
    await remove_gban_user(user.id)
    BANNED_USERS.remove(user.id)
    await message.reply_text(_["block_4"].format(user.mention))

@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            if not user:
                continue
            user = user.first_name if not user.mention else user.mention
            count += 1
            await mystic.edit_text(msg.format(count, user))
        except:
            continue
