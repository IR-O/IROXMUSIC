from pyrogram import Client, errors, types  # Importing necessary modules
from pyrogram.enums import ChatMemberStatus, ParseMode  # Importing necessary enums

import config  # Importing config module

from ..logging import LOGGER  # Importing custom logging module

class Irop(Client):
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
        try:
            await super().start()  # Starting the Client

            # Getting the bot's details
            self.id = self.me.id
            self.name = self.me.first_name + " " + (self.me.last_name or "")
            self.username = self.me.username
            self.mention = self.me.mention

            # Sending a message to the log channel
            try:
                # Sending a formatted message to the log channel
                await self.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
                )
            except (errors.ChannelInvalid, errors.PeerIdInvalid):
                LOGGER(__name__).error(
                    "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
                )  # Logging the error if the bot fails to access the log channel

        except Exception as e:
            LOGGER(__name__).error(f"Failed to start bot: {e}")  # Logging the error if starting the Client fails
        finally:
            if self.username is not None:
                LOGGER(__name__).info(f"Bot username: @{self.username}")
