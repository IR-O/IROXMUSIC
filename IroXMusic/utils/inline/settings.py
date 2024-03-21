from typing import List, Union

from pyrogram.types import InlineKeyboardButton, CallbackQuery

def create_settings_markup(locale_dict: dict) -> List[List[InlineKeyboardButton]]:
    """Returns a list of lists of InlineKeyboardButton objects for a settings menu."""
    buttons = [
        [
            InlineKeyboardButton(text=locale_dict["ST_B_1"], callback_data="AU"),
            InlineKeyboardButton(text=locale_dict["ST_B_3"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=locale_dict["ST_B_2"], callback_data="PM"),
        ],
        [
            InlineKeyboardButton(text=locale_dict["ST_B_4"], callback_data="VM"),
        ],
        [
            InlineKeyboardButton(text=locale_dict["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons

def create_vote_mode_markup(
    locale_dict: dict, current_value: str, mode: Union[bool, str] = None
) -> List[List[InlineKeyboardButton]]:
    """Returns a list of lists of InlineKeyboardButton objects for a vote mode menu."""
    buttons = [
        [
            InlineKeyboardButton(text="Vᴏᴛᴇɪɴɢ ᴍᴏᴅᴇ", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text=locale_dict["TOGGLE_TEXT"] if mode is not None else locale_dict["ST_B_6"],
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data=f"FERRARIUDTI M {current_value}"),
            InlineKeyboardButton(
                text=f"Cᴜʀʀᴇɴᴛ : {current_value}",
                callback_data="ANSWERVOMODE",
            ),
            InlineKeyboardButton(text="+2", callback_data=f"FERRARIUDTI A {current_value}"),
        ],
        [
            InlineKeyboardButton(
                text=locale_dict["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=locale_dict["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons

def create_auth_users_markup(locale_dict: dict, status: Union[bool, str] = None) -> List[List[InlineKeyboardButton]]:
    """Returns a list of lists of InlineKeyboardButton objects for an authorization users menu."""
    buttons = [
        [
            InlineKeyboardButton(text=locale_dict["ST_B_7"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=locale_dict["AUTH_TEXT"] if status is not None else locale_dict["ST_B_9"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text=locale_dict["ST_B_1"], callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text=locale_dict["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=locale_dict["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons

def create_playmode_users_markup(
    locale_dict: dict,
    direct: Union[bool, str] = None,
    group: Union[bool, str] = None,
    playtype: Union[bool, str] = None,
) -> List[List[InlineKeyboardButton]]:
    """
    Returns a list of lists of InlineKeyboardButton objects for a play mode users menu.
    """
    buttons = [
        [
            InlineKeyboardButton(text=locale_dict["ST_B_10"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=locale_dict["PLAYMODE_TEXT"] if direct is not None else locale_dict["ST_B_12"},
                callback_data="PLAYMODE",
            ),
        ],
        # Add more buttons here for the group and playtype options
        [
            InlineKeyboardButton(
                text=locale_dict["BACK_BUTTON"],
                callback_data="settings_helper",
            ),
            InlineKeyboardButton(text=locale_dict["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
