from pyrogram import filters, StopPropagation
from pyrogram.errors import FloodWait

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import add_off, add_on
from IroXMusic.utils.decorators.language import language

@app.on_message(filters.private & filters.command(["logger"]) & filters.user(SUDOERS) & LOVE)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state not in ("enable", "disable"):
        return await message.reply_text(usage)
    chat_id = message.chat.id
    try:
        if state == "enable":
            await add_on(chat_id)
            await message.reply_text(_["log_2"])
        elif state == "disable":
            await add_off(chat_id)
            await message.reply_text(_["log_3"])
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        raise StopPropagation

@app.on_message(filters.group & filters.command(["logger"]) & filters.user(SUDOERS) & LOVE)
@language
async def logger_group(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state not in ("enable", "disable"):
        return await message.reply_text(usage)
    chat_id = message.chat.id
    try:
        if state == "enable":
            await add_on(chat_id)
            await message.reply_text(_["log_2"])
        elif state == "disable":
            await add_off(chat_
