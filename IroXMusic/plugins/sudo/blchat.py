from pyrogram import filters, StopPropagation  # Importing filters, Message, StopPropagation from pyrogram library
from pyrogram.types import Message  # Importing Message from pyrogram.types
from typing import List, Union  # Importing List and Union from typing

from IroXMusic import app  # Importing app from IroXMusic
from IroXMusic.misc import SUDOERS, LOVE  # Importing SUDOERS and LOVE from IroXMusic.misc
from IroXMusic.utils.database import (
    blacklist_chat,
    blacklisted_chats,
    is_chat_blacklisted,
    whitelist_chat,
)  # Importing required functions from IroXMusic.utils.database
from IroXMusic.utils.decorators.language import language  # Importing language from IroXMusic.utils.decorators.language

# Helper function to check if a chat is blacklisted
async def is_chat_blacklisted(chat_id: int) -> bool:
    if chat_id in await blacklisted_chats():
        return True
    return await is_blacklisted_chat(chat_id)

# Decorator to listen for messages that contain "blchat" or "blacklistchat" command, only for sudoers and loved users
@app.on_message(filters.command(["blchat", "blacklistchat"]) & SUDOERS & LOVE)
# Function to blacklist a chat
@language  # Decorator to translate messages
async def blacklist_chat_func(client, message: Message, _):
    if len(message.command) != 2:  # Check if the command has only one argument
        return await message.reply_text(_["black_1"])  # If not, reply with error message
    chat_id = int(message.text.strip().split()[1])  # Extract the chat id from the command

    # Check if the chat exists in the database
    if chat_id not in await blacklisted_chats():
        try:
            await app.get_chat(chat_id)
        except:
            return await message.reply_text(_["black_8"])  # Reply with error message if the chat doesn't exist

    # Check if the chat is already blacklisted
    if await is_chat_blacklisted(chat_id):
        return await message.reply_text(_["black_2"])  # If yes, reply with error message

    # Check if the bot has permission to delete messages in the chat
    if await app.can_delete_messages(chat_id):
        success = await blacklist_chat(chat_id)  # Blacklist the chat

        # If the chat is blacklisted
        if success:  # If the chat is blacklisted
            await message.reply_text(_["black_3"])  # Reply with success message
        else:  # If the chat is not blacklisted
            await message.reply_text(_["black_9"])  # Reply with error message

        # Leave the chat
        try:
            await app.leave_chat(chat_id)
        except:
            pass  # If there is an error, ignore it
    else:
        await message.reply_text(_["black_10"])  # If the bot doesn't have permission to delete messages, reply with error message

    # Stop the propagation of the message to other filters
    raise StopPropagation

# Decorator to listen for messages that contain "whitelistchat", "unblacklistchat" or "unblchat" command, only for sudoers
@app.on_message(filters.command(["whitelistchat", "unblacklistchat", "unblchat"]) & SUDOERS)
# Function to whitelist a chat
@language  # Decorator to translate messages
async def white_funciton(client, message: Message, _):
    if len(message.command) != 2:  # Check if the command has only one argument
        return await message.reply_text(_["black_4"])  # If not, reply with error message
    chat_id = int(message.text.strip().split()[1])  # Extract the chat id from the command

    # Check if the chat is blacklisted
    if await is_chat_blacklisted(chat_id):
        success = await whitelist_chat(chat_id)  # Whitelist the chat

        # If the chat is whitelisted
        if success:  # If the chat is whitelisted
            await message.reply_text(_["black_6"])  # Reply with success message
        else:  # If the chat is not whitelisted
            await message.reply_text(_["black_5"])  # Reply with error message
    else:  # If the chat is not blacklisted
        await message.reply_text(_["black_5"])  # Reply with error message

    # Stop the propagation of the message to other filters
    raise StopPropagation

