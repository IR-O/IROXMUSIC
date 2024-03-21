# Importing necessary modules from pyrogram.types and config modules
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT
from translate import gettext as _

def create_button(text, url=None, callback_data=None):
    """
    Create an InlineKeyboardButton object with the given text, URL, and callback data.
    """
    button = InlineKeyboardButton(text, url=url, callback_data=callback_data)
    return button

def create_markup(button):
    """
    Create an InlineKeyboardMarkup object with the given button.
    """
    markup = InlineKeyboardMarkup([[button]])
    return markup

def botplaylist_markup():
    """
    Create a markup for botplaylist with the given text, URL, and callback data.
    """
    url = SUPPORT_CHAT
    button = create_button(_["S_B_9"], url, "close")
    markup = create_markup(button)
    return markup

def close_markup():
    """
    Create a markup for closing the current window with the given text and callback data.
    """
    button = create_button(_["CLOSE_BUTTON"], callback_data="close")
    markup = create_markup(button)
    return markup

def supp_markup():
    """
    Create a markup for support with the given text and URL.
    """
    url = SUPPORT_CHAT
    button = create_button(_["S_B_9"], url)
    markup = create_markup(button)
    return markup
