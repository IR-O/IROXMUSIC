import pyrogram
from typing import Union
from exceptions import AssistantErr

class StreamHandler:
    @staticmethod
    async def stream(
        mystic,  # The message object that triggered the stream.
        user_id,  # The ID of the user who triggered the stream.
        result,  # The result of the search query.
        chat_id,  # The ID of the chat where the stream will be played.
        user_name,  # The username of the user who triggered the stream.
        original_chat_id,  # The original chat ID where the stream will be played.
        video=None,  # Whether to stream a video or not.
        streamtype=None,  # The type of stream.
        spotify=None,  # Whether to force Spotify playback or not.
        forceplay=None,  # Whether to force play the stream or not.
    ) -> pyrogram.types.Message:
        # If there's no result, return without doing anything.
        if not result:
            return

        # If forceplay is set to True, stop any currently playing stream.
        if forceplay:
            await Irop.force_stop_stream(chat_id)

        # Determine the stream type and delegate the streaming process to the appropriate private method.
        match streamtype:
            case "playlist":
                return await StreamHandler._playlist_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    spotify,
                    forceplay,
                )
            case "youtube":
                return await StreamHandler._youtube_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    forceplay,
                )
            case "soundcloud":
                return await StreamHandler._soundcloud_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    forceplay,
                )
            case "telegram":
                return await StreamHandler._telegram_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    forceplay,
                )
            case "live":
                return await StreamHandler._live_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    forceplay,
                )
            case "index":
                return await StreamHandler._index_stream(
                    mystic,
                    user_id,
                    result,
                    chat_id,
                    user_name,
                    original_chat_id,
                    video,
                    forceplay,
                )
            case _:
                raise AssistantErr("Invalid stream type")
