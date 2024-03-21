from pyrogram import filters, StopPropagation # Import necessary filters and exceptions from Pyrogram
from pyrogram.errors import FloodWait

from IroXMusic import app # Import app instance from IroXMusic
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import add_off, add_on # Import add_off and add_on functions from the database module
from IroXMusic.utils.decorators.language import language # Import language decorator

# Function to handle "logger" command in private messages
@app.on_message(filters.private & filters.command(["logger"]) & filters.user(SUDOERS) & LOVE)
@language
async def logger(client, message, _):
    usage = _["log_1"] # Get the usage message for the "logger" command
    if len(message.command) != 2:
        return await message.reply_text(usage) # If the user did not provide the correct number of arguments, reply with the usage message
    state = message.text.split(None, 1)[1].strip().lower() # Get the state (enable/disable) from the user input
    if state not in ("enable", "disable"):
        return await message.reply_text(usage) # If the user provided an invalid state, reply with the usage message
    chat_id = message.chat.id # Get the chat ID
    try:
        if state == "enable":
            await add_on(chat_id) # Enable logging for the chat
            await message.reply_text(_["log_2"]) # Reply with a success message
        elif state == "disable":
            await add_off(chat_id) # Disable logging for the chat
            await message.reply_text(_["log_3"]) # Reply with a success message
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}") # If an error occurred, reply with the error message
        raise StopPropagation # Stop the propagation of the message to prevent other event handlers from processing it


# Function to handle "logger" command in group messages
@app.on_message(filters.group & filters.command(["logger"]) & filters.user(SUDOERS
