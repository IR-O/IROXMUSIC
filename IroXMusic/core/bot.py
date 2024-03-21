from pyrogram import Client, errors, types  # Importing necessary modules
from pyrogram.enums import ChatMemberStatus, ParseMode  # Importing necessary enums

import config  # Importing config module

from ..logging import LOGGER  # Importing custom logging module

class Irop(Client):
    """
    Custom Pyrogram Client for IroXMusic bot.
    """

    def __init__(self):
        # Logging that the bot is starting
        LOGGER(__name__).info(f"Starting Bot...")

        # Checking if the required configurations are set
        if not config.BOT_TOKEN:
            LOGGER(__name__).error("Bot token is empty.")
            exit()
        if not isinstance(config.LOGGER_ID, int) or config.LOGGER_ID <= 0:
            LOGGER(__name__).error("Invalid logger ID.")
            exit()
        if not config.API_ID or not config.API_HASH:
            LOGGER(__name__).error("API ID or hash is empty.")
            exit()

        # Initializing the Client with required configurations
        super().__init__(
            name="IroXMusic",  # Friendly name for the Client
            api_id=config.API_ID,  # Telegram API ID
            api_hash=config.API_HASH,  # Telegram API Hash
            bot_token=config.BOT_TOKEN,  # Bot token
            in_memory=True,  # Running the Client in-memory
            parse_mode=ParseMode.HTML,  # Setting parse mode to HTML
            max_concurrent_transmissions=7,  # Maximum number of simultaneous transmissions
        )

    async def start(self):
        """
        Starting the bot and logging in.
        """
        try:
            await super().start()  # Starting the Client

            # Getting the bot's details
            self.id = self.me.id
            self.name = self.me.first_name + " " + (self.me.last_name or "")
            self.username = self.me.username
            self.mention = self.me.mention

            # Checking if the bot is an admin in the chat
            try:
                chat_member = await self.get_chat_member(config.LOGGER_ID, self.id)
                if chat_member.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
                        "Bot is not an admin in the log channel."
                    )  # Logging the error if the bot is not an admin
            except errors.UserNotParticipant:
                LOGGER(__name__).error(
                    "Bot has not been added to the log group/channel."
                )  # Logging the error if the bot is not a member of the log channel

            # Checking if the bot can send messages in the chat
            try:
                await self.send_message(
                    chat_id=config.LOGGER_ID, text="Test message"
                )
                await self.delete_messages(
                    chat_id=config.LOGGER_ID, message_ids=self.last_message_id
                )
            except errors.ChatAdminRequired:
                LOGGER(__name__).error(
                    "Bot is not an admin in the log group/channel."
                )  # Logging the error if the bot is not an admin
            except errors.ChatSendMessageForbidden:
                LOGGER(__name__).error(
                    "Bot does not have permission to send messages in the log group/channel."
                )  # Logging the error if the bot does not have permission to send messages

            # Sending a formatted message to the log channel
            try:
                # Sending a formatted message to the log channel
                await self.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀ��
