from pyrogram.enums import ParseMode
from pyrogram.errors import ChatAdminRequired, UserIsBlocked

from IroXMusic import app, LOGGER_ID, USERNAME
from IroXMusic.utils.database import is_on_off
from IroXMusic.utils.decorators import errors

@errors
async def play_logs(message, streamtype):
    if not await is_on_off(2):
        return

    try:
        logger_text = (
            f"<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>\n"
            f"<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n"
            f"<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}\n"
            f"<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}\n"
            f"<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
            f"<b>ɴᴀᴍᴇ :</b> {message.from_user.first_name}\n"
            f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}\n"
            f"<b>sᴛʀᴇᴀᴍ ᴛʏᴘᴇ :</b> {streamtype}"
        )

        await app.send_message(
            LOGGER_ID,
            text=logger_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    except ChatAdminRequired:
        await message.reply(
            "⚠️ **I'm not a chat administrator, please add me as one and try again.**",
            parse_mode=ParseMode.MARKDOWN,
        )

    except UserIsBlocked:
        await message.reply(
            "⚠️ **You blocked me, unblock me and try again.**",
            parse_mode=ParseMode.MARKDOWN,
        )
