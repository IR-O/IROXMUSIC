# Importing necessary modules from pyrogram.types and config modules
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUPPORT_CHAT

# This function creates an InlineKeyboardButton object with the given text, URL, and callback data
def create_button(_, text, url=None, callback_data=None):
    # If URL is provided, create a button with the text and URL
    if url:
        return InlineKeyboardButton(text=_["S_B_9"], url=url)
    # If callback data is provided, create a button with the text and callback data
    elif callback_data:
        return InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=callback_data)

# This function creates an InlineKeyboardMarkup object with the given button
def create_markup(_, text, url=None, callback_data=None):
    button = create_button(_, text, url, callback_data)
    # Return a list containing the button as a single-item list
    return InlineKeyboardMarkup([[button]])

# This function creates a markup for botplaylist with the given text, URL, and callback data
def botplaylist_markup(_):
    # Return the markup created using the create_markup function
    return create_markup(_, _["S_B_9"], SUPPORT_CHAT, "close")

# This function creates a markup for closing the current window with the given text and callback data
def close_markup(_):
    # Return the markup created using the create_markup function
    return create_markup(_, _["CLOSE_BUTTON"], callback_data="close")

# This function creates a markup for support with the given text and URL
def supp_markup(_):
    # Return the markup created using the create_markup function
    return create_markup(_, _["S_B_9"], SUPPORT_CHAT)
