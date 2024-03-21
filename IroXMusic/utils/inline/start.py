from typing import List, Optional

from pyrogram.types import InlineKeyboardButton

import config
from IroXMusic import app

def get_button(text: str, url: str) -> InlineKeyboardButton:
    # This function returns an InlineKeyboardButton object with the given text and url.
    return InlineKeyboardButton(text=text, url=url)

def get_support_chat() -> str:
    # This function returns the support chat URL as a string.
    # If the SUPPORT_CHAT variable is defined in the config module, it will be used,
    # otherwise, the default value "https://t.me/your_support_chat" will be returned.
    return config.SUPPORT_CHAT if config.SUPPORT_CHAT else "https://t.me/your_support_chat"

def get_owner_id() -> int:
    # This function returns the owner ID as an integer.
    # If the OWNER_ID variable is defined in the config module, it will be used,
    # otherwise, the default value 0 will be returned.
    return config.OWNER_ID if config.OWNER_ID else 0

def start_panel() -> List[List[InlineKeyboardButton]]:
    # This function returns a list of lists of InlineKeyboardButton objects,
    # which represents the start panel.
    return [
        (
            get_button(config.START_BUTTON_1, f"https://t.me/{app.username}?startgroup=true"),
            get_button(config.START_BUTTON_2, get_support_chat()),
        )
    ]

def private_panel() -> List[List[InlineKeyboardButton]]:
    # This function returns a list of lists of InlineKeyboardButton objects,
    # which represents the private panel.
    support_chat = get_support_chat()
    owner_id = get_owner_id()
    return [
        (
            get_button(config.PRIVATE_BUTTON_3, f"https://t.me/{app.username}?startgroup=true"),
        ),
        (
            get_button("Support", support_chat),
            get_button("Owner", f"https://t.me/{app.username}?start=owner_{owner_id}"),
        )
    ]
