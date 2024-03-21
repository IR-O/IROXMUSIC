# Importing required modules
import re
from pykeyboard import InlineKeyboard  # Importing InlineKeyboard class from pykeyboard library
from pyrogram import filters  # Importing filters class from pyrogram library
from pyrogram.types import InlineKeyboardButton, Message, CallbackQuery  # Importing required types from pyrogram library

# Importing local modules
from IroXMusic import app  # Importing app instance from IroXMusic module
from IroXMusic.utils.database import get_lang, set_lang  # Importing get_lang and set_lang functions from IroXMusic.utils.database module
from IroXMusic.utils.decorators import ActualAdminCB, language, languageCB  # Importing required decorators
from config import BANNED_USERS  # Importing BANNED_USERS from config module
from strings import get_string, languages_present  # Importing get_string and languages_present functions from strings module

# Function to create a keyboard for language selection
def languages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)  # Creating an instance of InlineKeyboard class
    for i in languages_present:  # Iterating through languages_present
        keyboard.add(InlineKeyboardButton(text=languages_present[i], callback_data=f"languages:{i}"))  # Adding a button for each language
    keyboard.row(
        InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settingsback_helper"),  # Adding a back button
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),  # Adding a close button
    )
    return keyboard  # Returning the created keyboard

# Command handler for /lang, /setlang, and /language commands
@app.on_message(filters.command(["lang", "setlang", "language"]) & ~BANNED_USERS)
@language  # Using language decorator
async def langs_command(client, message: Message, _):
    keyboard = languages_keyboard(_)  # Creating a language selection keyboard
    await message.reply_text(
        _["lang_1"],  # Replying with a message to select language
        reply_markup=keyboard,
    )

# Callback query handler for LG regex
@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB  # Using languageCB decorator
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()  # Answering the callback query
    except:
        pass  # If any exception occurs, pass it
    keyboard = languages_keyboard(_)  # Creating a language selection keyboard
    await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)  # Editing the message with the new keyboard

# Callback query handler for languages:<language\_code> regex
@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB  # Using ActualAdminCB decorator
async def language_markup(client, CallbackQuery, _):
    langauge = CallbackQuery.data.split(":")[1]  # Extracting the selected language code
    old = await get_lang(CallbackQuery.message.chat.id)  # Getting the current language code
    if old == langauge:  # If the selected language is the same as the current language
        return  # Return without doing anything
    await set_lang(CallbackQuery.message.chat.id, langauge)  # Setting the new language
    await CallbackQuery.answer(_["lang_2"], show_alert=True)  # Showing a success message
