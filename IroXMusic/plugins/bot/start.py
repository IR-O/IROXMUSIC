import time
from typing import List, Union  # Importing necessary modules and libraries

import aioschedule as schedule
import pyrogram
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, ChatBannedRightsError, UserBannedInChannel
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config  # Importing config module
from IroXMusic import app, LOGGER, SUDO_USERS  # Importing app, LOGGER and SUDO_USERS from IroXMusic module
from IroXMusic.misc import _boot_
from IroXMusic.plugins.sudo.sudoers import sudoers_list
from IroXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from IroXMusic.utils.decorators.language import LanguageStart
from IroXMusic.utils.formatters import get_readable_time
from IroXMusic.utils.inline import help_pannel, private_panel, start_panel

@app.on_message(filters.command(["start"]) & filters.private & ~config.BANNED_USERS)
@LanguageStart
async def start_pm(_, message: Message) -> None:  # Defining the start_pm function to handle start command in private chat
    await add_served_user(message.from_user.id)  # Adding the user to the served_user list in the database
    if len(message.text.split()) > 1:  # Checking if any arguments are passed with the start command
        name = message.text.split(None, 1)[1]  # Extracting the argument
        if name.startswith("help"):  # If the argument starts with "help"
            keyboard = help_pannel(_)  # Creating the help panel
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )  # Replying with the start image, help message and help panel
        if name.startswith("sud"):  # If the argument starts with "sud"
            await sudoers_list(_, message)  # Calling the sudoers_list function
            if await is_on_off(2):  # If the logging is turned on
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} just started the bot to check <b>sudolist</b>.\n\n<b>USER ID :</b> <code>{message.from_user.id}</code>\n<b>USERNAME :</b> @{message.from_user.username}",
                )  # Logging the event in the logger chat
            return
        if name.startswith("inf"):  # If the argument starts with "inf"
            m = await message.reply_text("🔎")  # Replying with a loading message
            query = name.replace("info_", "", 1)  # Extracting the query from the argument
            query = f"https://www.youtube.com/watch?v={query}"  # Formatting the query to youtube video link
            results = VideosSearch(query, limit=1)  # Searching the youtube for the query
            result = await results.next()  # Getting the first result
            title = result["title"]  # Extracting the title of the video
            duration = result["duration"]  # Extracting the duration of the video
            views = result["viewCount"]["short"]  # Extracting the views of the video
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]  # Extracting the thumbnail of the video
            channellink = result["channel"]["link"]  # Extracting the channel link of the video
            channel = result["channel"]["name"]  # Extracting the channel name of the video
            link = result["link"]  # Extracting the link of the video
            published = result["publishedTime"]  # Extracting the published time of the video
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )  # Formatting the searched text message
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )  # Creating the inline keyboard with two buttons, one to open the video and another to open the support chat
            await m.delete()  # Deleting the loading message
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )  # Replying with the searched video thumbnail, searched text and inline keyboard
            if await is_on_off(2):  # If the logging is turned on
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} just started the bot to check <b>track information</b>.\n\n<b>USER ID :</b> <code>{message.from_user.id}</code>\n<b>USERNAME :</b> @
