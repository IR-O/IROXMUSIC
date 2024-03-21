from typing import Union, Callable

import pyrogram  # Python wrapper for the Telegram Bot API
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import filters, types
from pyrogram.errors import FloodWait, UserAlreadyParticipant, ChatAdminRequired, ChatWriteForbidden

from IroXMusic import app
from IroXMusic.utils import help_pannel, private_help_panel
from IroXMusic.utils.database import get_lang
from IroXMusic.utils.decorators.language import LanguageStart
from IroXMusic.utils.inline.help import help_back_markup
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers

async def helper_private(client: app, update: Union[types.Message, CallbackQuery]) -> None:
    is_callback = isinstance(update, CallbackQuery)

    if is_callback:
        try:
            await update.answer()
        except pyrogram.errors.BotBlocked:
            return

        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)

        try:
            await update.edit_message_text(
                _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
            )
        except ChatWriteForbidden:
            return
    else:
        try:
            await update.delete()
        except FloodWait as e:
            await asyncio.sleep(e.x)
        except UserAlreadyParticipant:
            return

        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)

        try:
            await update.reply_photo(
                photo=START_IMG_URL,
                caption=_["help_1"].format(SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        except ChatAdminRequired:
            return
        except UserAlreadyParticipant:
            return

@LanguageStart
async def help_com_group(client: app, message: Message) -> None:
    try:
        keyboard = private_help_panel(_)
        await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))
    except UserAlreadyParticipant:
        return
    except ChatAdminRequired:
        return
    except ChatWriteForbidden:
        return

HELP_TEXTS = {
    "hb1": helpers.HELP_1,
    "hb2": helpers.HELP_2,
    "hb3": helpers.HELP_3
}
