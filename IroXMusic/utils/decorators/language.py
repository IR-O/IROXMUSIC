# Import necessary modules and functions
from strings import get_string # Import get\_string function from strings module

from IroXMusic import app # Import app from IroXMusic module
from IroXMusic.misc import SUDOERS # Import SUDOERS from IroXMusic.misc module
from IroXMusic.utils.database import get_lang, is_maintenance # Import get_lang and is_maintenance functions from IroXMusic.utils.database module


# Define an asynchronous function to get the chat language
async def get_chat_language(chat_id):
    try:
        # Get the language for the given chat_id
        language = await get_lang(chat_id)
        # Return the localized string for the language
        return get_string(language)
    except:
        # If there is an exception, return the localized string for English
        return get_string("en")


# Define a decorator to set the language for messages
def language(mystic):
    async def wrapper(_, message, **kwargs):
        if not await is_maintenance():
            # If maintenance mode is not enabled, set the language for the message
            message.language = await get_chat_language(message.chat.id)
        # Call the decorated function with the message object
        return await mystic(_, message)

    return wrapper


# Define a decorator to set the language for callback queries
def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if not await is_maintenance():
            # If maintenance mode is not enabled, set the language for the callback query
            CallbackQuery.message.language = await get_chat_language(CallbackQuery.message.chat.id)
        # Call the decorated function with the callback query object
        return await mystic(_, CallbackQuery)

    return wrapper


# Define a decorator to set the language for start messages
def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        message.language = await get_chat_language(message.chat.id)
       
