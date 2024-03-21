# Import necessary modules
import asyncio  # Asynchronous programming library
import speedtest  # Module for internet speed testing
from pyrogram import filters, Client as TelegramClient  # Pyrogram library for creating a Telegram bot
from pyrogram.types import Message  # Message object for handling Telegram messages

# Import custom modules
from config import SUDOERS, LOVE  # Import SUDOERS and LOVE constants from config.py
from utils.decorators.language import language  # Import language decorator for handling multiple languages

# Function for handling internet speed testing
@language  # Decorator to handle multiple languages
async def internet_speed_test(client: TelegramClient, message: Message):
    st = speedtest.Speedtest()  # Initialize a new Speedtest object
    st.get_servers()  # Get a list of speedtest servers
    st.download()  # Start the download test
    st.upload()  # Start the upload test
    result = st.results.dict()  # Get the results

    # Prepare the response message
    response = f"Download: {result['download'] / 1000000:.2f} Mbps\n"
    response += f"Upload: {result['upload'] / 1000000:.2f} Mbps\n"
    response += f"Ping: {result['ping']:.2f} ms"

    await message.reply(response)  # Send the response message

# Event handler for the /start command
@client.on_message(filters.command("start"))
async def start_command_handler(client: TelegramClient, message: Message):
    await message.reply("Hello, this is a speedtest bot!")

# Event handler for the /speedtest command
@client.on_message(filters.command("speedtest"))
async def speedtest_command_handler(client: TelegramClient, message: Message):
    await internet_speed_test(client, message)

# Run the bot
if __name__ == "__main__":
    # Initialize the bot with your API ID and hash
    app = TelegramClient("your_bot_api_id", "your_bot_hash")

    # Start the bot
    app.run()
