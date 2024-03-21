from typing import List, Optional

from pyrogram.types import InlineKeyboardButton

import config
from IroXMusic import app

# This function generates a list of InlineKeyboardButton lists for the start panel
def start_panel() -> List[List[InlineKeyboardButton]]:
    buttons = [
        # This list contains two InlineKeyboardButton objects
        [
            # The first button is created with the text from config.START_BUTTON_1
            # and a URL that opens a group chat with the bot
            InlineKeyboardButton(
                text=config.START_BUTTON_1,
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            # The second button is created with the text from config.START_BUTTON_2
            # and a URL for the support chat
            InlineKeyboardButton(text=config.START_BUTTON_2, url=config.SUPPORT_CHAT),
        ],
    ]
    # The function returns the buttons list
    return buttons

# This function generates a list of InlineKeyboardButton lists for the private panel
def private_panel() -> List[List[InlineKeyboardButton]]:
    # support_chat is set to the value of config.SUPPORT_CHAT if it exists,
    # otherwise it is set to "https://t.me/your_support_chat"
    support_chat = config.SUPPORT_CHAT if config.SUPPORT_CHAT else "https://t.me/your_support_chat"
    # owner_id is set to the value of config.OWNER_ID if it exists,
    # otherwise it is set to 0
    owner_id = config.OWNER_ID if config.OWNER_ID else 0
    buttons = [
        # This list contains one InlineKeyboardButton object
        [
            # The button is created with the text from config.PRIVATE_BUTTON_3
            # and a URL that opens a group chat with the bot
            InlineKeyboardButton(
                text=config.PRIVATE_BUTTON_3,
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        # This list contains one InlineKeyboardButton object
        [
            # The button is created with the text from config.PRIVATE_BUTTON_4
            # and a callback data of "settings_
