from pyrogram import filters  # Importing filters from pyrogram library
from pyrogram.errors import UserNotEmpty, UserIsBot  # Importing error classes from pyrogram library
from pyrogram.types import Message, User  # Importing Message and User classes from pyrogram library
from typing import Optional  # Importing Optional type from typing library

from IroXMusic import app  # Importing app instance from IroXMusic package
from IroXMusic.core.call import Irop  # Importing Irop class from IroXMusic.core.call module
from IroXMusic.utils.database import is_music_playing, music_off  # Importing is_music_playing and music_off functions from IroXMusic.utils.database module
from IroXMusic.utils.decorators import AdminRightsCheck  # Importing AdminRightsCheck decorator from IroXMusic.utils.decorators module
from IroXMusic.utils.inline import close_markup  # Importing close_markup function from IroXMusic.utils.inline module
from config import BANNED_USERS  # Importing BANNED_USERS from config module
from language import _  # Importing translation function from language module

@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)  # Decorator to listen for /pause or /cpause command in group chats excluding banned users
@AdminRightsCheck  # Decorator to check for admin rights
async def pause_admin(cli, message: Message, _, chat_id: int):  # Function to pause the music
    if not await is_music_playing(chat_id):  # Check if music is already playing
        if not await message.chat.get_members(message.from_user.id):  # Check if the user is a member of the chat
            return await message.reply_text(_["not_admin"])  # Reply with not_admin message if the user is not a member
        return await message.reply_text(_["admin_1"])  # Rep
