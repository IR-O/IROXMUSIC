import asyncio
import os
import time
from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Voice

import config
from IroXMusic import app
from IroXMusic.utils.formatters import (
    check_duration,  # Function to check duration of a video/audio file
    convert_bytes,  # Function to convert bytes to a human-readable format
    get_readable_time,  # Function to convert seconds to a readable time format
    seconds_to_min,  # Function to convert seconds to minutes
)

class TeleAPI:
    def __init__(self):
        self.chars_limit = 4096  # Maximum characters allowed in a single message
        self.sleep = 5  # Sleep time in seconds

    async def send_split_text(self, message, string):
        """
        Sends a text message split into multiple parts if it exceeds the character limit.
        :param message: The Pyrogram Message object
        :param string: The text string to be sent
        :return: True upon successful completion
        """
        n = self.chars_limit
        out = [(string[i : i + n]) for i in range(0, len(string), n)]
        for x in out:
            await message.reply_text(x, disable_web_page_preview=True)
        return True

    async def get_link(self, message):
        """
        Returns the message link.
        :param message: The Pyrogram Message object
        :return: The message link as a string
        """
        return message.link

    async def get_filename(self, file, audio: Union[bool, str] = None):
        """
        Returns the file name with the appropriate extension.
        :param file: The Pyrogram File object
        :param audio: Optional parameter to specify if the file is an audio file
        :return: The file name as a string
        """
        try:
            file_name = file.file_name
            if file_name is None:
                file_name = "ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴅɪᴏ" if audio else "ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ"
        except:
            file_name = "ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴅɪᴏ" if audio else "ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ"
        return file_name

    async def get_duration(self, file):
        """
        Returns the duration of the file in minutes.
        :param file: The Pyrogram File object
        :return: The duration as a string
        """
        try:
            dur = seconds_to_min(file.duration)
        except:
            dur = "Unknown"
        return dur

    async def get_duration(self, filex, file_path):
        """
        Returns the duration of the file in minutes.
        :param filex: The Pyrogram File object or Voice object
        :param file_path: The file path as a string
        :return: The duration as a string
        """
        try:
            dur = seconds_to_min(filex.duration)
        except:
            try:
                dur = await asyncio.get_event_loop().run_in_executor(
                    None, check_duration, file_path
                )
                dur = seconds_to_min(dur)
            except:
                return "Unknown"
        return dur

    async def get_filepath(
        self,
        audio: Union[bool, str] = None,
        video: Union[bool, str] = None,
    ):
        """
        Returns the file path with the appropriate file name.
        :param audio: Optional parameter to specify if the file is an audio file
        :param video: Optional parameter to specify if the file is a video file
        :return: The file path as a string
        """
        if audio:
            try:
                file_name = (
                    filex.file_unique_id
                    + "."
                    + (
                        (filex.file_name.split(".")[-1])
                        if (not isinstance(filex, Voice))
                        else "ogg"
                    )
                )
            except:
                file_name = filex.file_unique_id + "." + "ogg"
            file_name = os.path.join(os.path.realpath("downloads"), file_name)
        if video:
            try:
                file_name = (
                    filex.file_unique_id + "." + (filex.file_name.split(".")[-1])
                )
            except:
                file_name = filex.file_unique_id + "." + "mp4"
            file_name = os.path.join(os.path.realpath("downloads"), file_name)
        return file_name

    async def download(self, _, message, mystic, fname):
        """
        Downloads a file and updates the progress.
        :param _: Ignored parameter
        :param message: The Pyrogram Message object
        :param mystic: The Pyrogram Chat object
        :param fname: The file name as a string
        :return: None
        """
        lower = [0, 8, 17, 38, 64, 77, 96]
        higher = [5, 10, 20, 40, 66, 80, 99]
        checker = [5, 10, 20, 40, 66, 80, 99]
        speed_counter = {}
        if os.path.exists(fname):
            return True

        async def progress(current, total):
            if current == total:
                return
            nonlocal speed_counter
            current_time = time.time()
            if current_time - speed_counter.get('time', 0) > 1:
                speed
