from IroXMusic import app
from IroXMusic.utils.database import get_cmode
import logging

async def get_channel_playCB(_, command: str, CallbackQuery) -> tuple[str | None, str | None]:
    """
    This function gets the chat ID and channel title for the given CallbackQuery.

    If the command is "c", it retrieves the chat ID from the database and the channel title from the chat.
    If the command is not "c", it gets the chat ID from the CallbackQuery and sets the channel title to None.

    Args:
        _: The first parameter is a leading underscore, which is often used in Python to indicate that a parameter is not used in the function definition.
        command (str): The command to be processed.
        CallbackQuery: An instance of the CallbackQuery class, which contains information about the callback query.

    Returns:
        A tuple of the chat ID and the channel title (or None if the channel title could not be retrieved).
    """
    chat_id = None  # Initialize chat_id to None
    channel = None  # Initialize channel to None

    if command == "c":
        # If the command is "c", get the chat ID from the database and the channel title from the chat.
        chat_id = await get_cmode(CallbackQuery.message.chat.id)

        if chat_id is None:
            # If the chat ID is None, show an alert with the text from the "setting_7" key and return.
            try:
                if _["setting_7"] is not None:
                    await CallbackQuery.answer(_["setting_7"], show_alert=True)
            except Exception as e:
                logging.error(f"Error while answering callback query: {e}")
            return

        try:
            # Get the chat information using the app.get_chat() method.
            chat = await app.get_chat(chat_id)

            if chat is not None and chat.title is not None:
                # If the chat object and its title are not None, set the channel to the chat title.
                channel = chat.title
        except Exception as e:
            logging.error(f"Error while getting chat: {e}")
    
    elif CallbackQuery is not None:
