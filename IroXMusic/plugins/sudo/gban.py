import asyncio
from typing import List, Union

import pyrogram
from pyrogram.errors import FloodWait
from pyrogram.types import Message, User

from IroXMusic import app, SUDOERS, LOVE
from IroXMusic.misc import get_readable_time
from IroXMusic.utils import get_served_chats, is_banned_user, add_banned_user, remove_banned_user, get_banned_users, get_banned_count
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.extraction import extract_user

BANNED_USERS = set()

@app.on_message(pyrogram.filters.command(["gban", "globalban"]) & SUDOERS & LOVE)
@language
async def global_ban(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)

    if user.id == message.from_user.id:
        return await message.reply_text(_["gban_1"])
    elif user.id == app.id:
        return await message.reply_text(_["gban_2"])
    elif user.id in SUDOERS:
        return await message.reply_text(_["gban_3"])

    if await is_banned_user(user.id):
        return await message.reply_text(_["gban_4"].format(user.mention))

    if user.id not in BANNED_USERS:
        BANNED_USERS.add(user.id)

    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))

    time_expected = get_readable_time(len(served_chats))

    mystic = await message.reply_text(_["gban_5"].format(user.mention, time_expected))

    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await app.ban_chat_member(chat_id, user.id)
            number_of_chats += 1
            await add_banned_user(user.id)
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except Exception:
            continue

    await message.reply_text(
        _["gban_6"].format(
            app.mention,
            message.chat.title,
            message.chat.id,
            user.mention,
            user.id,
            message.from_user.mention,
            number_of_chats,
        )
    )

    await mystic.delete()
    await message.stop_propagation()

@app.on_message(pyrogram.filters.command(["ungban"]) & SUDOERS & LOVE)
@language
async def global_unban(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])

    user = await extract_user(message)

    if not await is_banned_user(user.id):
        return await message.reply_text(_["gban_7"].format(user.mention))

    BANNED_USERS.remove(user.id)

    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))

    for chat_id in served_chats:
        try:
            await app.unban_chat_member(chat_id, user.id)
            await remove_banned_user(user.id)
        except Exception:
            continue

    await message.reply_text(_["gban_8"].format(user.mention))
