from pyrogram import filters # Importing filters module from pyrogram library
from pyrogram.types import Message # Importing Message class from pyrogram.types module

from IroXMusic import app # Importing app instance from IroXMusic module
from IroXMusic.misc import SUDOERS, LOVE # Importing SUDOERS and LOVE from IroXMusic.misc module
from IroXMusic.utils.database import autoend_on, autoend_off # Importing autoend_on and autoend_off functions from IroXMusic.utils.database module

@app.on_message(filters.command("autoend") & SUDOERS & LOVE) # Decorator to listen for /autoend command from sudoers and LOVE users
async def auto_end_stream(_, message: Message): # Defining the asynchronous function auto_end_stream
    USAGE = "ᴇxᴀᴍᴘʟᴇ :\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]" # Defining the usage message
    # Checking if the length of the command is not equal to 2
    if len(message.command) != 2:
        return await message.reply_text(USAGE) # Replying to the user with the usage message
    state = message.text.split(None, 1)[1].strip().lower() # Extracting the state (enable or disable) from the user input
    # Checking if the state is equal to "enable"
    if state == "enable":
        await autoend_on() # Calling the autoend_on function
        await message.reply_text(
            "» ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ.\n\nᴀssɪsᴛᴀɴᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀғ
