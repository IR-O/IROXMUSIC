from pyrogram import filters
from pyrogram.types import Message
from typing import Any

import IroXMusic
from IroXMusic.core.call import Irop
from IroXMusic.utils.database import is_music_playing, music_on
from IroXMusic.utils.decorators import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS
from translations import _

@IroXMusic.app.on_message(  # Decorator to listen for incoming messages
    filters.command(["resume", "cresume"])  # Command filter: "resume" or "cresume"
    & filters.group  # Only listen in groups
    & ~BANNED_USERS  # Exclude banned users
)
@AdminRightsCheck  # Decorator to check for admin rights
async def resume_com(cli, message: Message, _: Any, chat_id: int):  # Define the function with required parameters
    if not await is_music_playing(chat_id):  # Check if music is playing in the chat
        return await message.reply_text(_["admin_3"])  # If not, return a message and exit
    
    try:
        await music_on(chat_id)  # Turn on the music
        await Irop.resume_stream(chat_id)  # Resume the stream
        await message.reply_text(
            _["admin_4"].format(message.from_user.mention),  # Reply with a success message
            reply_markup=close_markup(_)  # Add a close button to the reply
        )
    except Exception as e:  # Catch any exceptions
        await message.reply_text(f"Error: {e}")  # Reply with the error message
