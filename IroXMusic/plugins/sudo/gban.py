import asyncio
from typing import List, Union

import pyrogram
from pyrogram.errors import FloodWait
from pyrogram.types import Message, User

from IroXMusic import app, SUDOERS, LOVE
from IroXMusic.misc import get_readable_time
from IroXMusic.utils import get_served_chats, is_banned_user, add_banned_user, remove_banned_user, get_banned_users, get_banned_count
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.extraction import extract_user

# Set to store globally banned user IDs
BANNED_USERS = set()

# Command handler for global banning a user
@app.on_message(pyrogram.filters.command(["gban", "globalban"]) & SUDOERS & LOVE)
@language
async def global_ban(client, message: Message, _):
    # Check if the message is a reply to another message and if the command has the correct number of arguments
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    # Extract the user to ban from the reply message
    user = await extract_user(message)

    # Check if the user to ban is the message sender, the bot itself, or a sudo user
    if user.id == message.from_user.id:
        return await message.reply_text(_["gban_1"])
    elif user.id == app.id:
        return await message.reply_text(_["gban_2"])
    elif user.id in SUDOERS:
        return await message.reply_text(_["gban_3"])

    # Check if the user is already globally banned
    if await is_banned_user(user.id):
        return await message.reply_text(_["gban_4"].format(user.mention))

    # Add the user's ID to the set of globally banned users
    if user.id not in BANNED_USERS:
        BANNED_USERS.add(user.id)

    # Get the list of chats served by the bot
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))

    # Calculate the time expected to ban the user from all chats
    time_expected = get_readable_time(len(served_chats))

    # Reply to the message with a message indicating the ban process has started
    mystic = await message.reply_text(_["gban_5"].format(user.mention, time_expected))

    # Iterate through the list of served chats and ban the user from each one
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            # Ban the user from the chat
            await app.ban_chat_member(chat_id, user.id)
            number_of_chats += 1
            # Add the user's ID to the list of banned users for the chat
            await add_banned_user(user.id)
        except FloodWait as fw:
            # If the bot is being rate-limited, sleep for the specified amount of time
            await asyncio.sleep(int(fw.value))
        except Exception:
            # If any other error occurs, continue to the next chat
            continue

    # Reply to the message with a message indicating the ban was successful
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

    # Delete the reply to the original message
    await mystic.delete()
    # Stop the propagation of the message to prevent infinite loops
    await message.stop_propagation()

# Command handler for un-globally banning a user
@app.on_message(pyrogram.filters.command(["ungban"]) & SUDOERS & LOVE)
@language
async def global_un(client, message: Message, _):
    # Check if the message is a reply to another message and if the command has the correct number of arguments
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    # Extract the user to unban from the reply message
    user = await extract_user(message)

    # Check if the user is already unbanned
    if not await is_banned_user(user.id):
        return await message.reply_text(_["gban_7"].format(user.mention))

    # Remove the user's ID from the set of globally banned users
    BANNED_USERS.remove(user.id)

    # Get the list of chats served by the bot
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))

    # Calculate the time expected to unban the user from all chats
    time_expected = get_
