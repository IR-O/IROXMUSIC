from strings import get_string

from IroXMusic import app
from IroXMusic.misc import SUDOERS
from IroXMusic.utils.database import get_lang, is_maintenance


async def get_chat_language(chat_id):
    try:
        language = await get_lang(chat_id)
        return get_string(language)
    except:
        return get_string("en")


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if not await is_maintenance():
            message.language = await get_chat_language(message.chat.id)
        return await mystic(_, message)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if not await is_maintenance():
            CallbackQuery.message.language = await get_chat_language(CallbackQuery.message.chat.id)
        return await mystic(_, CallbackQuery)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        message.language = await get_chat_language(message.chat.id)
        return await mystic(_, message)

    return wrapper
