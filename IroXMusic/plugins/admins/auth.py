import asyncio
from typing import List, Dict

import pyrogram
from pyrogram.handlers import MessageHandler
from pyrogram.filters import FilterNone
from pyrogram.types import Message

class Client(pyrogram.Client):
    def __init__(self):
        super().__init__("my_account")
        # Initialize a list to store message handlers
        self.message_handlers = []

    async def start(self):
        # Start the client and connect to the Telegram API
        await super().start()
        # Add all message handlers to the client
        for handler in self.message_handlers:
            self.add_handler(handler)
        # Wait until the client is done processing messages
        await self.idle()

    def add_message_handler(self, handler: MessageHandler):
        # Add a message handler to the list of handlers
        self.message_handlers.append(handler)

if __name__ == "__main__":
    # Create a new instance of the Client class
    app = Client()

    # Define a message handler function
    async def handle_message(client: pyrogram.Client, message: Message):
        # Print the text of the received message
        print(f"Received message: {message.text}")

    # Add the message handler to the client
    app.add_message_handler(handle_message)

    # Start the client's event loop
    app.run()
