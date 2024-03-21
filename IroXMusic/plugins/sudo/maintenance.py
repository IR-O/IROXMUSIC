from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired

import asyncio

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on,
)
from strings import get_string

# This decorator defines a new asynchronous function that listens for
# incoming messages containing the "maintenance" command, is created
# by a SUDOERS user, and contains the LOVE flag.
@app.on_message(filters.command(["maintenance"]) & SUDOERS & LOVE)
async def maintenance(client, message: Message):
    try:
        # Get the language for the chat
        language = await get_lang(message.chat.id)
        # Get the corresponding strings for the language
        _ = get_string(language)
    except:
        # If the language cannot be determined, use English
        _ = get_string("en")
        # Reply with an error message
        await message.reply_text(_["error_chat_language"])
        return

    # Display usage information if the command is used incorrectly
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)

    # Get the state from the command arguments
    state = message.text.split(None, 1)[1].strip().lower()
    if state not in ["enable", "disable"]:
        await message.reply_text(usage)
        return

    # Enable maintenance mode
    if state == "enable":
        # Check if maintenance mode is already enabled
        if await is_maintenance():
            await message.reply_text(_["maint_4"])
        else:
            # Attempt to enable maintenance mode
            try:
                await maintenance_on()
                # Reply with a success message
                await message.reply_text(_["maint_2"].format(app.mention))
            except ChatAdminRequired:
                # If the bot is not an admin in the chat, reply with an error message
                await message.reply_text(_["error_admin_required"])

    # Disable maintenance mode
    elif state == "disable":
        #
