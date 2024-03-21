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
from IroXMusic.utils import IropBin, get_cmode, get_duration, get_image, get_seconds, seconds_to_min, is_active_chat, is_music_playing
from IroXMusic.utils.database import get_cmode, is_active_chat, is_music_playing
from IroXMusic.utils.decorators.language import language, languageCB
from IroXMusic.utils.inline import queue_back_markup, queue_markup
from config import BANNED_USERS, config

basic = {}


@functools.lru_cache()
def get_channeplayCB(client, what, message):
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


@app.on_message(
    filters.command(["queue", "cqueue", "player", "cplayer", "playing", "cplaying"])
    & filters.group(True)
    & ~BANNED_USERS
)
@language
async def get_queue(client, message: Message, _):
    if message.command[0][0] == "c":
        chat_id, channel = await get_channeplayCB(_, message.command[0][1], message)
        if chat_id is None:
            return await message.reply_text(_["setting_7"])
        try:
            await client.get_chat(chat_id)
        except:
            return await message.reply_text(_["cplay_4"])
        cplay = True
    else:
        chat_id = message.chat.id
        cplay = False
    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_5"])
    got = db.get(chat_id)
    if not got:
        return await message.reply_text(_["queue_2"])
    file = got[0]["file"]
    videoid = got[0]["vidid"]
    user = got[0]["by"]
    title = (got[0]["title"]).title()
    typo = (got[0]["streamtype"]).title()
    DUR = get_duration(got)
    image_path = get_image(videoid)
    image_url = image_path if os.path.isfile(image_path) else config.YOUTUBE_IMG_URL
    send = _["queue_6"] if DUR == "Unknown" else _["queue_7"]
    cap = _["queue_8"].format(app.mention, title, typo, user, send)
    upl = queue_markup(_, DUR, "c" if cplay else "g", videoid) if DUR == "Unknown" else queue_markup(
        _,
        DUR,
        "c" if cplay else "g",
        videoid,
        seconds_to_min(got[0]["played"]),
        got[0]["dur"],
    )
    basic[videoid] = True
    mystic = await message.reply_photo(
        photo=image_url,
        caption=cap,
        reply_markup=upl,
    )
    if DUR != "Unknown":
        try:
            while db[chat_id][0]["vidid"] == videoid:
                await asyncio.sleep(5)
                if await is_active_chat(chat_id):
                    if basic[videoid]:
                        if await is_music_playing(chat_id):
                            try:
                                buttons = queue_markup(
                                    _,
                                    DUR,
                                    "c" if cplay else "g",
                                    videoid,
                                    seconds_to_min(db[chat_id][0]["played"]),
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


@app.on_callback_query(filters.regex("GetTimer") & ~BANNED_USERS)
async def quite_timer(client, CallbackQuery: CallbackQuery):
    with contextlib.suppress(Exception):
        await CallbackQuery.answer()


@app.on_callback_query(filters.regex("GetQueued") & ~BANNED_US
