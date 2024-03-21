import asyncio
from typing import AsyncContextManager, List, Optional, Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from pathlib import Path

from IroXMusic.utils.database import (
    add_new_user,
    get_user,
    get_user_from_event,
    is_active_chat,
    is_premium,
)
from IroXMusic.utils.formatters import time_to_seconds

# Move the import statement for logging to the top of the file
import logging

# Initialize logger
logger = logging.getLogger(__name__)

async def download_audio(...):
    ...

async def search_song(query: str) -> Optional[str]:
    ...

async def get_file_name(...):
    ...

async def download_and_save(...):
    ...

async def process_download(message: Message, query: str):
    ...

async def song_download_function(message: Message):
    ...
