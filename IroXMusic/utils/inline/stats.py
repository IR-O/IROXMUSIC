from typing import List, Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def button(text: str, callback_data: str) -> InlineKeyboardButton:
    """Creates an InlineKeyboardButton object with the given text and callback_data."""
    return InlineKeyboardButton(text, callback_data=callback_data)

def keyboard_markup(buttons: List[List[Union[InlineKeyboardButton, str]]]) -> InlineKeyboardMarkup:
    """Creates an InlineKeyboardMarkup object with the given list of buttons."""
    return InlineKeyboardMarkup(buttons)

def stats_buttons(_, status) -> InlineKeyboardMarkup:
    """Creates a list of buttons for the stats command."""
    not_sudo = [button(_["SA_B_1"], "TopOverall")] if _["SA_B_1"] else []
    sudo = [button(_["SA_B_2"], "bot_stats_sudo"), button(_["SA_B_3"], "TopOverall")] if all([_["SA_B_2"], _["SA_B_3"]]) else []

    if status:
        buttons = sudo
    else:
        buttons = not_sudo

    return keyboard_markup(buttons)
