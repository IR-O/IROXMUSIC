import asyncio
import os
import shutil
import socket
import logging
import pathlib
from datetime import datetime
import aiohttp
import git
from typing import List

import config
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import HAPP
import SUDOERS
import XCB
import LOVE
from IroXMusic import app
from IroXMusic.misc import HAPP, SUDOERS, XCB, LOVE
from IroXMusic.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from IroXMusic.utils.decorators.language import language
from IroXMusic.utils.pastebin import IropBin

# This line disables the InsecureRequestWarning from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)  # Initialize the logger


async def is_heroku() -> bool:
    """
    A function to check if the code is running on Heroku.
    Returns a boolean value.
    """
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS & LOVE)
@language
async def log_(client, message, _):
    """
    A function to send the log.txt file as a document when the /getlog, /logs, or /getlogs command is used by a SUDOER.
    """
    try:
        await message.reply_document(document="log.txt")
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await message.reply_text(_["server_1"])
    except Exception as e:
        logger.exception(e)
        await message.reply_text(_["server_1"])


@app.on_message(filters.command(["update", "gitpull"]) & SUDOERS & LOVE)
@language
async def update_(client, message, _):
    """
    A function to update the bot's code when the /update or /gitpull command is used by a SUDOER.
    """
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])
    response = await message.reply_text(_["server_3"])
    try:
        repo = git.Repo()  # Initialize the Git repository object
    except git.exc.GitCommandError:
        return await response.edit(_["server_4"])
    except git.exc.InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    await asyncio.gather(
        asyncio.create_task(run_command(to_exc)),
        asyncio.sleep(7),
    )
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(_["server_6"])
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: <a href={REPO_}/commit/{info}>{info.summary}</a> ʙʏ -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴛᴇᴅ ᴏɴ :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ\n\n<b><u>ᴜᴩᴅᴀᴛᴇs:</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await IropBin(updates)
        nrs = await response.edit(
            f"<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜ
