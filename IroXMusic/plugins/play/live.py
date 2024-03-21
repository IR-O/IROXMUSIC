from pyrogram import filters, StopPropagation
from typing import Optional

from IroXMusic import YouTube, app, _
from IroXMusic.utils.channelplay import get_channeplayCB
from IroXMusic.utils.decorators.language import languageCB
from IroXMusic.utils.stream.stream import stream
from config import BANNED_USERS

@app.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS)
@languageCB
async def play_live_stream(client, CallbackQuery, _: dict) -> None:
    """Play live stream from YouTube."""
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    vidid, user_id, mode, cplay, fplay = callback_request.split("|")

    if CallbackQuery.from_user.id != int(user_id):
        await CallbackQuery.answer(_["playcb_1"], show_alert=True)
        raise StopPropagation

    try:
        chat_id, channel = await get_channeplayCB(_, cplay, CallbackQuery)
    except Exception:
        return

    video = True if mode == "v" else None
    user_name = CallbackQuery.from_user.first_name

    try:
        await CallbackQuery.message.delete()
        await CallbackQuery.answer()
    except Exception:
        pass

    mystic = await CallbackQuery.message.reply_text(
        _["play_2"].format(channel) if channel else _["play_1"]
    )

    try:
        details, track_id = await YouTube.track(vidid, True)
    except Exception:
        return await mystic.edit_text(_["play_3"])

    ffplay = True if fplay == "f" else None

    try:
        async with stream(
            _,
            mystic,
            user_id,
            details,
            chat_id,
            user_name,
            CallbackQuery.message.chat.id,
            video,
            streamtype="live",
            forceplay=ffplay,
        ) as stream_task:
            await stream_task
    except Exception as e:
        await mystic.edit_text(str(e))
