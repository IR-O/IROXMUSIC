import asyncio
import os
import re
from typing import AsyncContextManager, List, Optional, Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch  # A module for YouTube search
from pathlib import Path  # A library to handle file paths

import IroXMusic.utils.database as database  # A module for database-related operations
from IroXMusic.utils.formatters import time_to_seconds  # A function to convert time to seconds

# This is an asynchronous context manager, which is used to manage resources in an asynchronous context.
AsyncContextManager

# List, Optional, and Union are types from the typing module, which provides optional static typing for Python.
List, Optional, Union

# yt_dlp is a fork of youtube-dl with additional features and fixes.
import yt_dlp

# Pyrogram's MessageEntityType is an enumeration of the different types of message entities.
MessageEntityType

# Pyrogram's Message is a class representing a message in a chat.
Message

# VideosSearch is a class from youtubesearchpython that provides a simple way to search for YouTube videos.
VideosSearch

# Path is a class from pathlib that provides an object-oriented interface to filesystem paths.
Path

# The database module contains functions for interacting with the application's database.
IroXMusic.utils.database

# The formatters module contains a function for converting time formats to seconds.
IroXMusic.utils.formatters
