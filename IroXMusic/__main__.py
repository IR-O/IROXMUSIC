import asyncio
import importlib
import sys
import os

import aioschedule as schedule
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from IroXMusic import LOGGER, app, userbot, client
from IroXMusic.core.call import Irop
from IroXMusic.misc import sudo
from IroXMusic.plugins import ALL_MODULES
from IroXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def import_modules():
    LOADING_MODULES = []
    for module in ALL_MODULES:
        try:
            importlib.import_module(f"IroXMusic.plugins{module}")
            LOADING_MODULES.append(f"{module} - Successfully Imported")
        except Exception as e:
            LOADING_MODULES.append(f"{module} - Failed to Import: {e}")
    return "\n".join(LOADING_MODULES)

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).error(f"Error while getting banned users: {e}")
    await app.start()
    await userbot.start()
    await Irop.start()
    try:
        await Irop.stream_call("https://te.legra.ph/file/ab9f1bb095596c10b7ff8.mp4")
    except NoActiveGroupCall:
        LOGGER("IroXMusic").error(
            "Please turn on the videochat of your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except Exception as e:
        LOGGER("IroXMusic").error(f"Error while streaming call: {e}")
    await import_modules()
    LOGGER("IroXMusic.plugins").info("Successfully Imported Modules...")
    schedule.every(10).seconds.do(Irop.decorators)
    LOGGER("IroXMusic").info("Running Irop.decorators every 10 seconds...")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("IroXMusic").info("Stopping IroX Music Bot...")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(init())
    except
