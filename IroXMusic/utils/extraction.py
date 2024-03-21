# Importing necessary modules and classes
from pyrogram.enums import MessageEntityType  # Importing the MessageEntityType enum from the pyrogram library
from pyrogram.types import Message, User  # Importing the Message and User classes from the pyrogram library

# Importing the app instance from the IroXMusic module
from IroXMusic import app

# Using the imported classes and enums
def handle_message(message: Message):
    # Printing the message text and the type of any message entities
    print(f"Message text: {message.text}")
    for entity in message.entities:
        print(f"Entity type: {MessageEntityType(entity.type).name}")

    # Printing the user's username, if available
    user = message.from_user
    if user.username:
        print(f"User username: @{user.username}")

# Listening for new messages
@app.on_message()
def listen_for_messages(client, message: Message):
    handle_message(message)

# Running the app
if __name__ == "__main__":
    app.run()
