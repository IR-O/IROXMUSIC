import asyncio
from typing import List, Dict

import pyrogram.filters
from pyrogram.types import Message
from pyrogram import Client as App

from IroXMusic.utils import (
    extract_user,
    int_to_alpha,
    get_authuser_names,
    get_authuser,
    delete_authuser,
    save_authuser,
)
from IroXMusic.utils.decorators import AdminActual
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS, adminlist


@app.on_message(pyrogram.filters.command("auth") & pyrogram.filters.group & ~BANNED_USERS)
@AdminActual
async def auth_command(client: App, message: Message):
    """Add a user to the authorized users list."""
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    auth_users = await get_authuser_names(message.chat.id)
    count = len(auth_users)
    if count == 25:
        return await message.reply_text(_["auth_1"])
    if token not in auth_users:
        assis = {
            "auth_user_id": user.id,
            "auth_name": user.first_name,
            "admin_id": message.from_user.id,
            "admin_name": message.from_user.first_name,
        }
        chat_admins = adminlist.get(message.chat.id)
        if chat_admins:
            if user.id not in chat_admins:
                chat_admins.append(user.id)
        await save_authuser(message.chat.id, token, assis)
        return await message.reply_text(_["auth_2"].format(user.mention))
    else:
        return await message.reply_text(_["auth_3"].format(user.mention))


@app.on_message(pyrogram.filters.command("unauth") & pyrogram.filters.group & ~BANNED_USERS)
@AdminActual
async def unauth_command(client: App, message: Message):
    """Remove a user from the authorized users list."""
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    deleted = await delete_authuser(message.chat.id, token)
    chat_admins = adminlist.get(message.chat.id)
    if chat_admins:
        if user.id in chat_admins:
            chat_admins.remove(user.id)
    if deleted:
        return await message.reply_text(_["auth_4"].format(user.mention))
    else:
        return await message.reply_text(_["auth_5"].format(user.mention))


@app.on_message(
    pyrogram.filters.command(["authlist", "authusers"]) & pyrogram.filters.group & ~BANNED_USERS
)
async def authusers_command(client: App, message: Message):
    """List the authorized users in the chat."""
    auth_users = await get_authuser_names(message.chat.id)
    if not auth_users:
        return await message.reply_text(_["setting_4"])
    else:
        j = 0
        reply_message = await message.reply_text(_["auth_6"])
        text = _["auth_7"].format(message.chat.title)
        async for auth_user in auth_users:
            try:
                user_data = await get_authuser(message.chat.id, auth_user)
                user_id = user_data["auth_user_id"]
                admin_id = user_data["admin_id"]
                admin_name = user_data["admin_name"]
                user = (await app.get_users(user_id)).first_name
                j += 1
            except Exception:
                continue
            text += f"{j}➤ {user}[<code>{user_id}</code>]\n"
            text += f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
        await reply_message.edit_text(text, reply_markup=close_markup(_))
