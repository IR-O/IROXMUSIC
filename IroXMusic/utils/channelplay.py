from IroXMusic import app
from IroXMusic.utils.database import get_cmode

async def get_channel_playCB(_, command: str, CallbackQuery) -> tuple[str, str | None]:
    """Get the chat ID and channel title for the given CallbackQuery.

    If the command is "c", get the chat ID from the database and the channel title from the chat.
    If the command is not "c", get the chat ID from the CallbackQuery and set the channel title to None.

    Returns:
        A tuple of the chat ID and the channel title (or None if the channel title could not be retrieved).
    """
    chat_id = None
    channel = None

    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                if _["setting_7"] is not None:
                    await CallbackQuery.answer(_["setting_7"], show_alert=True)
            except:
                pass
            return

        try:
            chat = await app.get_chat(chat_id)
            if chat is not None and chat.title is not None:
                channel = chat.title
        except
