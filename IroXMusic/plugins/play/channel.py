from pyrogram import filters, StopPropagation
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus, ChatType
from pyrogram.types import Message

from IroXMusic import app
from IroXMusic.utils.database import set_cmode
from IroXMusic.utils.decorators.admins import AdminActual
from config import BANNED_USERS

_support = {
    "cplay_1": "Please provide a valid argument for the channelplay command.",
    "cplay_2": "This group is not linked to any channel.",
    "cplay_3": "The playmode channel has been set to {channel_title} ({channel_id}).",
    "cplay_4": "An error occurred while processing the request. Please try again later.",
    "cplay_5": "The provided chat is not a channel.",
    "cplay_6": "This channel ({channel_title}) is owned by {owner_username}, not you.",
    "cplay_7": "The playmode channel has been successfully unset.",
}

@app.on_message(filters.command(["channelplay"]) & filters.group & ~BANNED_USERS)
@AdminActual
async def playmode_(client, message: Message):
    args = message.text.split(None, 2)[1:]
    query = args[0].lower().strip() if args else ""

    if len(args) > 1:
        return await message.reply_text(_support["cplay_1"])

    if query == "disable":
        await set_cmode(message.chat.id, None)
        return await message.reply_text(_support["cplay_7"])

    if query == "linked":
        chat = await app.get_chat(message.chat.id)
        if chat.linked_chat:
            chat_id = chat.linked_chat.id
            await set_cmode(message.chat.id, chat_id)
            return await message.reply_text(_support["cplay_3"].format(channel_title=chat.linked_chat.title, channel_id=chat.linked_chat.id))
        else:
            return await message.reply_text(_support["cplay_2"])

    try:
        chat = await app.get_chat(query)
    except:
        return await message.reply_text(_support["cplay_4"])

    if chat.type != ChatType.CHANNEL:
        return await message.reply_text(_support["cplay_5"])

    try:
        async for user in app.get_chat_members(chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
            if user.status == ChatMemberStatus.OWNER and user.user.id == message.from_user.id:
                await set_cmode(message.chat.id, chat.id)
                return await message.reply_text(_support["cplay_3"].format(channel_title=chat.title, channel_id=chat.id))
    except:
        return await message.reply_text(_support["cplay_4"])

    return await message.reply_text(_support["cplay_6"].format(channel_title=chat.title, owner_username=chat.owner.username))
