from pyrogram import filters
from pyrogram.types import Message
from typing import Optional

from IroXMusic import app
from IroXMusic.utils.database import get_loop as get_loop_db, set_loop as set_loop_db
from IroXMusic.utils.decorators import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS
from config import get_string as _

@app.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(cli, message: Message, _: Optional[str] = None, chat_id: int = None):
    if chat_id is None:
        return
    usage = _["admin_17"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    try:
        if state.isnumeric():
            state = int(state)
            if 1 <= state <= 10:
                got = await get_loop_db(chat_id)
                if got is not None:
                    state = got + state
                if int(state) > 10:
                    state = 10
                await set_loop_db(chat_id, state)
                return await message.reply_text(
                    text=_["admin_18"].format(state, message.from_user.mention),
                    reply_markup=close_markup(_),
                )
            else:
                return await message.reply_text(_["admin_17"])
        elif state.lower() == "enable":
            await set_loop_db(chat_id, 10)
            return await message.reply_text(
                text=_["admin_18"].format(state, message.from_user.mention),
                reply_markup=close_markup(_),
            )
        elif state.lower() == "disable":
            await set_loop_db(chat_id, 0)
            return await message.reply_text(
                _["admin_19"].format(message.from_user.mention),
                reply_markup
