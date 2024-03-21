from typing import Any

from pyrogram import filters
from pyrogram.types import Message

from IroXMusic import YouTube, app, Irop
from IroXMusic.core.call import Irop
from IroXMusic.misc import db
from IroXMusic.utils import AdminRightsCheck, seconds_to_min
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS

@app.on_message(                                       # Listens for incoming messages
    filters.command(["seek", "cseek", "seekback", "cseekback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck                                       # Checks if the user has admin rights
async def seek_command(cli, message: Message, _: Any, chat_id: int) -> None:
    """
    Handles the seek command for a group chat.
    This function is called when the user sends a message with the 'seek', 'cseek', 'seekback', or 'cseekback' command
    in a group chat, and the user has admin rights.
    """
    if len(message.command) == 1:                       # Checks if the user provided a value for the seek command
        return await message.reply_text(_["admin_20"])   # If not, sends an error message

    query = message.text.split(None, 1)[1].strip()      # Gets the value provided for the seek command
    if not query.isnumeric():                           # Checks if the value is a number
        return await message.reply_text(_["admin_21"])   # If not, sends an error message

    playing = db.get(chat_id)                          # Gets the current playing song for the chat
    if not playing:                                     # If there's no playing song, sends an error message
        return await message.reply_text(_["queue_2"])

    duration_seconds = int(playing[0]["seconds"])       # Gets the duration of the current playing song
    if duration_seconds == 0:                           # If the duration is 0, sends an error message
        return await message.reply_text(_["admin_22"])

    file_path = playing[0]["file"]                     # Gets the file path of the current playing song
    duration_played = int(playing[0]["played"])         # Gets the duration played of the current playing song
    duration_to_skip = int(query)                       # Gets the value provided for the seek command as the duration to skip
    duration = playing[0]["dur"]                       # Gets the duration of the current playing song

    is_seek_back = message.command[0][-2] == "c"         # Checks if the seek command is a seek back command

    if is_seek_back:                                    # If the seek command is a seek back command
        if (duration_played - duration_to_skip) <= 10:  # Checks if the duration played minus the duration to skip is less than or equal to 10
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )                                           # If so, sends an error message
        to_seek = duration_played - duration_to_skip + 1 # Calculates the new duration played
    else:                                               # If the seek command is not a seek back command
        if (duration_seconds - (duration_played + duration_to_skip)) <= 10:  # Checks if the duration of the song minus the duration played plus the duration to skip is less than or equal to 10
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )                                           # If so, sends an error message
        to_seek = duration_played + duration_to_skip + 1 # Calculates the new duration played

    mystic = await message.reply_text(_["admin_24"])     # Sends a loading message

    try:                                                # Tries to seek the song
        if "vid_" in file_path:                          # If the file path contains 'vid_', it's a YouTube video
            n, file_path = await YouTube.video(playing[0]["vidid"], True)
            if n == 0:                                   # If the video cannot be found, sends an error message
                return await message.reply_text(_["admin_22"])

        check = (playing[0]).get("speed_path")          # Checks if the current playing song has a speed path
        if check:                                       # If so, uses the speed path as the file path
            file_path = check

        if "index_" in file_path:                       # If the file path contains 'index_', it's a cached file
            file_path = playing[0]["vidid"]             #
