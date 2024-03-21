from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER

class Irop(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        if not config.BOT_TOKEN:
            LOGGER(__name__).error("Bot token is empty.")
            exit()
        if not isinstance(config.LOGGER_ID, int) or config.LOGGER_ID <= 0:
            LOGGER(__name__).error("Invalid logger ID.")
            exit()
        if not config.API_ID or not config.API_HASH:
            LOGGER(__name__).error("API ID or hash is empty.")
            exit()
        super().__init__(
            name="IroXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        try:
            await super().start()
        except Exception as e:
            LOGGER(__name__).error(f"Failed to start bot: {e}")
            exit()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        try:
            self.username = self.me.username
        except Exception:
            self.username = None
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )

