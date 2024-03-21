import asyncio
from typing import Any, Callable, Coroutine, Optional

import aiohttp
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import YouTube from "IroXMusic.YouTube"
import app from "IroXMusic.app"
import get_string from "IroXMusic.strings"
import get_lang from "IroXMusic.misc.lang"
import get_cmode from "IroXMusic.misc.cmode"
import get_playmode from "IroXMusic.misc.playmode"
import get_playtype from "IroXMusic.misc.playtype"
import is_active_chat from "IroXMusic.misc.is_active_chat"
import is_maintenance from "IroXMusic.misc.is_maintenance"
import botplaylist_markup from "IroXMusic.utils.inline.botplaylist_markup"
import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist from "config"

links = {}

async def PlayWrapper(command: Callable[[Message, str, int, bool, Optional[str]], Coroutine[Any, Any, Any]]) -> Callable[[Message], Coroutine[Any, Any, Any]]:
    async def wrapper(client: YouTube, message: Message) -> Coroutine[Any, Any, None]:
        language = await get_lang(message.chat.id)
        _ = get_string(language)

        if message.chat.type not in ("group", "supergroup"):
            return await message.reply_text(_["general_2"])

        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="AnonymousAdmin")]]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )

        try:
            await message.delete()
        except:
            pass

        audio_telegram = message.reply_to_message.audio if message.reply_to_message else None
        video_telegram = message.reply_to_message.video if message.reply_to_message else None
        url = await YouTube.url(message)

        if not (audio_telegram or video_telegram or url):
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["play_18"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )

        chat_id = await get_cmode(message.chat.id) if message.command[0][0] == "c" else message.chat.id
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        channel = await get_channel(chat_id)

        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_13"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])

        video = True if message.command[0][0] == "v" else None
        if "-v" in message.text:
            video = True
        fplay = True if message.command[0][-1] == "e" else None

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)
            try:
                get = await app.get_chat_member(chat_id, userbot.id)
                if (
                    get.status == ChatMemberStatus.BANNED
