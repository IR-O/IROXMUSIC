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
