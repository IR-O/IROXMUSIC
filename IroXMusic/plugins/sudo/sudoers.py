# Importing required modules
from typing import List, Optional

from pyrogram import filters
from pyrogram.errors import UserNotFound
from pyrogram.types import Message, User
from pyrogram.utils import get_size

# Importing custom modules
from IroXMusic import app, LOVE
from IroXMusic.misc import SUDOERS
from IroXMusic.utils.database import add_sudo, remove_sudo
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.extraction import extract_user
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID

@app.on_message(filters.command(["addsudo"]) & filters.user(OWNER_ID | LOVE))
@language
async def useradd(client, message: Message, _):
    # Check if the message has a reply and extract the user
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)

    # Check if the user is already a sudoer
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))

    # Add the user to the sudoers list and update the global SUDOERS list
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"]) & filters.user(OWNER_ID | LOVE))
@language
async def userdel(client, message: Message, _):
    # Check if the message has a reply and extract the user
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)

    # Check if the user is not a sudoer
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))

    # Remove the user from the sudoers list and update the global SUDOERS list
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    text = _["sudo_5"]

    # Add the bot owner to the list
    user = await app.get_me()
    user = user.first_name if not user.mention else user.mention
    text += f"1➤ {user}\n"

    # Initialize counters
    count = 0
    smex = 0

    # Iterate through the global SUDOERS list and add each sudoer to the list
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += _["sudo_6"] + "\n"
                text += f"{count + 1}➤ {user}\n"
                count += 1
            except UserNotFound:
                continue

    if not count:
        text += _["sudo_7"]

    await message.reply_text(text)
