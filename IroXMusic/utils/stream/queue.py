import asyncio
from typing import Union

from IroXMusic.misc import db  # Database module
from IroXMusic.utils.formatters import check_duration, seconds_to_min  # Helper functions
from config import autoclean, time_to_seconds  # Configuration settings

async def get_chat_queue(chat_id):
    """Get the queue for a given chat id from the database."""
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
    """Add a song to the queue after processing the input data.

    This function converts the duration to seconds, handles invalid durations,
    and inserts the song into the queue based on the forceplay parameter.
    """
    title = title.title()  # Capitalize the first letter of the title

    try:
        duration_in_seconds = time_to_seconds(duration) - 3  # Convert duration to seconds
    except ValueError:
        duration_in_seconds = 0  # If the duration is invalid, set the duration to 0 seconds
        duration = "Invalid duration"  # Set the duration string to 'Invalid duration'

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
        queue.insert(0, put)  # Insert the song at the beginning of the queue if forceplay is True
    else:
        queue = await get_chat_queue(chat_id)
        queue.append(put)  # Otherwise, append the song to the end of the queue

    db[chat_id] = queue  # Save the updated queue in the database
    autoclean.append(file)  # Add the file to the autoclean list

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
    """Add a song to the queue with index checking after processing the input data."""
    if "20.212.146.162" in vidid:  # If the vidid contains a specific IP address
        try:
            dur = await check_duration(vidid)  # Get the duration using the check_duration function
            duration = seconds_to_min(dur)  # Convert the duration to a human-readable format
        except Exception:
            duration = "ᴜʀʟ sᴛʀᴇᴀᴍ"  # If there's an error, set the duration to 'URL stream'
            dur
