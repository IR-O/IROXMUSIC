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

        direct = playmode == "Direct" if is_non_admin else None
        group = not is_non_admin if playmode == "Group" else None
        playtype = playty == "Everyone" if group else playty

    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    # Do something with direct, group, and playtype
    # ...
