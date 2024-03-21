from typing import List, Optional

from pyrogram.types import InlineKeyboardButton

import config
from IroXMusic import app


def start_panel() -> List[List[InlineKeyboardButton]]:
    buttons = [
        [
            InlineKeyboardButton(
                text=config.START_BUTTON_1,
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            InlineKeyboardButton(text=config.START_BUTTON_2, url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel() -> List[List[InlineKeyboardButton]]:
    support_chat = config.SUPPORT_CHAT if config.SUPPORT_CHAT else "https://t.me/your_support_chat"
    owner_id = config.OWNER_ID if config.OWNER_ID else 0
    buttons = [
        [
            InlineKeyboardButton(
                text=config.PRIVATE_BUTTON_3,
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=config.PRIVATE_BUTTON_4, callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text=config.PRIVATE_BUTTON_5, user_id=owner_id),
            InlineKeyboardButton(text=config.START_BUTTON_2, url=support_chat),
        ],
        [
            InlineKeyboardButton(text=config.PRIVATE_BUTTON_6, url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=config.PRIVATE_BUTTON_7, url=config.UPSTREAM_REPO),
        ],
