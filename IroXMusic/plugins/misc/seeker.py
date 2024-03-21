import asyncio
from IroXMusic.misc import db # Importing the db module from IroXMusic.misc
from IroXMusic.utils.database import get_active_chats, is_music_playing # Importing get_active_chats and is_music_playing functions

async def stop_music_if_playing():
    """Coroutine to continuously check if music is playing in any active chats and stop it if necessary."""
    while True:
        try:
            # Get a list of active chats in the database
            active_chats = await get_active_chats()

            # Check if music is currently playing in any of the active chats
            is_playing = await is_music_playing()

            # If music is playing in any of the active chats, stop it
            if is_playing:
              
