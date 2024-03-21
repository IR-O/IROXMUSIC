import time
import asyncio
from typing import List, Union

import aioschedule as schedule
import pyrogram
from pyrogram import filters, StopPropagation
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, ChatBannedRightsError, UserBannedInChannel, RPCError
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython import VideosSearch

import config
from IroXMusic import app, LOGGER, SUDO_USERS
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
async def start_pm(_, message: Message) -> None:
    try:
        await add_served_user(message.from_user.id)
        if len(message.text.split()) > 1:
            name = message.text.split(None, 1)[1]
            if name.startswith("help"):
                keyboard = help_pannel(_)
                return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["help_1"].format(config.SUPPORT_CHAT),
                    reply_markup=keyboard,
                )
            if name.startswith("sud"):
                await sudoers_list(_, message)
                if await is_on_off(2):
                    await app.send_message(
                        chat_id=config.LOGGER_ID,
                        text=f"{message.from_user.mention} just started the bot to check <b>sudolist</b>.\n\n<b>USER ID :</b> <code>{message.from_user.id}</code>\n<b>USERNAME :</b> @{message.from_user.username}",
                    )
                return
            if name.startswith("inf"):
                m = await message.reply_text("🔎")
                query = name.replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                result = await results.next()
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
                searched_text = _["start_6"].format(
                    title, duration, views, published, channellink, channel, app.mention
                )
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text=_["S_B_8"], url=link),
                            InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                        ],
                    ]
                )
                await m.delete()
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                )
                if await is_on_off(2):
                    await app.send_message(
                        chat_id=config.LOGGER_ID,
                        text=f"{message.from_user.mention} just started the bot to check <b>track information</b>.\n\n<b>USER ID :</b> <code>{message.from_user.id}</code>\n<b>USERNAME :</b> @{message.from_user.username}",
                    )
        else:
            await start_panel(_, message)
    except UserBannedInChannel as err:
        await message.reply_text(f"Error: {str(err)}")
    except ChatBannedRightsError as err:
        await message.reply_text(f"Error: {str(err)}")
    except ChatAdminRequired as err:
        await message.reply_text(f"Error: {str(err)}")
    except RPCError as err:
        await message.reply_text(f"Error: {str(err)}")
    except Exception as err:
        LOGGER.exception(err)
        await message.reply_text("An error occurred, please try again later.")
        raise StopPropagation
