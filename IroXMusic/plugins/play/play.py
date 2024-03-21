import os
import random
import string
import time
from typing import Any
from typing import Dict
from typing import List
from typing import Union

import aiohttp
import aiohttp.client_exceptions
import aiohttp.web
import requests
from bs4 import BeautifulSoup
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.errors import MessageNotModified
from pyrogram.errors import RPCError
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputMediaPhoto
from pyrogram.types import Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from IroXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from IroXMusic.core.call import Irop
from IroXMusic.utils import seconds_to_min
from IroXMusic.utils import time_to_seconds
from IroXMusic.utils.channelplay import get_channeplayCB
from IroXMusic.utils.decorators.language import languageCB
from IroXMusic.utils.decorators.play import PlayWrapper
from IroXMusic.utils.formatters import formats
from IroXMusic.utils.inline import (
    botplaylist_markup,
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from IroXMusic.utils.logger import play_logs
from IroXMusic.utils.stream.stream import stream
from config import BANNED_USERS
from config import lyrical

