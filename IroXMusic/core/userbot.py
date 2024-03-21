from pyrogram import Client
from os import getenv
from dotenv import load_dotenv
from ..logging import LOGGER
import config

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSIONS = [getenv(f"STRING_SESSION{i}") for i in range(1, 6)]
TEST_ID = int("-10021311999991689")
LOGGER_ID = getenv("LOGGER_ID", "")

# Function to create assistant instances
def create_assistants():
    assistants = []
    for i in range(1, 6):
        if STRING_SESSIONS[i - 1]:
            assistant = Client(
                name=f"IroXAss{i}",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                session_string=STRING_SESSIONS[i - 1],
                no_updates=True,
            )
            assistants.append(assistant)
    return assistants

# Function to join a chat or log an error if joining fails
def join_chat_or_log(client, chat_id):
    try:
        client.join_chat(chat_id)
    except Exception as e:
        LOGGER(__name__).error(f"Failed to join chat {chat_id}: {e}")

# Async function to start an assistant
async def start_assistant(assistant):
    try:
        await assistant.start()
        join_chat_or_log(assistant, "iro_x_support")
        join_chat_or_log(assistant, "iro_bot_support")
        await assistant.send_message(LOGGER_ID, "Assistant Started")
        LOGGER(__name__).info(f"Assistant Started as {assistant.name}")
    except Exception as e:
        LOGGER(__name__).error(f"Failed to start assistant {assistant.name}: {e}")

# Async function to start all assistants
async def start():
    LOGGER(__name__).info(f"Starting Assistants...")
    await asyncio.gather(*[start_assistant(assistant) for assistant in create_assistants()])

# Async function to stop all assistants
async def stop():
    LOGGER(__name__).info(f"Stopping Assistants...")
    for assistant in create_assistants():
        try:
            await assistant.stop()
        except:
            pass
