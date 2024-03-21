from pyrogram import filters # Importing filters from pyrogram library
from pyrogram.types import Message # Importing Message from pyrogram.types

from IroXMusic import app # Importing app from IroXMusic
from IroXMusic.core.call import Irop # Importing Irop from IroXMusic.core.call
from IroXMusic.misc import SUDOERS, db # Importing SUDOERS and db from IroXMusic.misc
from IroXMusic.utils import AdminRightsCheck # Importing AdminRightsCheck from IroXMusic.utils
from IroXMusic.utils.database import is_active_chat, is_nonadmin_chat # Importing is_active_chat and is_nonadmin_chat from IroXMusic.utils.database
from IroXMusic.utils.decorators.language import languageCB # Importing languageCB from IroXMusic.utils.decorators.language
from IroXMusic.utils.inline import close_markup, speed_markup # Importing close_markup and speed_markup from IroXMusic.utils.inline
from config import BANNED_USERS, adminlist # Importing BANNED_USERS and adminlist from config

checker = [] # Initializing an empty list called checker


@app.on_message( # Decorator to listen for incoming messages
    filters.command(["cspeed", "speed", "cslow", "slow", "playback", "cplayback"]) # Checking for specific commands
    & filters.group # Checking if the message is in a group
    & ~BANNED_USERS # Checking if the user is not in the BANNED_USERS list
)
@AdminRightsCheck # Decorator to check for admin rights
async def playback(cli, message: Message, _, chat_id): # Defining the function playback
    playing = db.get(chat_id) # Getting the playing status from the database
    if not playing: # If there is no playing status
        return await message.reply_text(_["queue_2"]) # Reply with a message
    duration_seconds = int(playing[0]["seconds"]) # Getting the duration of the playing status
    if duration_seconds == 0: # If the duration is 0
        return await message.reply_text(_["admin_27"]) # Reply with a message
    file_path = playing[0]["file"] # Getting the file path of the playing status
    if "downloads" not in file_path: # If the file path does not contain "downloads"
        return await message.reply_text(_["admin_27"]) # Reply with a message
    upl = speed_markup(_, chat_id) # Getting the speed markup
    return await message.reply_text(
        text=_["admin_28"].format(app.mention), # Replying with a message and mentioning the app
        reply_markup=upl, # Adding the speed markup to the reply
    )


@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS) # Decorator to listen for incoming callback queries
@languageCB # Decorator to handle language changes
async def del_back_playlist(client, CallbackQuery, _): # Defining the function del_back_playlist
    callback_data = CallbackQuery.data.strip() # Getting the callback data
    callback_request = callback_data.split(None, 1)[1] # Splitting the callback data
    chat, speed = callback_request.split("|") # Splitting the callback request
    chat_id = int(chat) # Converting the chat to an integer
    if not await is_active_chat(chat_id): # Checking if the chat is active
        return await CallbackQuery.answer(_["general_5"], show_alert=True) # Answering the callback query with a message and showing an alert
    is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id) # Checking if the chat is not admin
    if not is_non_admin: # If the chat is not non-admin
        if CallbackQuery.from_user.id not in SUDOERS: # Checking if the user is not in the SUDOERS list
            admins = adminlist.get(CallbackQuery.message.chat.id) # Getting the admins from the adminlist
            if not admins: # If there are no admins
                return await CallbackQuery.answer(_["admin_13"], show_alert=True) # Answering the callback query with a message and showing an alert
            else: # If there are admins
                if CallbackQuery.from_user.id not in admins: # Checking if the user is not in the admins list
                    return await CallbackQuery.answer(_["admin_14"], show_alert=True) # Answering the callback query with a message and showing an alert
    playing = db.get(chat_id) # Getting the playing status from the database
    if not playing: # If there is no playing status
        return await CallbackQuery.answer(_["queue_2"], show_alert=True) # Answering the callback query with a message and showing an alert
    duration_seconds = int(playing[0]["seconds"]) # Getting the duration of the playing status
    if duration_seconds == 0: # If the duration is 0
        return await CallbackQuery.answer(_["admin_27"], show_alert=True) # Answering the callback query with a message and showing an alert
    file_path = playing[0]["file"] # Getting the file path of the playing status
    if "downloads" not in file_path: # If the file path does not contain "downloads"
        return await CallbackQuery.answer(_["admin_27"], show_alert=True) # Answering the callback query with a message and showing an alert
    checkspeed = (playing[0]).get("speed") # Getting the speed from the playing status
    if checkspeed: # If there is a speed
        if str(checkspeed) == str(speed): # If the speed is the same as the selected speed
            if str(speed) == str("1.0"): # If the speed is 
