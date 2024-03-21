from pyrogram import filters, StopPropagation  # Importing filters, Message, StopPropagation from pyrogram library
from pyrogram.types import Message  # Importing Message from pyrogram.types
from typing import List, Union  # Importing List and Union from typing

from IroXMusic import app  # Importing app from IroXMusic
from IroXMusic.misc import SUDOERS, LOVE  # Importing SUDOERS and LOVE from IroXMusic.misc
from IroXMusic.utils.database import blacklist_chat, blacklisted_chats, is_blacklisted_chat, whitelist_chat  # Importing required functions from IroXMusic.utils.database
from IroXMusic.utils.decorators.language import language  # Importing language from IroXMusic.utils.decorators.language

@app.on_message(filters.command(["blchat", "blacklistchat"]) & SUDOERS & LOVE)  # Decorator to listen for messages that contain "blchat" or "blacklistchat" command, only for sudoers and loved users
@language  # Decorator to translate messages
async def blacklist_chat_func(client, message: Message, _):  # Function to blacklist a chat
    if len(message.command) != 2:  # Check if the command has only one argument
        return await message.reply_text(_["black_1"])  # If not, reply with error message
    chat_id = int(message.text.strip().split()[1])  # Extract the chat id from the command
    if chat_id in await blacklisted_chats():  # Check if the chat is already blacklisted
        return await message.reply_text(_["black_2"])  # If yes, reply with error message
    if await is_blacklisted_chat(chat_id):  # Check if the chat is already blacklisted
        return await message.reply_text(_["black_2"])  # If yes, reply with error message
    if await app.can_delete_messages(chat_id):  # Check if the bot has permission to delete messages in the chat
        blacklisted = await blacklist_chat(chat_id)  # Blacklist the chat
        if blacklisted:  # If the chat is blacklisted
            await message.reply_text(_["black_3"])  # Reply with success message
        else:  # If the chat is not blacklisted
            await message.reply_text(_["black_9"])  # Reply with error message
        try:
            await app.leave_chat(chat_id)  # Leave the chat
        except:
            pass  # If there is an error, ignore it
    else:
        await message.reply_text(_["black_10"])  # If the bot doesn't have permission to delete messages, reply with error message
    raise StopPropagation  # Stop the propagation of the message to other filters

@app.on_message(filters.command(["whitelistchat", "unblacklistchat", "unblchat"]) & SUDOERS)  # Decorator to listen for messages that contain "whitelistchat", "unblacklistchat" or "unblchat" command, only for sudoers
@language  # Decorator to translate messages
async def white_funciton(client, message: Message, _):  # Function to whitelist a chat
    if len(message.command) != 2:  # Check if the command has only one argument
        return await message.reply_text(_["black_4"])  # If not, reply with error message
    chat_id = int(message.text.strip().split()[1])  # Extract the chat id from the command
    if chat_id not in await blacklisted_chats():  # Check if the chat is not blacklisted
        return await message.reply_text(_["black_5"])  # If not, reply with error message
    if await is_blacklisted_chat(chat_id):  # Check if the chat is blacklisted
        await whitelist_chat(chat_id)  # Whitelist the chat
        await message.reply_text(_["black_6"])  # Reply with success message
    else:  # If the chat is not blacklisted
        await message.reply_text(_["black_5"])  # Reply with error message
    raise StopPropagation  # Stop the propagation of the message to other filters
