from pyrogram import filters  # Importing filters from pyrogram library
from pyrogram.types import Message  # Importing Message from pyrogram.types

import IroXMusic  # Importing the IroXMusic module
from IroXMusic.core.call import Irop  # Importing Irop from IroXMusic.core.call
from IroXMusic.utils.database import set_loop  # Importing set_loop from IroXMusic.utils.database
from IroXMusic.utils.decorators import AdminRightsCheck  # Importing AdminRightsCheck from IroXMusic.utils.decorators
from IroXMusic.utils.inline import close_markup  # Importing close_markup from IroXMusic.utils.inline
from config import BANNED_USERS  # Importing BANNED_USERS from config

# @app.on_message(filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS)
@app.on_message(filters.command(commands=["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):  # The function to stop the music
    """
    This function is used to stop the music in the group chat.
    :param cli: The pyrogram client
    :param message: The incoming message object
    :param _: The extra arguments
    :param chat_id: The ID of the chat
    """
    if not len(message.command) == 1:  # Checking if the user has provided any arguments
        return  # If yes, then return and do nothing

    # Calling the stop_stream method from Irop class and passing chat_id as an argument
    await Irop.stop_stream(chat_id)

    # Calling the set_loop method from database.py and passing 0 as an argument
    await set_loop(chat_id, 0)

