import os  # Importing the os module to interact with the operating system
import random  # Importing the random module to generate random values
import string  # Importing the string module for string manipulation
import time  # Importing the time module to work with time
from typing import Any  # Importing Any from typing module
from typing import Dict  # Importing Dict from typing module
from typing import List  # Importing List from typing module
from typing import Union  # Importing Union from typing module

import aiohttp  # Asynchronous HTTP client/server for Python
import aiohttp.client_exceptions  # Exceptions for aiohttp
import aiohttp.web  # Web framework for aiohttp
import requests  # Python HTTP Library
from bs4 import BeautifulSoup  # HTML/XML Parser for Python
from pyrogram import filters  # Filters for Pyrogram
from pyrogram.errors import FloodWait  # FloodWait exception for Pyrogram
from pyrogram.errors import MessageNotModified  # MessageNotModified exception for Pyrogram
from pyrogram.errors import RPCError  # RPCError exception for Pyrogram
from pyrogram.types import InlineKeyboardButton  # Inline keyboard button for Pyrogram
from pyrogram.types import InlineKeyboardMarkup  # Inline keyboard markup for Pyrogram
from pyrogram.types import InputMediaPhoto  # Input media photo for Pyrogram
from pyrogram.types import Message  # Message object for Pyrogram
from pytgcalls.exceptions import NoActiveGroupCall  # NoActiveGroupCall exception for pytgcalls

import config  # Importing config.py module for configuration settings
from IroXMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app  # Importing various modules for IroXMusic
from IroXMusic.core.call import Irop  # Importing Irop class from call.py
from IroXMusic.utils import seconds_to_min  # Function to convert seconds to minutes
from IroXMusic.utils import time_to_seconds  # Function to convert time to seconds
from IroXMusic.utils.channelplay import get_channeplayCB  # Function to get channel play callback
from IroXMusic.utils.decorators.language import languageCB  # Language change decorator
