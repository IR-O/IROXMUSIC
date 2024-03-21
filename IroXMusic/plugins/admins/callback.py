import asyncio
import typing

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from IroXMusic import YouTube, app, SUDOERS, db, Irop
from IroXMusic.core.call import Irop
from IroXMusic.misc import get_lang, is_active_chat, is_music_playing, is_nonadmin_chat, music_off, music_on, set_loop
from IroXMusic.utils.database import get_active_chats, get_upvote_count, is_active_chat, is_nonadmin_chat, music_off, music_on, set_loop
from IroXMusic.utils.decorators.language import languageCB
from IroXMusic.utils.formatters import seconds_to_min
from IroXMusic.utils.inline import close_markup, stream_markup, stream_markup_timer
from IroXMusic.utils.stream.autoclear import auto_clean
from IroXMusic.utils.thumbnails import get_thumb
from config import BANNED_USERS, adminlist, confirmer, votemode
from strings import get_string

checker: dict[int, dict[int, bool]] = {}
upvoters: dict[int, dict[int, list[int]]] = {}

@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, callback_query: typing.Callable, _: dict) -> None:
    callback_data = callback_query.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    if "_" in str(chat):
        bet = chat.split("_")
        chat = bet[0]
        counter = bet[1]
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await callback_query.answer(_["general_5"], show_alert=True)
    mention = callback_query.from_user.mention
    if command == "UpVote":
        if chat_id not in votemode:
            votemode[chat_id] = {}
        if chat_id not in upvoters:
            upvoters[chat_id] = {}

        voters = (upvoters[chat_id]).get(callback_query.message.id)
        if not voters:
            upvoters[chat_id][callback_query.message.id] = []

        vote = (votemode[chat_id]).get(callback_query.message.id)
        if not vote:
            votemode[chat_id][callback_query.message.id] = 0

        if callback_query.from_user.id in upvoters[chat_id][callback_query.message.id]:
            (upvoters[chat_id][callback_query.message.id]).remove(
                callback_query.from_user.id
            )
            votemode[chat_id][callback_query.message.id] -= 1
        else:
            (upvoters[chat_id][callback_query.message.id]).append(
                callback_query.from_user.id
            )
            votemode[chat_id][callback_query.message.id] += 1
        upvote = await get_upvote_count(chat_id)
        get_upvotes = int(votemode[chat_id][callback_query.message.id])
        if get_upvotes >= upvote:
            votemode[chat_id][callback_query.message.id] = upvote
            try:
                exists = confirmer[chat_id][callback_query.message.id]
                current = db[chat_id][0]
            except:
                return await callback_query.edit_message_text(f"ғᴀɪʟᴇᴅ.")
            try:
                if current["vidid"] != exists["vidid"]:
                    return await callback_query.edit_message.text(_["admin_35"])
                if current["file"] != exists["file"]:
                    return await callback_query.edit_message.text(_["admin_35"])
            except:
                return await callback_query.edit_message_text(_["admin_36"])
            try:
                await callback_query.edit_message_text(_["admin_37"].format(upvote))
            except:
                pass
            command = counter
            mention = "ᴜᴘᴠᴏᴛᴇs"
        else:
            if (
                callback_query.from_user.id
                in upvoters[chat_id][callback_query.message.id]
            ):
                await callback_query.answer(_["admin_38"], show_alert=True)
            else:
                await callback_query.answer(_["admin_39"], show_alert=True)
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text=f"👍 {get_upvotes}",
                            callback_data=f"ADMIN  UpVote|{chat_id}_{counter}",
                        )
                    ]
                ]
            )
            await callback_query.answer(_["admin_40"], show_alert=True)
            return await callback_query.edit_message_reply_markup(reply_markup=upl)
    else:
        is_non_admin = await is_nonadmin_chat(callback_query.message.chat.id)
        if not is_non_admin:
            if callback_query.from_user.id not in
