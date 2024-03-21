from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# IroXMusic import statements
from IroXMusic import app, LOGGER
from IroXMusic.misc import SUDOERS, db
from IroXMusic.utils.database import (
    get_authuser_names,
    get_cmode,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_maintenance,
    is_nonadmin_chat,
    is_skipmode,
)

# config import statements
from config import SUPPORT_CHAT, adminlist, confirmer
from strings import get_string

# Helper function to convert integer to alphabets
async def int_to_alpha(user_id: int) -> str:
    return "".join(chr(int(user_id // (10 ** i)) % 10 + 48) for i in range(7, 0, -1))

def AdminRightsCheck(mystic):
    """
    Decorator function to check for admin rights.
    """
    async def wrapper(client, message):
        try:
            # Check if maintenance mode is enabled
            if not await is_maintenance():
                # If not a sudo user, reply with maintenance message
                if message.from_user.id not in SUDOERS:
                    return await message.reply_text(
                        text=f"{app.mention} is under maintenance. Visit <a href={SUPPORT_CHAT}>support chat</a> for knowing the reason.",
                        disable_web_page_preview=True,
                    )

            # Delete the original message
            try:
                await message.delete()
            except:
                pass

            # Get the language for the chat
            try:
                language = await get_lang(message.chat.id)
                _ = get_string(language)
            except:
                _ = get_string("en")

            # Check if the message is from a sender chat
            if message.sender_chat:
                upl = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="how to fix ?",
                                callback_data="AnonymousAdmin",
                            ),
                        ]
                    ]
                )
                return await message.reply_text(_["general_3"], reply_markup=upl)

            # Check if the chat is active
            if not await is_active_chat(message.chat.id):
                return await message.reply_text(_["general_5"])

            # Check if the chat is not a non-admin chat
            is_non_admin = await is_nonadmin_chat(message.chat.id)
            if not is_non_admin:
                # Check if the user is a sudo user
                if message.from_user.id not in SUDOERS:
                    # Check if skipmode is enabled
                    if await is_skipmode(message.chat.id):
                        # Get the upvote count
                        upvote = await get_upvote_count(message.chat.id)
                        # Calculate the number of votes needed for the action
                        text = f"""<b>admin rights needed</b>

refresh admin cache via : /reload

» {upvote} votes needed for performing this action."""

                        command = message.command[0]
                        if command[0] == "c":
                            command = command[1:]
                        if command == "speed":
                            # If the command is "speed", return an error message
                            return await message.reply_text(_["admin_14"])
                        MODE = command.title()
                        # Create an inline keyboard with a vote button
                        upl = InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="vote",
                                        callback_data=f"ADMIN UpVote|{message.chat.id}_{MODE}",
                                    ),
                                ]
                            ]
                        )
                        # Store the video and file information in the confir
