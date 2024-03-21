import random

from pyrogram import filters
from pyrogram.types import Message

import db  # Database module
from . import app, AdminRightsCheck, close_markup, _  # IroXMusic module and utility functions
from config import BANNED_USERS  # Banned users list

@app.on_message(
    filters.command(["shuffle", "cshuffle"]) &  # Checks for "shuffle" or "cshuffle" command
    filters.group &  # Only process messages in groups
    ~BANNED_USERS  # Exclude banned users
)
@AdminRightsCheck  # Checks for admin privileges
async def admins(Client, message: Message, _, chat_id):
    # Get the current chat's database entry
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])  # If no entry, return a message

    try:
        # Remove the first item from the list
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))  # If an error occurs, return a message

    # Get the updated chat's database entry
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)  # If no entry, insert the removed item back
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))  # Return a message

    # Shuffle the list and insert the removed item at the beginning
    random.shuffle(check)
    check.insert(0, popped)

    # Reply with a success message
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention),  # User mention
        reply_markup=close_markup(_)  # Close the inline button
    )

