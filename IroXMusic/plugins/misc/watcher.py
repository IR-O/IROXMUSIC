from pyrogram import filters, StopPropagation  # Importing required modules
from pyrogram.types import Message
import asyncio

from IroXMusic import app  # Importing app instance
from IroXMusic.core.call import Irop  # Importing Irop instance from core.call module

@app.on_message(filters.video_chat_started | filters.video_chat_ended)  # Event listener for video_chat_started and video_chat_ended events
async def handle_video_chat(client, message: Message):
    if not message.from_user.is_administrator:  # Check if the user is an administrator
        return  # If not, return and do nothing
    
    try:
        await asyncio.sleep(1)  # Wait for 1 second before stopping the stream
        await Irop.stop_stream_force(message.chat.id)  # Stop the stream forcefully
    except StopPropagation:
        pass  # If StopPropagation is raised, do nothing
    except Exception as e:
        await message.reply(f"Error stopping stream: {e}")  # If any other exception occurs, reply with the error message
    
    chat_status = "started" if message.video_chat_started else "ended"  # Determine the chat status
    await message.reply("Video chat {} ended. Streaming stopped.".format(chat_status))  # Reply with the appropriate message
