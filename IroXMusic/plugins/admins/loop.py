from pyrogram import filters
from pyrogram.types import Message
from typing import Optional

from IroXMusic import app
from IroXMusic.utils.database import get_loop as get_loop_db, set_loop as set_loop_db
from IroXMusic.utils.decorators import AdminRightsCheck
from IroXMusic.utils.inline import close_markup
from config import BANNED_USERS
from config import get_string as _

@app.on_message(filters.command(["loop", "cloop"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def admins(cli, message: Message, _: Optional[str] = None, chat_id: int = None):
    """
    This function handles messages that contain the "loop" or "cloop" command in a group chat, as long as the user is not banned.
    It also checks if the user has admin rights.

    Args:
        cli: The Pyrogram client object.
        message: The Message object that triggered the function.
        _: An optional string that is not used in this function.
        chat_id: The ID of the chat where the message was sent.

    Returns:
        None
    """
    if chat_id is None:
        # If the chat ID is None, return without doing anything.
        return

    # Get the usage message for the "loop" command.
    usage = _["admin_17"]

    # Check if the message contains exactly two parts: the command and the argument.
    if len(message.command) != 2:
        # If not, reply with the usage message.
        return await message.reply_text(usage)

    # Get the argument from the message.
    state = message.text.split(None, 1)[1].strip()

    try:
        # Try to convert the argument to an integer.
        if state.isnumeric():
            # If it can be converted to an integer, check if it's between 1 and 10.
            state = int(state)
            if 1 <= state <= 10:
                # If it is, get the current loop state from the database.
                got = await get_loop_db(chat_id)
                if got is not None:
                    # If the loop state exists in the database, add the new state to it.
                    state = got + state
                if int(state) > 10:
                    # If the new state is greater than 10, set it to 10.
                    state = 10
                # Set the new loop state in the database.
                await set_loop_db(chat_id, state)
                # Reply with a message indicating the new loop state.
                return await message.reply_text(
                    text=_["admin_18"].format(state, message.from_user.mention),
                    reply_markup=close_markup(_),
              
