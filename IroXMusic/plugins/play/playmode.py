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
        playmode = await get_playmode(message.chat.id)
    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    direct: Optional[bool] = None
    if playmode == "Direct":
        direct = True

    try:
        is_non_admin = await is_nonadmin_chat(message.chat.id)
    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    group: Optional[bool] = None
    if not is_non_admin:
        group = True

    try:
        playty = await get_playtype(message.chat.id)
    except Exception as e:
        await message.reply_text(_["error_1"].format(str(e)))
        return

    playtype: Optional[bool] = None
    if playty == "Everyone":
        playtype = None
    else:
        playtype = True

