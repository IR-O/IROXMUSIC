import asyncio
from typing import List, Dict

import pyrogram
from pyrogram.handlers import MessageHandler
from pyrogram.filters import FilterNone
from pyrogram.types import Message

class Client(App):
    def __init__(self):
        super().__init__("my_account")
        self.message_handlers = []

    async def start(self):
        await super().start()
        for handler in self.message_handlers:
            self.add_handler(handler)
        await self.idle()

    def add_message_handler(self, handler: MessageHandler):
        self.message_handlers.append(handler)

if __name__ == "__main__":
    app = Client()

    @app.on_message(FilterNone)
    async def handle_message(client: App, message: Message):
        print(f"Received message: {message.text}")

    app.add_message_handler(handle_message)

    app.run()
