import asyncio
import os
import re
from typing import AsyncContextManager, List, Optional, Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch
from pathlib import Path

import IroXMusic.utils.database as database
from IroXMusic.utils.formatters import time_to_seconds


