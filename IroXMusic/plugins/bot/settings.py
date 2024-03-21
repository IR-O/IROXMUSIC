import logging
from typing import Literal

import pyrogram
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.filters import Command, Filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from IroXMusic import app
from IroXMusic.utils.database import (
    add_nonadmin_chat,
    get_authuser,
    get_authuser_names,
    get_playmode,
    get_playtype,
    get_upvote_count,
    is_nonadmin_chat,
    is_skipmode,
    remove_nonadmin_chat,
    set_playmode,
    set_playtype,
    set_upvotes,
    skip_off,
    skip_on,
)
from IroXMusic.utils.decorators.admins import ActualAdminCB
from IroXMusic.utils.decorators.language import language, languageCB
from IroXMusic.utils.inline.settings import (
    auth_users_markup,
    playmode_users_markup,
    setting_markup,
    vote_mode_markup,
)
from IroXMusic.utils.inline.start import private_panel
from config import BANNED_USERS, OWNER_ID

logger = logging.getLogger(__name__)

@app.on_message(Command(["settings", "setting"]) & Filters.group & ~BANNED_USERS)
@language
async def settings_mar(client: pyrogram.Client, message: Message, _: dict) -> None:
    """Show the settings menu for the group chat."""
    buttons = setting_markup(_)
    await message.reply_text(
        _["setting_1"].format(app.mention, message.chat.id, message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(Filters.regex("settings_helper") & ~BANNED_USERS)
@languageCB
async def settings_cb(client: pyrogram.Client, callback_query: CallbackQuery, _: dict) -> None:
    """Handle the "settings_helper" button press."""
    try:
        await callback_query.answer(_["set_cb_5"])
    except Exception:  # pylint: disable=broad-except
        logger.exception("Failed to answer callback query")
    buttons = setting_markup(_)
    return await callback_query.edit_message_text(
        _["setting_1"].format(
            app.mention,
            callback_query.message.chat.id,
            callback_query.message.chat.title,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(Filters.regex("settingsback_helper") & ~BANNED_USERS)
@languageCB
async def settings_back_markup(client: pyrogram.Client, callback_query: CallbackQuery, _: dict) -> None:
    """Handle the "settingsback_helper" button press."""
    try:
        await callback_query.answer()
    except Exception:  # pylint: disable=broad-except
        logger.exception("Failed to answer callback query")
    if callback_query.message.chat.type == ChatType.PRIVATE:
        await app.resolve_peer(OWNER_ID)
        OWNER = OWNER_ID
        buttons = private_panel(_)
        return await callback_query.edit_message_text(
            _["start_2"].format(callback_query.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = setting_markup(_)
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons)
        )


@app.on_callback_query(
    Filters.regex(
        pattern=r"^(SEARCHANSWER|PLAYMODEANSWER|PLAYTYPEANSWER|AUTHANSWER|ANSWERVOMODE|VOTEANSWER|PM|AU|VM)$"
    )
    & ~BANNED_USERS
)
@languageCB
async def without_Admin_rights(
    client: pyrogram.Client, callback_query: CallbackQuery, _: dict
) -> None:
    """Handle button presses that don't require admin rights."""
    command = callback_query.matches[0].group(1)
    if command == "SEARCHANSWER":
        try:
            await callback_query.answer(_["setting_2"], show_alert=True)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Failed to answer callback query")
    if command == "PLAYMODEANSWER":
        try:
            await callback_query.answer(_["setting_5"], show_alert=True)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Failed to answer callback query")
    if command == "PLAYTYPEANSWER":
        try:
            await callback_query.answer(_["setting_6"], show_alert=True)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Failed to answer callback query")
    if command == "AUTHANSWER":

