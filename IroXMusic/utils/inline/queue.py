from typing import Union  # Importing the Union type from typing module

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup  # Importing necessary classes from pyrogram.types module

# Function to create queue markup
def queue_markup(
    _,  # Underscore is used as a conventional name for the first parameter in decorators
    DURATION,  # The duration of the video
    CPLAY,  # The command play
    videoid,  # The ID of the video
    played: Union[bool, int] = None,  # Whether the video has been played or not, or the elapsed time of the video
    dur: Union[bool, int] = None,  # The duration of the video or a boolean value indicating if the duration is known
):
    not_dur = [ # If the duration is unknown, create a list of InlineKeyboardButton objects
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
    dur = [ # If the duration is known, create a list of InlineKeyboardButton objects
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),  # The text on the button
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
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)  # Create an InlineKeyboardMarkup object with the appropriate list of buttons
    return upl  # Return the InlineKeyboardMarkup object


# Function to create queue back markup
def queue_back_markup(_, CPLAY):
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
              `enter code here`                ),
            ]
        ]
    )
    return upl  # Return the InlineKeyboardMarkup object


# Function to create admin markup
def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),  # The text on the button and
