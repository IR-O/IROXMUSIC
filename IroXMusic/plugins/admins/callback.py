import asyncio
import typing
from functools import lru_cache

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# IroXMusic related imports
from IroXMusic import YouTube, app, SUDOERS, db, Irop
from IroXMusic.core.call import Irop
from IroXMusic.misc import get_lang, is_active_chat, is_music_playing, is_nonadmin_chat, music_off, music_on, set_loop
from IroXMusic.utils.database import get_active_chats, get_upvote_count, is_active_chat, is_nonadmin_chat, music_off, music_on, set_loop
from IroXMusic.utils.decorators.language import languageCB
from IroXMusic.utils.formatters import seconds_to_min
from IroXMusic.utils.inline import close_markup, stream_markup, stream_markup_timer
from IroXMusic.utils.stream.autoclear import auto_clean
from IroXMusic.utils.thumbnails import get_thumb
from config import BANNED_USERS, adminlist, confirmer, votemode
from strings import get_string

# Global variables
@lru_cache()
def get_chat_settings(chat_id):
    return db[chat_id]

