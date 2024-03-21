from pyrogram import filters
from pyrogram.types import Message
from typing import List, Union

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import blacklist_chat, blacklisted_chats, is_blacklisted_chat, whitelist_chat
from IroXMusic.utils.decorators.language import language


@app.on_message(filters.command(["blchat", "blacklistchat"]) & SUDOERS & LOVE)
@language
async def blacklist_chat_func(client, message: Message, _):
    if len(message.command) != 2:
        return await message.reply_text(_["black_1"])
    chat_id = int(message.text.strip().split()[1])
    if chat_id in await blacklisted_chats():
        return await message.reply_text(_["black_2"])
    if await is_blacklisted_chat(chat_id):
        return await message.reply_text(_["black_2"])
    if await app.can_delete_messages(chat_id):
        blacklisted = await blacklist_chat(chat_id)
        if blacklisted:
            await message.reply_text(_["black_3"])
        else:
            await message.reply_text(_["black_9"])
        try:
            await app.leave_chat(chat_id)
        except:
            pass
    else:
        await message.reply_text(_["black_10"])


@app.on_message(
    filters.command(["whitelistchat", "unblacklistchat", "unblchat"]) & SUDOERS, LOVE
)
@language
async def white_funciton(client, message: Message, _):
    if len(message.command) != 2:
        return await message.reply_text(_["black_4"])
    chat_id = int(message.text.strip().split()[1])
    if chat_id not in await blacklisted_chats():
        return await message.reply_text(_["black_5"])
    if not await is_blacklisted_chat(chat_id):
        return await message.reply_text(_["black_5"])
    whitelisted = await whitelist_chat(chat_id)
    if whitelisted:
        await message.reply_text(_["black_6"])
    else:
        await message.reply_text(_["black_9"])


@app.on_message(filters.command(["blchats", "blacklistedchats"]) & ~SUDOERS)
@language
async def all_chats(client, message: Message, _):
    text = _["black_7"]
    j = 0
    blacklisted_chats_ = await blacklisted_chats()
    for count, chat_id in enumerate(blacklisted_chats_, 1):
        try:
            chat =
