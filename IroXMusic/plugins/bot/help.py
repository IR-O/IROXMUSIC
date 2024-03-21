from typing import Union

import pyrogram
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram import filters, types

from IroXMusic import app
from IroXMusic.utils import help_pannel, private_help_panel
from IroXMusic.utils.database import get_lang
from IroXMusic.utils.decorators.language import LanguageStart
from IroXMusic.utils.inline.help import help_back_markup
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers

async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)

    if is_callback:
        await update.answer()
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass

        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


HELP_TEXTS = {
    "hb1": helpers.HELP_1,
    "hb2": helpers.HELP_2,
    "hb3": helpers.HELP_3,
    "hb4": helpers.HELP_4,
    "hb5": helpers.HELP_5,
    "hb6": helpers.HELP_6,
    "hb7": helpers.HELP_7,
    "hb8": helpers.HELP_8,
    "hb9": helpers.HELP_9,
    "hb10": helpers.HELP_10,
}

@filters.create(lambda _, __, query: query.data.startswith("help_callback"))
@LanguageStart
async def helper_cb(client, CallbackQuery, _, query):
    callback_data = query.data.strip()
    cb = callback_data.split(None, 1)[1]

    keyboard = help_back_markup(_)
    text = HELP_TEXTS.get(cb)

    if text:
        await CallbackQuery.edit_message_text(text, reply_markup=keyboard)
