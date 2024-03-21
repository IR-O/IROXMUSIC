from pyrogram import filters
from pyrogram.types import Message
from typing import Any

from IroXMusic import app
from IroXMusic.core.call import Irop
from IroXMusic.utils.database import is_music_playing, music_on
from IroXMusic.utils.decorators import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS
from translations import _

@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _: Any, chat_id: int):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    
    try:
        await music_on(chat_id)
        await Irop.resume_stream(chat_id)
        await message.reply_text(
            _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
        )
    except Exception as e:
        await message.reply_text(f"Error: {e}")
