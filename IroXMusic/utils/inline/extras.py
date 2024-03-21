# Importing necessary modules from pyrogram.types and config modules
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT
from translate import gettext as _

def create_button(text, url=None, callback_data=None):
    """
    Create an InlineKeyboardButton object with the given text, URL, and callback data.
    """
    if callback_data is not None:
        button = InlineKeyboardButton(text, callback_data=callback_data)
    elif url is not None:
        button = InlineKeyboardButton(text, url=url)
    else:
        raise ValueError("Either url or callback_data must be provided")
    return button

def create_markup(buttons):
    """
    Create an InlineKeyboardMarkup object with the given list of buttons.
    """
    markup = InlineKeyboardMarkup(buttons)
    return markup

def get_support_button(text):
    """
    Create a support button with the given text and URL.
    """
    url = SUPPORT_CHAT
    button = create_button(text, url)
    return button

def botplaylist_markup():
    """
    Create a markup for botplaylist with the given text, URL, and callback data.
    """
    button = create_button(_["S_B_9"], url=SUPPORT_CHAT, callback_data="close")
    markup = create_markup([[button]])
    return markup

def close_markup():
    """
    Create a markup for closing the current window with the given text and callback data.
    """
    button
