class StreamHandler:
    @staticmethod
    async def stream(
        *,
        mystic: pyrogram.types.Message,  # The message object that triggered the stream.
        user_id: int,  # The ID of the user who triggered the stream.
        result,  # The result of the search query.
        chat_id: int,  # The ID of the chat where the stream will be played.
        user_name: str,  # The username of the user who triggered the stream.
        original_chat_id: int,  # The original chat ID where the stream will be played.
        video: Union[bool, str] = None,  # Whether to stream a video or not.
        streamtype: Union[bool, str] = None,  # The type of stream.
        spotify: Union[bool, str] = None,  # Whether to force Spotify playback or not.
        forceplay: Union[bool, str] = None,  # Whether to force play the stream or not.
    ) -> Message:
        """
        Handles streaming of various types of media.

        This method determines the type of stream requested by the user and delegates the streaming process to the appropriate
        private method within the `StreamHandler` class. It supports streaming from YouTube, SoundCloud, Telegram, and
        Live DVR sources, as well as playing playlists and indexes.

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
