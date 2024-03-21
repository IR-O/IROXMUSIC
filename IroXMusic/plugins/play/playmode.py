from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from typing import Optional

from IroXMusic import app
from IroXMusic.utils.database import get_playmode, get_playtype, is_nonadmin_chat
from IroXMusic.utils.decorators import language
from IroXMusic.utils.inline.settings import playmode_users_markup
from config import BANNED_USERS

@app.on_message(filters.command(["playmode", "mode"]) & filters.group & ~BANNED_USERS)
@language
async def playmode_(client, message: Message, _):
    try:
        is_non_admin = await is_nonadmin_chat(message.chat.id)
    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    try:
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)

        if playmode not in ["Direct", "Group"] or playty not in ["Everyone", "Admin"]:
            raise Exception("Invalid playmode or playtype found in the database.")

        direct = playmode == "Direct" if is_non_admin else None
        group = not is_non_admin if playmode == "Group" else None
        playtype = playty if group else "Admin" if is_non_admin else None

    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    # Do something with direct, group, and playtype
    # ...

    keyboard = playmode_users_markup(direct, group, playtype)
    await message.reply_text(_["playmode_1"], reply_markup=keyboard)
