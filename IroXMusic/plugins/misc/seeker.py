import asyncio

from IroXMusic.misc import db # Importing the db module from IroXMusic.misc for database-related functionality
from IroXMusic.utils.database import get_active_chats, is_music_playing # Importing get_active_chats and is_music_playing functions from IroXMusic.utils.database for interacting with the database

# The following lines of code could be part of a larger function or method that handles some music-related functionality in the IroXMusic bot

# Calling get_active_chats function to get a list of active chats in the database
active_chats = get_active_chats()

# Calling is_music_playing function to check if music is currently playing in any of the active chats
is_playing = is_music_playing()

# If music is playing in any of the active chats, the code below could be used to stop it
# For example, the following line could be used to stop the music in the first active chat where it is playing
if is_playing:
    db.stop_music(active_chats[0])

# The following lines of code could be used to wait for a certain amount of time before checking the status of music playback again
# This could be useful in a loop that periodically checks if music is playing and stops it if necessary
wait_time = 10 # Wait time in seconds
await asyncio.sleep(wait_time)
