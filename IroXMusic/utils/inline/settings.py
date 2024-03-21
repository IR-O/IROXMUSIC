from typing import List, Union

from pyrogram.types import InlineKeyboardButton, CallbackQuery


def setting_markup(locale_dict: dict) -> List[List[InlineKeyboardButton]]:
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


def vote_mode_markup(
    locale_dict: dict, current_value: str, mode: Union[bool, str] = None
) -> List[List[InlineKeyboardButton]]:
    buttons = [
        [
            InlineKeyboardButton(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", callback_data="VOTEANSWER"),
            InlineKeyboardButton(
                text=locale_dict["ST_B_5"] if mode else locale_dict["ST_B_6"],
                callback_data="VOMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data=f"FERRARIUDTI M {current_value}"),
            InlineKeyboardButton(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current_value}",
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


def auth_users_markup(locale_dict: dict, status: Union[bool, str] = None) -> List[List[InlineKeyboardButton]]:
    buttons = [
        [
            InlineKeyboardButton(text=locale_dict["ST_B_7"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=locale_dict["ST_B_8"] if status else locale_dict["ST_B_9"],
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


def playmode_users_markup(
    locale_dict: dict,
    direct: Union[bool, str] = None,
    group: Union[bool, str] = None,
    playtype: Union[bool, str] = None,
) -> List[List[InlineKeyboardButton]]:
    buttons = [
        [
            InlineKeyboardButton(text=locale_dict["ST_B_10"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=locale_dict["ST_B_11"] if direct else locale_dict["ST_B_12"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=locale_dict["ST_B_13"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=locale_dict["ST_B_8"] if group else locale_dict["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=locale_dict["ST_B_14"], callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text=locale_dict["ST_B_8"] if playtype else locale_dict["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
            ),
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
