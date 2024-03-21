from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Function to create queue markup
def queue_markup(
    _,  # Underscore is used as a conventional name for the first parameter in decorators
    DURATION: str,  # The duration of the video
    CPLAY: str,  # The command play
    videoid: str,  # The ID of the video
    played: Union[bool, int] = None,  # Whether the video has been played or not, or the elapsed time of the video
    dur: Union[bool, int] = None,  # The duration of the video or a boolean value indicating if the duration is known
) -> InlineKeyboardMarkup:
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],  # The text on the button
                callback_data=f"GetQueued {CPLAY}|{videoid}",  # The data to be sent along with the callback query
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]

    if isinstance(DURATION, str) and DURATION == "Unknown":
        upl = InlineKeyboardMarkup(not_dur)
    else:
        if isinstance(dur, bool) and dur:
            dur = _["QU_B_3"]
        elif isinstance(dur, int):
            dur = _["QU_B_4"].format(dur)

        if isinstance(played, bool) and played:
            played = _["QU_B_5"].format(played)
        elif isinstance(played, int):
            played = _["QU_B_6"].format(played)

        dur = [
            [
                InlineKeyboardButton(
                    text=_(f"QU_B_2_{int(dur != 'Unknown')}").format(played, dur),  # The text on the button
                    callback_data="GetTimer",  # The data to be sent along with the callback query
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["QU_B_1"],  # The text on the button
                    callback_data=f"GetQueued {CPLAY}|{videoid}",  # The data to be sent along with the callback query
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]

        upl = InlineKeyboardMarkup(dur)

    return upl


# Function to create queue back markup
def queue_back_markup(_, CPLAY: str) -> InlineKeyboardMarkup:
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],  # The text on the button
                    callback_data=f"queue_back_timer {CPLAY}",  # The data to be sent along with the callback query
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


# Function to create admin markup
def aq_markup(_, chat_id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),  # The text on the button
            InlineKeyboardButton(text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"),  # The text on the button
            InlineKeyboardButton(text="⏸", callback_data=f"ADMIN Stop|{chat_id}"),  # The text on the button
        ],
        [
            InlineKeyboardButton(text="🗑", callback_data=f"ADMIN Clear|{chat_id}"),  # The text on the button
            InlineKeyboardButton(text="🔄", callback_data=f"ADMIN Refresh|{chat_id}"),  # The text on the button
        ],
        [
            InlineKeyboardButton(text="🔙", callback_data=f"queue_back_timer {CPLAY
