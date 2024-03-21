import asyncio
from IroXMusic.misc import db
from IroXMusic.utils.database import get_active_chats, is_music_playing

async def stop_music_if_playing():
    while True:
        # Calling get_active_chats function to get a list of active chats in the database
        active_chats = get_active_chats()

        # Calling is_music_playing function to check if music is currently playing in any of the active chats
        is_playing = is_music_playing()

        # If music is playing in any of the active chats, the code below could be used to stop it
        if is_playing:
            await db.stop_music(active_chats[0])

        # Wait for a certain amount of time before checking the status of music playback again
        wait_time = 10 # Wait time in seconds
        await asyncio.sleep(wait_time)

# Call the stop_music_if_playing coroutine using asyncio.create_task
asyncio.create_task(stop_music_if_playing())
