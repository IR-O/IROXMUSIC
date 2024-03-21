from datetime import datetime
from typing import Union

from pyrogram import filters
from pyrogram.errors import Photo size is too large
from pyrogram.types import Message

from IroXMusic import app
from IroXMusic.core.call import Irop
from IroXMusic.utils import bot_sys_stats
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.inline import supp_markup
from config import BANNED_USERS
from config import PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    if not message.text:
        return
    try:
        start = datetime.now()
        response = await message.reply_photo(
            photo=PING_IMG_URL,
            caption=_["ping_1"].format(app.mention),
        )
    except Photo size is too large:
        return await message.reply_text(_["ping_photo_error"])
    try:
        pytgping = await Irop.ping()
    except Exception as e:
        return await message.reply_text(_["ping_error"].format(str(e)))
    try:
        UP, CPU, RAM, DISK = await bot_sys_stats()
    except Exception
