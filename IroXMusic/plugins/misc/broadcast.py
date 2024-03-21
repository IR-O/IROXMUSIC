import asyncio
import re
from typing import List, Tuple

import pyrogram
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from IroXMusic.misc import SUDOERS, LOVE, app, get_served_chats, get_served_users
from IroXMusic.utils.database import get_client
from IroXMusic.utils.formatters import alpha_to_int
from IroXMusic.utils.decorators.language import language

IS_BROADCASTING = False
ADMIN_IDS = [int(admin) for admin in adminlist.split()]


@app.on_message(SUDOERS & LOVE & pyrogram.filters.command("broadcast"))
@language
async def broadcast_message(client, message: Message, _):
    global IS_BROADCASTING
    if len(message.command) < 2:
        return await message.reply_text(_["broad_2"])

    query = message.text.split(None, 1)[1]
    query = re.sub(r"(-pin|-nobot|-pinloud|-assistant|-user)", "", query)
    if not query:
        return await message.reply_text(_["broad_2"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent, pin = await _broadcast_to_chats(client, query, message)
        await message.reply_text(_["broad_3"].format(sent, pin))

    if "-user" in message.text:
        sent = await _broadcast_to_served_users(client, query, message)
        await message.reply_text(_["broad_4"].format(sent))

    if "-assistant" in message.text:
        sent = await _broadcast_to_assistants(client, query)
        await message.reply_text(_["broad_5"])

    IS_BROADCASTING = False


async def _broadcast_to_chats(
    client, query: str, message: Message
) -> Tuple[int, int]:
    sent, pin = 0, 0
    chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
    for i in chats:
        try:
            if not message.reply_to_message:
                m = await app.send_message(i, text=query)
            else:
                m = await app.forward_messages(i, message.reply_to_message.chat.id, message.reply_to_message.id)
            if "-pin" in message.text:
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except:
                    continue
            elif "-pinloud" in message.text:
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except:
                    continue
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except:
            continue
    return sent, pin


async def _broadcast_to_served_users(
    client, query: str, message: Message
) -> int:
    sent = 0
    served_users = [int(user["user_id"]) for user in await get_served_users()]
    for i in served_users:
        try:
            if i not in await get_served_chats():
                continue
            if not message.reply_to_message:
                m = await app.send_message(i, text=query)
            else:
                m = await app.forward_messages(i, message.reply_to_message.chat.id, message.reply_to_message.id)
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except:
            continue
    return sent


async def _broadcast_to_assistants(
    client, query: str
) -> List[bool]:
    sent = []
    from IroXMusic.core.userbot import assistants

    for num in assistants:
        try:
            client = await get_client(num)
        except:
            continue
        async for _ in client.get_dialogs():
            try:
                await client.send_message(chat_id=_.chat.id, text=query)
                sent.append(True)
            except:
                sent.append(False)
    return sent
