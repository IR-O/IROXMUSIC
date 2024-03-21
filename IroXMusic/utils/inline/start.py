from typing import List, Optional

from pyrogram.types import InlineKeyboardButton

import config
from IroXMusic import app

def get_button(text: str, url: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, url=url)

def get_support_chat() -> str:
    return config.SUPPORT_CHAT if config.SUPPORT_CHAT else "https://t.me/your_support_chat"

def get_owner_id() -> int:
    return config.OWNER_ID if config.OWNER_ID else 0

def start_panel() -> List[List[InlineKeyboardButton]]:
    return [
        [
            get_button(config.START_BUTTON_1, f"https://t.me/{app.username}?startgroup=true"),
            get_button(config.START_BUTTON_2, config.SUPPORT_CHAT),
        ]
    ]

def private_panel() -> List[List[InlineKeyboardButton]]:
    support_chat = get_support_chat()
    owner_id = get_owner_id()
    return [
        [
            get_button(config.PRIVATE_BUTTON_3, f"https://t.me/{app.username}?startgroup=true"),
        ],
        [
            get_button(config.PRIVATE_BUTTON_4, f"settings_{owner_id}"),
        ]
    ]
