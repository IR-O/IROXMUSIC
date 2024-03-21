import math
from typing import List, Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from IroXMusic.utils.formatters import time_to_seconds

def track_markup(
    videoid: str,  # The video ID for which the markup is generated
    user_id: int,  # The ID of the user who requested the markup
    channel: str,  # The channel or group where the markup will be displayed
    fplay: str  # The type of playback (audio or video)
) -> List[List[Union[InlineKeyboardButton, str]]]:
    """
    Generate InlineKeyboardMarkup for track.

    This function creates a markup for a single track with two buttons:
    'Play Audio' and 'Play Video'. It also includes a 'Close' button to
    dismiss the markup.
    """
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],  # Text for 'Play Audio' button
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],  # Text for 'Play Video' button
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],  # Text for 'Close' button
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(
    chat_id: int,  # The ID of the chat or group where the markup will be displayed
    played: str,  # The time elapsed since the stream started
    dur: str  # The total duration of the stream
) -> List[List[Union[InlineKeyboardButton, str]]]:
    """
    Generate InlineKeyboardMarkup for stream timer.

    This function creates a markup for a stream with several buttons:
    'Resume', 'Pause', 'Replay', 'Skip', 'Stop', and a progress bar.
    It also includes a 'Close' button to dismiss the markup.
    """
    played_sec = time_to_seconds(played)  # Convert played time to seconds
    duration_sec = time_to_seconds(dur)  # Convert total duration to seconds

    if duration_sec == 0:
        return []  # Return an empty markup if the duration is zero

    percentage = (played_sec / duration_sec) * 100  # Calculate the progress percentage
    umm = math.floor(percentage)  # Round the percentage to the nearest integer

    bar = ""  # Initialize the progress bar as an empty string
    # Generate the progress bar based on the percentage
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),  # Resume button
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),  # Pause button
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),  # Replay button
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),  # Skip button
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),  # Stop button
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",  # Progress bar and elapsed/total time
                callback_data="GetTimer",
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],  # Close button
    ]
    return buttons


def stream_markup(
    chat_id: int
) -> List[List[Union[InlineKeyboardButton, str]]]:
    """
    Generate InlineKeyboardMarkup for stream.

    This function creates a markup for a stream with several buttons:
    'Resume', 'Pause', 'Replay', 'Skip', 'Stop', and a 'Close' button to
    dismiss the markup.
    """
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),  # Resume button
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),  # Pause button
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),  # Replay button
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),  # Skip button
            InlineKeyboardButton(text="�
