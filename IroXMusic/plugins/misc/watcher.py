import asyncio
import logging

from pyrogram import filters, StopPropagation
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import Message

import logging
import sys
import traceback

from IroXMusic import app
from IroXMusic.core.call import Irop

@app.on_message(filters.video_chat_started | filters.video_chat_ended)
async def handle_video_chat(client, message: Message):
    if not message.from_user.is_administrator:
        return

    if message.chat.type == "private" or not message.mentions or (message.forward_from and message.forward_from.is_bot):
        return

    try:
        await asyncio.sleep(1)
        await Irop.stop_stream_force(message.chat.id)
    except StopPropagation:
        pass
    except ChatAdminRequired:
        await message.reply("I need admin permissions to stop the stream.")
    except Exception as e:
        logging.error(f"Error stopping stream: {e}")
        await message.reply(f"Error stopping stream: {e}", mention_via=message.from_user.id)

    chat_status = "started" if message.video_chat_started else "ended"
    await message.reply(f"Video chat {chat_status} ended. Streaming stopped.", mention_via=message.from_user.id)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    try:
        app.run()
    except Exception:
        traceback.print_exc(file=sys.stdout)
        logging.error("Exiting...")
        sys.exit(1)
