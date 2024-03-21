# Importing necessary modules and libraries
import os  # For interacting with the operating system
from IroXMusic.core.bot import Irop  # Importing Irop class from IroXMusic.core.bot module
from IroXMusic.core.dir import dirr  # Importing dirr function from IroXMusic.core.dir module
from IroXMusic.core.git import git  # Importing git function from IroXMusic.core.git module
from IroXMusic.core.db import dbb  # Importing dbb function from IroXMusic.core.db module
from IroXMusic.core.heroku import heroku  # Importing heroku function from IroXMusic.core.heroku module
from IroXMusic.core.userbot import Userbot  # Importing Userbot class from IroXMusic.core.userbot module

# Calling dirr, git, dbb, and heroku functions to set up the directories, git, database, and heroku configurations
dirr()
git()
dbb()
heroku()

# Creating an instance of the Irop class and assigning it to the variable 'app'
app = Irop()

# Creating an instance of the Userbot class and assigning it to the variable 'userbot'
userbot = Userbot()

# Defining APIs dictionary with various music platforms and their corresponding API classes
APIs = {
    "Apple": "IroXMusic.platforms.AppleAPI",
    "Carbon": "IroXMusic.platforms.CarbonAPI",
    "SoundCloud": "IroXMusic.platforms.SoundAPI",
    "Spotify": "IroXMusic.platforms.SpotifyAPI",
}
