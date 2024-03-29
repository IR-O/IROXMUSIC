from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# IroXMusic imports
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

# config imports
from config import SUPPORT_CHAT, adminlist, confirmer
from strings import get_string

# Helper function to convert integer to alphabets
async def int_to_alpha(user_id: int) -> str:
    return "".join(chr(int(user_id // (10 ** i)) % 10 + 48) for i in range(7, 0, -1))

def AdminRightsCheck(func):
    """
    Decorator function to check for admin rights.
    This function checks if the bot is in maintenance mode, if the message is from a sender chat, if the chat is active, and if the chat is not a non-admin chat.
    If all checks pass, it checks if the user is a sudo user and if skipmode is enabled.
    If skipmode is enabled, it calculates the number of votes needed for the action and creates an inline keyboard with a vote button.
    """
    async def wrapper(client, message):
        try:
            # Check if maintenance mode is enabled
            if not await is_maintenance():
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
                                callback_data="anonymous_admin",
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
                if message.from_user.id not in SUDOERS:
                    # Check if skipmode is enabled
                    if await is_skipmode(message.chat.id):
                        # Get the upvote count
                        upvote = await get_upvote_count(message.chat.id)
                        # Calculate the number of votes needed for the action
                        text = f"<b>admin rights needed</b>\n\nrefresh admin cache via : /reload\n\n» {upvote} votes needed for performing this action."

                        command = message.command[0]
                        if command[0] == "c":
                            command = command[1:]
                        if command == "speed":
                            return await message.reply_text(_["admin_14"])
                        mode = command.title()
                        # Create an inline keyboard with a vote button
                        upl = InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="vote",
                                        callback_data=f"admin upvote|{message.chat.id}_{mode}",
                                    ),
                                ]
                            ]
                        )
                        # Store the video and file information in the confirmer dictionary
                        confirmer[message.chat.id] = {
                            "video": message.video,
                            "file": message.document,
                            "text": text,
                            "mode": mode,
                        }
                        return await message.reply_text(
                            text=text,
                            reply_markup=upl,
                            disable_web_page_preview=True,
                        )

        except Exception as e:
            LOGGER.error(e)
            return
