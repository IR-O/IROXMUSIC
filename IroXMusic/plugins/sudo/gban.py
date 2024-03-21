import asyncio  # This module is used for running async tasks.
from typing import List, Union  # These are used for type hinting.

from pyrogram import filters, StopPropagation  # Pyrogram libraries for filters and stopping propagation.
from pyrogram.errors import FloodWait  # Pyrogram library for handling flood wait errors.
from pyrogram.types import Message, User  # Pyrogram libraries for Message and User objects.

from IroXMusic import app, SUDOERS, LOVE  # IroXMusic app instance, sudoers list, and love string.
from IroXMusic.misc import get_readable_time  # Function to convert seconds to a human-readable format.
from IroXMusic.utils import get_served_chats, is_banned_user, add_banned_user, remove_banned_user, get_banned_users, get_banned_count  # Various utility functions.
from IroXMusic.utils.decorators.language import language  # Language translation decorator.
from IroXMusic.utils.extraction import extract_user  # Function to extract user object from a message.

# Set to store globally banned users.
BANNED_USERS = set()

@app.on_message(filters.command(["gban", "globalban"]) & SUDOERS & LOVE)
@language  # Language translation decorator.
async def global_ban(client, message: Message, _):
    # Check if the message has a reply. If not, and the message doesn't have the correct number of arguments, reply with an error message.
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    # Extract the user object from the reply or the message arguments.
    user = await extract_user(message)
    # Check if the user to be banned is the message sender, the bot itself, or a sudoer. If so, reply with an error message.
    if user.id == message.from_user.id:
        return await message.reply_text(_["gban_1"])
    elif user.id == app.id:
        return await message.reply_text(_["gban_2"])
    elif user.id in SUDOERS:
        return await message.reply_text(_["gban_3"])
    # Check if the user is already globally banned. If so, reply with an error message.
    if await is_banned_user(user.id):
        return await message.reply_text(_["gban_4"].format(user.mention))
    # Add the user to the globally banned users set.
    if user.id not in BANNED_USERS:
        BANNED_USERS.add(user.id)
    # Get the list of served chats.
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    # Calculate the time expected to ban the user from all served chats.
    time_expected = get_readable_time(len(served_chats))
    # Reply with a message indicating the ban process has started.
    mystic = await message.reply_text(_["gban_5"].format(user.mention, time_expected))
    # Iterate through the served chats.
    number_of_chats = 0
    for chat_id in served_chats:
        # Try to ban the user from the chat.
        try:
            await app.ban_chat_member(chat_id, user.id)
            number_of_chats += 1
            # If successful, add the user to the banned users list.
            await add_banned_user(user.id)
        # If a FloodWait error occurs, sleep for the specified time.
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        # If any other error occurs, continue to the next chat.
        except Exception:
            continue
    # Reply with a message indicating the ban was successful.
    await message.reply_text(
        _["gban_6"].format(
            app.mention,
            message.chat.title,
            message.chat.id,
            user.mention,
            user.id,
            message.from_user.mention,
            number_of_chats,
        )
    )
    # Delete the initial message.
    await mystic.delete()
    # Stop the propagation of the message.
    await message.stop_propagation()


@app.on_message(filters.command(["ungban"]) & SUDOERS & LOVE)
@language  # Language translation decorator.
async def global_un(client, message: Message, _):
    # Check if the message has a reply. If not, and the message doesn't have the correct number of arguments, reply with an error message.
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    # Extract the user object from the reply or the message arguments.
    user = await extract_user(message)
    # Check if the user is not globally banned. If so, reply with an error message.
    if not await is_banned_user(user.id):
        return await message.reply_text(_["gban_7"].format(user.mention))
    # Remove the user from the globally banned users set.
    if user.id in BANNED_USERS:
        BANNED_USERS.remove(user.id)
    # Get the list of served chats.
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    # Calculate the time expected to unban the user from all served chats.
    time_expected = get_readable_time(len(served_chats))
    # Reply with
