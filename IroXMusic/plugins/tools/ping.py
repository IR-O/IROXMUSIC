from datetime import datetime # Importing datetime module to get current time
from typing import Union # Importing Union from typing module

from pyrogram import filters # Importing filters from pyrogram module
from pyrogram.errors import Photo size is too large # Importing specific error from pyrogram module
from pyrogram.types import Message # Importing Message from pyrogram module

from IroXMusic import app # Importing app from IroXMusic module
from IroXMusic.core.call import Irop # Importing Irop from IroXMusic.core.call module
from IroXMusic.utils import bot_sys_stats # Importing bot_sys_stats from IroXMusic.utils module
from IroXMusic.utils.decorators.language import language # Importing language from IroXMusic.utils.decorators.language module
from IroXMusic.utils.inline import supp_markup # Importing supp_markup from IroXMusic.utils.inline module
from config import BANNED_USERS # Importing BANNED_USERS from config module
from config import PING_IMG_URL # Importing PING_IMG_URL from config module


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS) # Decorator to listen for /ping and /alive commands from users not in BANNED_USERS list
@language # Decorator to handle language-specific translations
async def ping_com(client, message: Message, _): # Defining the asynchronous function ping_com with client, message and _ as parameters
    if not message.text: # Checking if message text is empty
        return # Returning if message text is empty
    try:
        start = datetime.now() # Getting current time before sending photo
        response = await message.reply_photo( # Replying to the message with a photo
            photo=PING_IMG_URL, # Using PING_IMG_URL as the photo
            caption=_["ping_1"].format(app.mention), # Adding caption to the photo using
