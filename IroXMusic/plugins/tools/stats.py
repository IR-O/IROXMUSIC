import os
import platform
from sys import version as pyver
from typing import Any

import psutil
from pytgcalls import __version__ as pytgver
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from urllib.parse import urlparse

from IroXMusic import app
from IroXMusic.core.userbot import assistants
from IroXMusic.misc import SUDOERS, mongodb
from IroXMusic.plugins import ALL_MODULES
from IroXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from IroXMusic.utils.decorators.language import language, languageCB
from IroXMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS, config

STATS_IMG_URL_valid = urlparse(config.STATS_IMG_URL).scheme in ("http", "https")

@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    if STATS_IMG_URL_valid:
        await message.reply_photo(
            photo=config.STATS_IMG_URL,
            caption=_["gstats_2"].format(app.mention),
            reply_markup=upl,
        )
    else:
        await message.reply_text(
            text=_["gstats_2"].format(app.mention),
            reply_markup=upl,
        )

@app.on_callback_query(filters.regex("stats_back") & ~BANNED_USERS)
@languageCB
async def home_stats(client, callback_query: CallbackQuery, _):
    upl = stats_buttons(_, True if callback_query.from_user.id in SUDOERS else False)
    await callback_query.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )

@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, callback_query: CallbackQuery, _):
    await callback_query.answer()
    upl = back_stats_buttons(_)
    try:
        await callback_query.answer()
    except:
        pass
    await callback_query.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await callback_query.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await callback_query.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )

@app.on_callback_query(filters.regex("bot_stats_sudo") & filters.user(SUDOERS) & ~BANNED_USERS)
@languageCB
async def sudo_stats(client, callback_query: CallbackQuery, _):
    await callback_query.answer()
    upl = stats_buttons(_, True)
    await callback_query.edit_message_text(_["gstats_4"].format(app.mention))
    text = _["gstats_5"].format(
        app.mention,
        pyver,
        platform.system(),
        platform.release(),
        psutil.cpu_count(),
    )
    await callback_query.edit_message_text(text)

