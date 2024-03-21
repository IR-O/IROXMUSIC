from typing import Union  # Importing Union from typing for specifying multiple types for a variable

import pyrogram  # Pyrogram library for creating a Telegram bot
from pyrogram.types import InlineKeyboardMarkup, Message  # Importing required types from pyrogram.types
from pyrogram import filters, types  # Importing required filters and types from pyrogram

from IroXMusic import app  # Importing app instance from IroXMusic
from IroXMusic.utils import help_pannel, private_help_panel  # Importing helper functions
from IroXMusic.utils.database import get_lang  # Importing function to get user's language
from IroXMusic.utils.decorators.language import LanguageStart  # Importing language decorator
from IroXMusic.utils.inline.help import help_back_markup  # Importing function to create back button
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT  # Importing required configurations
from strings import get_string, helpers  # Importing required strings and helper functions

# @app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
# @app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
# Decorators to handle help command in private chat and callback queries
# ~BANNED_USERS is used to ignore banned users
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    # is_callback is used to check if the update is a callback query

    if is_callback:
        try:
            await update.answer()
        except:
            pass
        # answer() method is used to send an answer to the callback query
        # If any error occurs, it is ignored

        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        # language is used to get the user's language
        # _ is used to get the translated strings

        keyboard = help_pannel(_, True)
        # keyboard is created using help_pannel function

        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
        # edit_message_text() method is used to edit the message text
        # The new text is formatted using _["help_1"] and SUPPORT_CHAT

    else:
        try:
            await update.delete()
        except:
            pass
        # delete() method is used to delete the message
        # If any error occurs, it is ignored

        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        # Similar to above, language and _ are used
        # keyboard is created using help_pannel function

        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )
        # reply_photo() method is used to reply to the message with a photo
        # The new text is formatted using _["help_1"] and SUPPORT_CHAT
        # keyboard is passed as a parameter


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    # keyboard is created using private_help_panel function

    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))
    # reply_text() method is used to reply to the message with text
    # The new text is formatted using _["help_2"]
    # keyboard is passed as a parameter


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    # callback_data is the data sent with the callback query
    # cb is the command to be executed

    keyboard = help_back_markup(_)
    # keyboard is created using help_back_markup function

    if cb == "hb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "hb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "hb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "hb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "hb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "hb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "hb10
