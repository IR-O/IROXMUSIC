import asyncio
from typing import Union

from IroXMusic.misc import db
from IroXMusic.utils.formatters import check_duration, seconds_to_min
from config import autoclean, time_to_seconds

async def get_chat_queue(chat_id):
    """Get the queue for a given chat id."""
    return db.get(chat_id, [])

async def add_to_queue(
    chat_id: int,
    original_chat_id: int,
    file: str,
    title: str,
    duration: str,
    user: str,
    vidid: str,
    user_id: int,
    stream: str,
    forceplay: Union[bool, str] = None,
):
    """Add a song to the queue."""
    title = title.title()
    try:
        duration_in_seconds = time_to_seconds(duration) - 3
    except ValueError:
        duration_in_seconds = 0
        duration = "Invalid duration"

    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "user_id": user_id,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
        "seconds": duration_in_seconds,
        "played": 0,
    }

    if forceplay:
        queue = await get_chat_queue(chat_id)
        queue.insert(0, put)
    else:
        queue = await get_chat_queue(chat_id)
        queue.append(put)

    db[chat_id] = queue
    autoclean.append(file)

async def add_to_queue_index(
    chat_id: int,
    original_chat_id: int,
    file: str,
    title: str,
    duration: str,
    user: str,
    vidid: str,
    stream: str,
    forceplay: Union[bool, str] = None,
):
    """Add a song to the queue with index checking."""
    if "20.212.146.162" in vidid:
        try:
            dur = await check_duration(vidid)
            duration = seconds_to_min(dur)
        except Exception:
            duration = "ᴜʀʟ sᴛʀᴇᴀᴍ"
            dur = 0
    else:
        dur = 0

    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
        "seconds": dur,
        "played": 0,
    }

    if force
