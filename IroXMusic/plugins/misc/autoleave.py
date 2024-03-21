import asyncio
from datetime import datetime
from pyrogram.enums import ChatType

import config
from IroXMusic import app
from IroXMusic.core.call import Irop, autoend
from IroXMusic.utils.database import get_client

async def auto_leave():
    if not config.AUTO_LEAVING_ASSISTANT:
        return

    while True:
        try:
            async with get_client(config.ASSISTANT_USER_ID) as client:
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in (
                        ChatType.GROUP,
                        ChatType.SUPERGROUP,
                        ChatType.CHANNEL,
                    ):
                        # calculate the time difference between the current time and the last message time
                        time_diff = datetime.now() - dialog.message.date
                        # check if the time difference is greater than the allowed idle time
                        if time_diff.total_seconds() > config.MAX_IDLE_TIME:
                            # leave the chat if the time difference is greater than the allowed idle time
                            await app.leave_chat(dialog.chat.id)
                            print(f"Left chat {dialog.chat.id} after being idle for {config.MAX_IDLE_TIME} seconds.")
                        else:
                            # print a message if the bot is still active in the chat
                            print(f"Active in chat {dialog.chat.id}.")
        except Exception as e:
            print(f"Error in auto_leave: {e}")

async def main():
    await auto_leave()

if __name__ == "__main__":
    asyncio.run(main())
