import os
from random import randint
from typing import Union

import pyrogram
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from IroXMusic import Carbon, YouTube, app
from IroXMusic.core.call import Irop
from IroXMusic.misc import db
from IroXMusic.utils.database import add_active_video_chat, is_active_chat
from IroXMusic.utils.exceptions import AssistantErr
from IroXMusic.utils.inline import aq_markup, close_markup, stream_markup
from IroXMusic.utils.pastebin import IropBin
from IroXMusic.utils.stream.queue import put_queue, put_queue_index
from IroXMusic.utils.thumbnails import get_thumb

class StreamHandler:
    @staticmethod
    async def stream(
        *,
        mystic: pyrogram.types.Message,
        user_id: int,
        result,
        chat_id: int,
        user_name: str,
        original_chat_id: int,
        video: Union[bool, str] = None,
        streamtype: Union[bool, str] = None,
        spotify: Union[bool, str] = None,
        forceplay: Union[bool, str] = None,
    ) -> Message:
        """
        Handles streaming of various types of media.

        :param mystic: The message object that triggered the stream.
        :param user_id: The ID of the user who triggered the stream.
        :param result: The result of the search query.
        :param chat_id: The ID of the chat where the stream will be played.
        :param user_name: The username of the user who triggered the stream.
        :param original_chat_id: The original chat ID where the stream will be played.
        :param video: Whether to stream a video or not.
        :param streamtype: The type of stream.
        :param spotify: Whether to force Spotify playback or not.
        :param forceplay: Whether to force play the stream or not.
        :return: The message object that acknowledges the stream has started.
        """
        if not result:
            return

        if forceplay:
            await Irop.force_stop_stream(chat_id)

        match streamtype:
            case "playlist":
                return await StreamHandler._playlist_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    spotify=spotify,
                    forceplay=forceplay,
                )
            case "youtube":
                return await StreamHandler._youtube_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    forceplay=forceplay,
                )
            case "soundcloud":
                return await StreamHandler._soundcloud_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    forceplay=forceplay,
                )
            case "telegram":
                return await StreamHandler._telegram_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    forceplay=forceplay,
                )
            case "live":
                return await StreamHandler._live_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    forceplay=forceplay,
                )
            case "index":
                return await StreamHandler._index_stream(
                    mystic=mystic,
                    user_id=user_id,
                    result=result,
                    chat_id=chat_id,
                    user_name=user_name,
                    original_chat_id=original_chat_id,
                    video=video,
                    forceplay=forceplay,
                )
            case _:
                raise AssistantErr("Invalid stream type")
    
    @staticmethod
    async def _playlist_stream(
        *,
        mystic: pyrogram.types.Message,
        user_id: int,
        result,
        chat_id: int,
        user_name: str,
        original_chat_id: int,
        video: Union[bool, str] = None,
        spotify: Union[bool, str] = None,
        forceplay: Union[bool, str] = None,
    ) -> Message:
        msg = f"{config.PLAY_19}\n\n"
        count = 0
        for search in result:
            if int(count) == config.PLAYLIST_FETCH_LIMIT:
                continue
            try:
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumb
