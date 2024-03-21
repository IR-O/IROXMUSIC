from typing import List, AsyncIterator

from pyrogram import filters, Message
from pyrogram.types import Chat
from pyrogram.errors import ChatNotFound

from unidecode import unidecode

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice", "activev", "activevideo"]) & SUDOERS & LOVE)
async def active_chats(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    chat_type = message.command[1]
    served_chats: List[str] = []
    if chat_type == "vc" or chat_type == "voice":
        served_chats = await get_active_chats()
    elif chat_type == "v" or chat_type == "video":
        served_chats = await get_active_video_chats()
    else:
        return await mystic.edit_text(f"» ɪɴᴠᴀʟɪᴅ ᴄʜᴀᴛ ᴛʏᴘᴇ {chat_type}.")

    if not served_chats:
        return await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ {chat_type.upper()} ᴄʜᴀᴛs ᴏɴ {app.mention}.")

    text = f"» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ {chat_type.upper()} ᴄʜᴀᴛs :\n\n"
    async for x in served_chats:
        try:
            chat: Chat = await app.get_chat(x)
            if chat.type.value != "private":
                title = chat.title
            else:
                title = "Private Chat"
        except ChatNotFound:
            await remove_active_chat(x) if chat_type == "vc" or chat_type == "voice" else remove_active_video_chat(x
