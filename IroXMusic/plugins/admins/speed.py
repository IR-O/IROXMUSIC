from pyrogram import filters, types
from pyrogram.errors import ChatAdminRequired

from IroXMusic import app
from IroXMusic.core.call import Irop
from IroXMusic.misc import SUDOERS, db
from IroXMusic.utils import AdminRightsCheck
from IroXMusic.utils.database import is_active_chat, is_nonadmin_chat
from IroXMusic.utils.decorators.language import languageCB
from IroXMusic.utils.inline import close_markup, speed_markup
from config import BANNED_USERS, adminlist

checker: list = []

@app.on_message(
    filters.command(["cspeed", "speed", "cslow", "slow", "playback", "cplayback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def playback(cli, message: types.Message, _, chat_id: int):
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = playing[0]["seconds"]
    if not duration_seconds:
        return await message.reply_text(_["admin_27"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await message.reply_text(_["admin_27"])
    upl = speed_markup(_, chat_id)
    return await message.reply_text(
        text=_["admin_28"].format(app.mention),
        reply_markup=upl,
    )

@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
    if not is_non_admin:
        try:
            await AdminRightsCheck(CallbackQuery.message)
        except ChatAdminRequired:
            return await CallbackQuery.answer(_["admin_13"], show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await CallbackQuery.answer(_["queue_2"], show_alert=True)
    duration_seconds = playing[0]["seconds"]
    if not duration_seconds:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    check_speed = playing[0].get("speed")
    if check_speed is None:
        return await CallbackQuery.answer(_["admin_27"], show_alert=True)
    if check_speed == float(speed):
        if speed == "1.0":
            return await CallbackQuery.answer(_["admin_29"], show_alert=True)
        else:
            return await CallbackQuery.answer(_["admin_30"], show_alert=True)
    await Irop.change_speed(callback_query_id=CallbackQuery.id, speed=speed)
    await CallbackQuery.answer()
