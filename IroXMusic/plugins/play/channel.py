from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message

from IroXMusic import app
from IroXMusic.utils.database import set_cmode
from IroXMusic.utils.decorators.admins import AdminActual
from config import BANNED_USERS

@app.on_message(filters.command(["channelplay"]) & filters.group & ~BANNED_USERS)
@AdminActual
async def playmode_(client, message: Message, _):
    # Check if the user provided a valid argument
    if len(message.command) < 2:
        return await message.reply_text(_["cplay_1"].format(message.chat.title))
    query = message.text.split(None, 2)[1].lower().strip()

    # Handle the "disable" argument
    if (str(query)).lower() == "disable":
        await set_cmode(message.chat.id, None)
        return await message.reply_text(_["cplay_7"])

    # Handle the "linked" argument
    elif str(query) == "linked":
        chat = await app.get_chat(message.chat.id)
        if chat.linked_chat:
            chat_id = chat.linked_chat.id
            await set_cmode(message.chat.id, chat_id)
            return await message.reply_text(
                _["cplay_3"].format(chat.linked_chat.title, chat.linked_chat.id)
            )
        else:
            return await message.reply_text(_["cplay_2"])

    # Handle the case where the user provided a channel username or ID
    else:
        try:
            chat = await app.get_chat(query)
        except:
            return await message.reply_text(_["cplay_4"])
        if chat.type != ChatType.CHANNEL:
            return await message.reply_text(_["cplay_5"])

        # Check if the bot has administrator privileges in the channel
        try:
            async for user in app.get_chat_members(
                chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if user.status == ChatMemberStatus.OWNER:
                    cusn = user.user.username
                    crid = user.user.id
        except:
            return await message.reply_text(_["cplay_4"])

        # Ensure the bot is the owner of the channel
        if crid != message.from_user.id:
            return await message.reply_text(_["cplay_6"].format(chat.title, cusn))

        # Set the playmode channel and inform the user
        await set_cmode(message.chat.id, chat.id)
        return await message.reply_text(_["cplay_3"].format(chat.title, chat.id))
