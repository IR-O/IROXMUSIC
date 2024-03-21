from pyrogram import filters, StopPropagation
from pyrogram.types import Message

from IroXMusic import app
from IroXMusic.core.call import Irop

@app.on_message(filters.video_chat_started | filters.video_chat_ended)
async def handle\_video\_chat(client, message: Message):
try:
await Irop.stop\_stream\_force(message.chat.id)
except StopPropagation:
pass
if message.video\_chat\_started:
await message.reply("Video chat started. Streaming stopped.")
else:
await message.reply("Video chat ended. Streaming stopped.")
