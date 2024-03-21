from pyrogram import filters # Import filters from pyrogram

from IroXMusic import YouTube, app # Import YouTube and app from IroXMusic
from IroXMusic.utils.channelplay import get_channeplayCB # Import get_channeplayCB from channelplay.utils
from IroXMusic.utils.decorators.language import languageCB # Import languageCB from decorators.language
from IroXMusic.utils.stream.stream import stream # Import stream from stream.utils
from config import BANNED_USERS # Import BANNED_USERS from config

@app.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS) # Decorator to handle callback queries with regex "LiveStream" and not in BANNED_USERS
@languageCB # Decorator to handle language callbacks
async def play_live_stream(client, CallbackQuery, _): # Function to handle playback of live streams
    callback_data = CallbackQuery.data.strip() # Get the callback data and strip any whitespace
    callback_request = callback_data.split(None, 1)[1] # Split the callback data and get the second part
    vidid, user_id, mode, cplay, fplay = callback_request.split("|") # Split the callback request into variables

    # If the user ID does not match the one in the callback request, answer the callback query with an alert
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(_["playcb_1"], show_alert=True)
        except:
            return

    # Try to get the chat ID and channel from get_channeplayCB
    try:
        chat_id, channel = await get_channeplayCB(_, cplay, CallbackQuery)
    except:
        return

    # Set video to True if mode is 'v', otherwise None
    video = True if mode == "v" else None
    user_name = CallbackQuery.from_user.first_name # Get the user's first name

    # Delete the message and try to answer the callback query
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        pass

    # Reply to the message with a loading text
    mystic = await CallbackQuery.message.reply_text(
        _["play_2"].format(channel) if channel else _["play_1"]
    )

    # Try to get the video details and track ID from YouTube
    try:
        details, track_id = await YouTube.track(vidid, True)
    except:
        return await mystic.edit_text(_["play_3"])

    # Set ffplay to True if fplay is 'f', otherwise None
    ffplay = True if fplay == "f" else None

    # If the video has no duration, try to play the stream
    if not details["duration_min"]:
        try:
            await stream(
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
            )
        except Exception
