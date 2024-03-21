import re
from typing import Any, Callable, Optional

from pyrogram import filters
from pyrogram.types import Message

from IroXMusic import YouTube, app, Irop
from IroXMusic.core.call import Irop
from IroXMusic.misc import db
from IroXMusic.utils import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS

@app.on_message(
    filters.command(["seek", "cseek", "seekback", "cseekback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def seek_command(cli, message: Message, _: Any, chat_id: int) -> None:
    """
    Handle the seek command for a group chat.

    :param cli: The Pyrogram client.
    :param message: The incoming message object.
    :param _: A placeholder for any extra arguments.
    :param chat_id: The ID of the chat.
    """
    seek_func: Optional[Callable[[int], None]] = None

    if len(message.command) == 1:
        return await message.reply_text(_["admin_20"])

    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text(_["admin_21"])

    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])

    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_22"])

    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]

    is_seek_back = message.command[0][-2] == "c"

    if is_seek_back:
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played - duration_to_skip + 1
    else:
        if (duration_seconds - (duration_played + duration_to_skip)) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played + duration_to_skip + 1

    mystic = await message.reply_text(_["admin_24"])

    try:
        if "vid_" in file_path:
            n, file_path = await YouTube.video(playing[0]["vidid"], True)
            if n == 0:
                return await message.reply_text(_["admin_22"])

        check = playing[0].get("speed_path")
        if check:
            file_path = check

        if "index_" in file_path:
            file_path = playing[0]["vidid"]

        if seek_func is None:
            seek_func = Irop.seek if is_seek_back else Irop.cseek

        await seek_func(chat_id, to_seek)
        await mystic.edit_text(_["admin_25"].format(seconds_to_min(to_seek)))

    except Exception as e:
        await mystic.edit_text(f"Error: {str(e)}")
