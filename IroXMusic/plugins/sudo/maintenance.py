from pyrogram import filters, StopPropagation
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired

import asyncio

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import (
    get_lang,
    is_maintenance,
    maintenance_off,
    maintenance_on,
)
from strings import get_string

@app.on_message(filters.command(["maintenance"]) & SUDOERS & LOVE)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
        await message.reply_text(_["error_chat_language"])
        return

    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)

    state = message.text.split(None, 1)[1].strip().lower()
    if state not in ["enable", "disable"]:
        await message.reply_text(usage)
        return

    if state == "enable":
        if await is_maintenance():
            await message.reply_text(_["maint_4"])
        else:
            try:
                await maintenance_on()
                await message.reply_text(_["maint_2"].format(app.mention))
            except ChatAdminRequired:
                await message.reply_text(_["error_admin_required"])
                raise StopPropagation

    elif state == "disable":
        if not await is_maintenance():
            await message.reply_text(_["maint_3"])
        else:
            try:
                await maintenance_off()
                await message.reply_text(_["maint_5"].format(app.mention))
            except ChatAdminRequired:
                await message.reply_text(_["error_admin_required"])
                raise StopPropagation
