import asyncio
from IroXMusic.misc import db # Importing the db module from IroXMusic.misc
from IroXMusic.utils.database import get_active_chats, is_music_playing # Importing get_active_chats and is_music_playing functions

async def stop_music_if_playing():
    """Coroutine to continuously check if music is playing in any active chats and stop it if necessary."""
    while True:
        # Get a list of active chats in the database
        active_chats = get_active_chats()

        # Check if music is currently playing in any of the active chats
        is_playing = is_music_playing()

        # If music is playing in any of the active chats, stop it
        if is_playing:
            await db.stop_music(active_chats[0])

        # Wait for a certain amount of time before checking the status of music playback again
        wait_time = 10 # Wait time in seconds
        await asyncio.sleep(wait_time)

# Call the stop_music_if_playing coroutine using asyncio.create_task
asyncio.create_task(stop_music_if_playing())
