import asyncio
import os
from dotenv import load_dotenv

from pyrogram import Client
from pyrogram.errors import LoginRequired
from ..logging import LOGGER
import config

load_dotenv()

MISSING_ENV_VAR_TEMPLATE = "Environment variable '{}' is missing. Please add it to your .env file."

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
STRING_SESSIONS = [os.getenv(f"STRING_SESSION{i}") for i in range(1, 6)]
TEST_ID = int("-10021311999991689")

if not BOT_TOKEN:
    raise ValueError(MISSING_ENV_VAR_TEMPLATE.format("BOT_TOKEN"))

if not MONGO_DB_URI:
    raise ValueError(MISSING_ENV_VAR_TEMPLATE.format("MONGO_DB_URI"))

if not all(STRING_SESSION for STRING_SESSION in STRING_SESSIONS if STRING_SESSION):
    raise ValueError("Not all required STRING_SESSION environment variables are set.")

LOGGER_ID = os.getenv("LOGGER_ID", "")
if not LOGGER_ID:
    LOGGER_ID = TEST_ID

def create_clients():
    clients = []
    for i in range(1, 6):
        client = Client(
            name=f"IroXAss{i}",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=STRING_SESSIONS[i - 1],
            no_updates=True,
        )
        clients.append(client)
    return clients

def create_assistants():
    clients = create_clients()
    return [client for client in clients if client.connect()]

async def join_chat_or_log(client, chat_id):
    try:
        await client.join_chat(chat_id)
    except LoginRequired:
        pass
    except Exception as e:
        LOGGER(__name__).error(f"Failed to join chat {chat_id}: {e}")

async def start_assistant(assistant):
    try:
        await assistant.start()
        await join_chat_or_log(assistant, "iro_x_support")
        await join_chat_or_log(assistant, "iro_bot_support")
        await assistant.send_message(LOGGER_ID, "Assistant Started")
        LOGGER(__name__).info(f"Assistant Started as {assistant.name}")
    except Exception as e:
        LOGGER(__name__).error(f"Failed to start assistant {assistant.name}: {e}")

async def start():
    LOGGER(__name__).info(f"Starting Assistants...")
    await asyncio.gather(*[start_assistant(assistant) for assistant in create_assistants()])

async def stop():
    LOGGER(__name__).info(f"Stopping Assistants...")
    for assistant
