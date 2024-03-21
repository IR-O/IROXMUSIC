import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from IroXMusic import app
from IroXMusic.core.call import Irop, autoend
from IroXMusic.utils.database import get_client, is_active_chat, is_autoend

async def auto_leave():
    if not config.AUTO_LEAVING_ASSISTANT:
        return

    while True:
        try:
            async with get_client(config.ASSISTANT_USER_ID) as client:
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in [
                        ChatType.SUPERGROUP,
                        ChatType.GROUP,
                        ChatType.CHANNEL,
                    ]:
                        if dialog.chat.id not in [
                            config.LOGGER_ID,
                            -1001653694038,
                            -1001698464500,
                        ]:
                            if not await is_active_chat(dialog.chat.id):
                                try:
                                    await client.leave_chat(dialog.chat.id)
                                except:
                                    pass
        except:
            await asyncio.sleep(10)

        await asyncio.sleep(900)

async def auto_end():
    if not await is_autoend():
        return

    while True:
        try:
            for chat_id, timer in autoend.items():
                if not timer:
                    continue

                if datetime.now() > timer:
                    if not await is_active_chat(chat_id):
                        del autoend[chat_id]
                        continue

                    try:
                        await Irop.stop_stream(chat_id)
                    except:
                        pass

                    try:
                        await app.send_message(
                            chat_id,
                            "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
                        )
                    except:
                        pass

                    del autoend[chat_id]

        except:
            await asyncio.sleep(10)

        await asyncio.sleep(5)

async def main():
    await asyncio.gather(
        auto_leave(),
        auto_end()
    )

if __name__ == "__main__":
    asyncio.run(main())
