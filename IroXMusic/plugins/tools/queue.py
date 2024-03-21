import asyncio
import os
import pathlib
import snmp
import functools

import pyrogram
from pyrogram import Client, filters, raw
from pyrogram.errors import FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from snmp import TimeTicks

from IroXMusic import app
from IroXMusic.misc import db
from IroXMusic.utils import IropBin, get_cmode, get_duration, get_image, get_seconds, get_seconds_to_min, is_active_chat, is_music_playing
from IroXMusic.utils.database import get_cmode, is_active_chat, is_music_playing
from IroXMusic.utils.decorators.language import language, languageCB
from IroXMusic.utils.inline import queue_back_markup, queue_markup
from config import BANNED_USERS, config

# Initialize an empty dictionary to store video IDs
basic = {}

# A decorator to cache the result of get_channeplayCB function
@functools.lru_cache()
def get_channeplayCB(client, what, message):
    # Resolve the chat ID and channel
    try:
        chat_id = client.resolve_peer(message.chat.id)["chat_id"]
    except:
        chat_id = None
    if not chat_id:
        return None, None
    try:
        channel = client.resolve_peer(what)
    except:
        return None, None
    return chat_id, channel


# A callback function to handle the /queue, /cqueue, /player, /cplayer, /playing, /cplaying commands
@app.on_message(
    filters.command(["queue", "cqueue", "player", "cplayer", "playing", "cplaying"])
    & filters.group(True)
    & ~BANNED_USERS
)
@language
async def get_queue(client, message: Message, _):
    # Check if the command is for a channel
    if message.command[0][0] == "c":
        chat_id, channel = await get_channeplayCB(_, message.command[0][1], message)
        if chat_id is None:
            return await message.reply_text(_["setting_7"])
        try:
            # Check if the chat exists
            await client.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
        cplay = True
    else:
        chat_id = message.chat.id
        cplay = False
    # Check if the chat is active
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_5"])
    # Get the chat data from the database
    got = db.get(chat_id)
    if not got:
        return await message.reply_text(_["queue_2"])
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    # Get the duration of the video
    DUR = get_duration(got)
    # Get the path of the video thumbnail
    image_path = get_image(videoid)
    # Set the default thumbnail URL
    image_url = image_path if os.path.isfile(image_path) else config.YOUTUBE_IMG_URL
    # Set the caption of the message
    send = _["queue_6"] if DUR == "Unknown" else _["queue_7"]
    cap = _["queue_8"].format(app.mention, title, typo, user, send)
    # Create the inline keyboard markup
    upl = queue_markup(_, DUR, "c" if cplay else "g", videoid) if DUR == "Unknown" else queue_markup(
        _,
        DUR,
        "c" if cplay else "g",
        videoid,
        get_seconds_to_min(got[0]["played"]),
        got[0]["dur"],
    )
    # Add the video ID to the dictionary
    basic[videoid] = True
    # Send the message with the caption and inline keyboard markup
    mystic = await message.reply_photo(
        photo=image_url,
        caption=cap,
        reply_markup=upl,
    )
    # If the duration is not "Unknown"
    if DUR != "Unknown":
        # Wait until the video changes
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                # If the chat is active and the music is playing
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                        # If the music is playing
                        if await is_music_playing(chat_id):
                            # Edit the message with the new inline keyboard markup
                            try:
                                buttons = queue_markup(
                                    _,
                                    DUR,
                                    "c" if cplay else "g",
                                    videoid,
                                    get_seconds_to_min(db[chat_id][0]["played"]),
                                    db[chat_id][0]["dur"],
                                )
                                await asyncio.gather(
                                    mystic.edit_reply_markup(reply_markup=buttons),
                                    asyncio.sleep(5),
                                )
                            except FloodWait as e:
                                await asyncio.sleep(e.x)
                        else:
                            pass
                    else:
                        break
                else:
                    break
        except:
            return


# A callback function to handle the GetTimer callback query
@app.on_callback_query(filters
