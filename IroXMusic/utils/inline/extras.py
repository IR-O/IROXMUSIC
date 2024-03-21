from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT

def create_button(_, text, url=None, callback_data=None):
    if url:
        return InlineKeyboardButton(text=_["S_B_9"], url=url)
    elif callback_data:
        return InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=callback_data)

def create_markup(_, text, url=None, callback_data=None):
    button = create_button(_, text, url, callback_data)
    return InlineKeyboardMarkup([[button]])

def botplaylist_markup(_):
    return create_markup(_, _["S_B_9"], SUPPORT_CHAT, "close")

def close_markup(_):
    return create_markup(_, _["CLOSE_BUTTON"], callback_data="close")

def supp_markup(_):
    return create_markup(_, _["S_B_9"], SUPPORT_CHAT)
