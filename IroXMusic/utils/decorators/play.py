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

from IroXMusic import YouTube, app
from IroXMusic.misc import SUDOERS
from IroXMusic.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from IroXMusic.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

links = {}

def PlayWrapper(command: Callable[[Message, str, int, bool, Optional[str]], Coroutine[Any, Any, Any]]) -> Callable[[Message], Coroutine[Any, Any, Any]]:
# This function takes a command as an argument and returns another function that takes a Message as an argument.
# The returned function is a coroutine that wraps the execution of the provided command with some additional functionality.

    async def wrapper(client: YouTube, message: Message) -> Coroutine[Any, Any, None]:
# This is the wrapper function that is returned by PlayWrapper. It takes a YouTube client and a Message as arguments,
# and returns a coroutine that performs the following tasks:

        language = await get_lang(message.chat.id)
        _ = get_string(language)
# Get the language for the current chat and load the string resources for that language.

        if message.chat.type not in ("group", "supergroup"):
            return await message.reply_text(_["general_2"])
# If the message was not sent in a group or supergroup, reply with a message indicating that the command can only be used in such chats.

        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʜᴏᴡ ᴛᴏ ғɪx ?", callback_data="AnonymousAdmin")]]
            )
            return await message.reply_text(_["general_3"], reply_markup=upl)
# If the message was sent by an anonymous administrator, provide a way for them to learn how to fix that and reply with a message.

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )
# If the bot is not in maintenance mode, but the user is not a sudoer, reply with a message indicating that the bot is under maintenance and providing a link to the support chat.

        try:
            await message.delete()
        except:
            pass
# Try to delete the message that triggered the command, but ignore any errors that may occur.

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
# If the message did not contain a Telegram media message or a YouTube URL, and the command was not "stream",
# reply with a photo of the playlist and a set of inline buttons.

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
# If the playtype is not "Everyone", and the user is not a sudoer, check if they are an administrator of the chat.
# If they are not, reply with a message indicating that they do not have the necessary permissions.

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
                    or get.status == ChatMemberStatus.
