import asyncio
import os
from typing import Dict, Union

import pyrogram
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    TelegramServerError,
)
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded

# Initialize empty dictionaries
# We use dictionaries to store asynchronous events and counters for each chat.
autoend: Dict[int, asyncio.Event] = {}
counter: Dict[int, int] = {}

import config  # Import configuration settings
from IroXMusic import LOGGER, YouTube, app  # Import necessary modules
from IroXMusic.misc import db  # Import database-related functions
from IroXMusic.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_lang,
    get_loop,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from IroXMusic.utils.exceptions import AssistantErr
from IroXMusic.utils.formatters import check_duration, seconds_to_min, speed_converter
from IroXMusic.utils.inline.play import stream_markup
from IroXMusic.utils.stream.autoclear import auto_clean
from IroXMusic.utils.thumbnails import get_thumb
from strings import get_string

# Commented out debugging line
# LOGGER.info("This is some debugging info.")
