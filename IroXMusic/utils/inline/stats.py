from typing import List, Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def button(text: str, callback_data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text, callback_data=callback_data)


def keyboard_markup(buttons: List[List[Union[InlineKeyboardButton, str]]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(buttons)


def stats_buttons(_, status):
    not_sudo = [button(_["SA_B_1"], "TopOverall")] if _["SA_B_1"] else []
    sudo = [button(_["SA_B_2"], "bot_stats_sudo"), button(_["SA_B_3"], "TopOverall")] if _["SA_B_2"] and _["SA_B_3"] else []
    buttons = [sudo if status and sudo else not_sudo, [button(_["CLOSE_BUTTON"], "close")]]
    return keyboard_markup(buttons)


def back_stats_buttons(_):
    buttons = [[button(_["BACK_BUTTON"], "stats_back"), button(_["CLOSE_BUTTON"], "close")]]
    return keyboard_markup(buttons)
