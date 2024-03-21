from pyrogram import filters, StopPropagation
from pyrogram.types import Message
import asyncio

from IroXMusic import app
from IroXMusic.core.call import Irop

@app.on_message(filters.video_chat_started | filters.video_chat_ended)
async def handle_video_chat(client, message: Message):
    if not message.from_user.is_administrator:
        return
    
    try:
        await asyncio.sleep(1)
        await Irop.stop_stream_force(message.chat.id)
    except StopPropagation:
        pass
    except Exception as e:
        await message.reply(f"Error stopping stream: {e}")
    
    await message.reply("Video chat {} ended. Streaming stopped.".format("started" if message.video_chat_started else "ended"))
