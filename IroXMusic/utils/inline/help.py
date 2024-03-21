from typing import Union  # Importing the Union type from typing module

import pyrogram.types  # Importing InlineKeyboardButton and InlineKeyboardMarkup from pyrogram.types

from IroXMusic import app  # Importing app from IroXMusic module

# The help_pannel function generates an inline keyboard markup for help commands
def help_pannel(_, START: Union[bool, int] = None):
    first = [    # Defining the first list of InlineKeyboardButton
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")
    ]
    second = [    # Defining the second list of InlineKeyboardButton
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first  # Setting the mark list based on the START value
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            # ... More lists of InlineKeyboardButton here
            [
                mark,  # Adding the mark list as the last button list
            ],
        ]
    )
    return upl  # Returning the generated InlineKeyboardMarkup

# The help_back_markup function generates an inline keyboard markup for the back button
def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl  # Returning the generated InlineKeyboardMarkup

# The private_help_panel function generates an inline keyboard markup for private help commands
def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons  # Returning the generated list of InlineKeyboardButton
