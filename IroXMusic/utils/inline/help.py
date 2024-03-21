from typing import Union

import pyrogram.types
from pyrogram import filters

from irox_music import app

# The help_pannel function generates an inline keyboard markup for help commands
def help_pannel(bot, update: Union[bool, int] = None, _=None):
    """Generate help inline keyboard markup."""
    if _ is None:
        raise ValueError("The '_' variable is not defined.")

    first = [
        pyrogram.types.InlineKeyboardButton(
            text=_["CLOSE_BUTTON"], callback_data=f"close")
    ]

    second = [
        pyrogram.types.InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]

    mark = second if update else first

    upl = pyrogram.types.InlineKeyboardMarkup(
        [
            [
                pyrogram.types.InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                pyrogram.types.InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
                pyrogram.types.InlineKeyboardButton(
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

    return upl

# The help_back_markup function generates an inline keyboard markup for the back button
def help_back_markup(bot, _=None):
    """Generate help back inline keyboard markup."""
    if _ is None:
        raise ValueError("The '_' variable is not defined.")

    upl = pyrogram.types.InlineKeyboardMarkup(
        [
            [
                pyrogram.types.InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )

    return upl

# The private_help_panel function generates an inline keyboard markup for private help commands
def private_help_panel(bot, _=None):
    """Generate private help inline keyboard markup."""
    if _ is None:
        raise ValueError("The '_' variable is not defined.")

    buttons = [
        [
            pyrogram.types.InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]

    return buttons
