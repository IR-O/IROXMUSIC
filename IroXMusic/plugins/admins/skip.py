import asyncio
import os
from typing import List, Tuple

import pyrogram
from pyrogram.errors import QueryIdInvalid
from pyrogram.filters import Command, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BANNED_USERS
from IroXMusic.core.call import Irop
from IroXMusic.core.database import db
from IroXMusic.decorators.admin_check import AdminRightsCheck
from IroXMusic.functions.auto_clean import auto_clean
from IroXMusic.functions.close_keyboard import close_markup
from IroXMusic.functions.get_loop import get_loop
from IroXMusic.functions.get_thumb import get_thumb
from IroXMusic.functions.string_ as s

# Define the skip function
@app.on_message(Command(["skip", "cskip", "next", "cnext"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def skip(cli, message: Message, _):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) < 2:
        queue = db.get(chat_id)
        if not queue:
            return await message.reply_text(_["queue_2"])
        popped = queue.pop(0)
        if popped:
            await auto_clean(popped)
        if not queue:
            try:
              
