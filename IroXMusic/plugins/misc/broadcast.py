import asyncio
from pyrogram import filters, Client as PyrogramClient  # Importing necessary modules and classes
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from typing import List

import IroXMusic.misc  # Importing custom modules
import IroXMusic.utils.database
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.formatters import alpha_to_int
from config import adminlist

# Global variable to keep track of broadcasting status
IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & SUDOERS & LOVE)  # Event decorator for the /broadcast command
@language
async def braodcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        query = _parse_query(query)

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent, pin = await _broadcast_to_chats(client, query, x, y)
        await message.reply_text(_["broad_3"].format(sent, pin))

    if "-user" in message.text:
        sent = await _broadcast_to_served_users(client, query)
        await message.reply_text(_["broad_4"].format(sent))

    if "-assistant" in message.text:
        await message.reply_text(_["broad_5"])
        sent = await _broadcast_to_assistants(client, query)


def _parse_query(query: str) -> str:
    # Parsing and cleaning the query string
    query = query.replace("-pin", "").replace("-nobot", "").replace("-pinloud", "")
    query = query.replace("-assistant", "").replace("-user", "")
    if not query:
        raise ValueError("Invalid query")
    return query


async def _broadcast_to_chats(
    client: PyrogramClient, query: str, x: int, y: int
) -> tuple[int, int]:
    sent, pin = 0, 0
    chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
    for i in chats:
        try:
            if not message.reply_to_message:
                m = await app.send_message(i, text=query)
            else:
                m = await app.forward_messages(i, y, x)
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
    client: PyrogramClient, query: str
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
                m = await app.forward_messages(i, y, x)
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except:
            continue
    return sent


async def _broadcast_to_assistants(
    client: PyrogramClient, query: str
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
                await client.send_message(chat_id=_, text=query)
                sent.append(True)
            except:
                sent.append(False)
    return sent
