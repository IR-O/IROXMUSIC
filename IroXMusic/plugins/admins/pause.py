from pyrogram import filters
from pyrogram.errors import UserNotEmpty, UserIsBot
from pyrogram.types import Message, User
from typing import Optional

from IroXMusic import app
from IroXMusic.core.call import Irop
from IroXMusic.utils.database import is_music_playing, music_off
from IroXMusic.utils.decorators import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS
from language import _

@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id: int):
    if not await is_music_playing(chat_id):
        if not await message.chat.get_members(message.from_user.id):
            return await message.reply_text(_["not_admin"])
        return await message.reply_text(_["admin_1"])
    try:
        await music_off(chat_id)
        await Irop.pause_stream(chat_id)
        await message.reply_text(
            _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
        )
    except UserNotEmpty:
        await message.reply_text(_["admin_3"])
    except UserIsBot:
        await message.reply_text(_["admin_4"])
