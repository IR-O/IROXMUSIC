from typing import Union  # for type hinting of union types

import pyrogram  # Python wrapper for the Telegram Bot API
from pyrogram.types import InlineKeyboardMarkup, Message  # for creating keyboard markups
from pyrogram import filters, types  # for creating filters and handling various types of Telegram messages
from pyrogram.errors import FloodWait  # for handling flood wait errors

from IroXMusic import app  # the main Pyrogram application instance
from IroXMusic.utils import help_pannel, private_help_panel  # utility functions for creating help panels
from IroXMusic.utils.database import get_lang  # utility function for getting the user's language
from IroXMusic.utils.decorators.language import LanguageStart  # decorator for handling language translations
from IroXMusic.utils.inline.help import help_back_markup  # utility function for creating a help back button
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT  # various configuration variables
from strings import get_string, helpers  # utility functions for getting translated strings and help text

# A helper function to handle private messages and callback queries
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    # Check if the update is a callback query
    is_callback = isinstance(update, types.CallbackQuery)

    if is_callback:
        # Answer the callback query to hide the default loading state
        await update.answer()
        # Get the chat ID from the message that the callback query belongs to
        chat_id = update.message.chat.id
        # Get the user's language
        language = await get_lang(chat_id)
        # Get the translated strings for the help panel
        _ = get_string(language)
        # Create the help panel keyboard markup
        keyboard = help_pannel(_, True)
        # Edit the message text and reply markup for the callback query
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        # Delete the incoming message to prevent flooding the chat
        try:
            await update.delete()
        except FloodWait as e:
            # If the deletion is rate-limited, wait for the specified amount of time
            await asyncio.sleep(e.x)
        # Get the user's language
        language = await get_lang(update.chat.id)
        # Get the translated strings for the help panel
        _ = get_string(language)
        # Create the help panel keyboard markup
        keyboard = help_pannel(_)
        # Send a photo and help panel to the user
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )

# A command handler for displaying the help panel in a group chat
@LanguageStart
async def help_com_group(client, message: Message, _):
    # Create the help panel keyboard markup
    keyboard = private_help_panel(_)
    # Send the help panel to the user
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))

# A dictionary of help text callback data and their corresponding help text
HELP_TEXTS = {
    "hb1": helpers.HELP_1,
    "hb2": helpers.HELP_2,
    "hb3": helpers.HELP_3
