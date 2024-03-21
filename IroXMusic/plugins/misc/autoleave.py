import asyncio  # for running multiple coroutines concurrently
from datetime import datetime  # for handling date and time

from pyrogram.enums import ChatType  # for handling different types of chats

import config  # for importing configuration settings
from IroXMusic import app  # for importing the Pyrogram bot instance
from IroXMusic.core.call import Irop, autoend  # for handling music playback and autoend functionality
from IroXMusic.utils.database import get_client  # for handling database connections

# A coroutine that automatically leaves inactive chats
async def auto_leave():
    if not config.AUTO_LEAVING_ASSISTANT:
        return

    while True:
        try:
            async with get_client(config.ASSISTANT_USER_ID) as client:  # create a database connection and get the client instance
                async for dialog in client.get_dialogs():  # iterate over all dialogs
                    if dialog.chat.type in [  # check if the dialog is a group, supergroup, or channel
                        ChatType.SUPERGROUP,
                
