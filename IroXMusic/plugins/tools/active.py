from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from IroXMusic import app
from IroXMusic.misc import SUDOERS, LOVE
from IroXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS & LOVE)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    if not served_chats:
        return await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")

    text = "» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :\n\n"
    for j, x in enumerate(served_chats, start=1):
        try:
            chat = await app.get_chat(x)
            title = chat.title
        except:
            await remove_active_chat(x)
            continue
        try:
            if chat.username:
                user = chat.username
                text += f"<b>{j}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += f"<b>{j}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
        except:
            continue

    await mystic.edit_text(text, disable_web_page_preview=True)


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS & LOVE)
async def activevi(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_video_chats()
    if not served_chats:
        return await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")

    text = "» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :\n\n"
    for j, x in enumerate(served_chats, start=1):
        try:
            chat = await app.get_chat(x)
            title = chat.title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if chat.username:
                user = chat.username
                text += f"<b>{j}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += f"<b>{j}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
        except:
            continue

    await mystic.edit_text(text, disable_web_page_preview=True)
