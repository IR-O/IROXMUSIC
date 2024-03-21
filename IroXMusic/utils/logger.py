from pyrogram.enums import ParseMode  # Importing ParseMode enum from pyrogram library
from pyrogram.errors import ChatAdminRequired, UserIsBlocked  # Importing required exceptions

from IroXMusic import app, LOGGER_ID, USERNAME  # Importing app, LOGGER_ID, and USERNAME from the IroXMusic module
from IroXMusic.utils.database import is_on_off  # Importing is_on_off function from the database utilities
from IroXMusic.utils.decorators import errors  # Importing errors decorator

@errors  # Decorating the function with errors decorator
async def play_logs(message, streamtype):  # Defining the asynchronous function play_logs with message and streamtype as parameters
    if not await is_on_off(2):  # If the value returned by is_on_off(2) is False
        return  # Exit the function

    try:
        logger_text = f"""  # Initializing the logger_text variable with the following formatted string
            <b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>  # Bold text for 'IroXMusic Play Log'

            <b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>  # Bold text for 'Chat ID' followed by the chat ID in code format
            <b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}  # Bold text for 'Chat Name' followed by the chat title
            <b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}  # Bold text for 'Chat Username' followed by the chat username

            <b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>  # Bold text for 'User ID' followed by the user ID in code format
            <b>ɴᴀᴍᴇ :
