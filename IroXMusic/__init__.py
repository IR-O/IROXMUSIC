# Importing necessary modules and libraries
import os
from IroXMusic.core.bot import Irop
from IroXMusic.core.userbot import Userbot
from IroXMusic.core.platforms.apple import AppleAPI
from IroXMusic.core.platforms.carbon import CarbonAPI
from IroXMusic.core.platforms.soundcloud import SoundAPI
from IroXMusic.core.platforms.spotify import SpotifyAPI
from IroXMusic.core.dir import dirr as core_dirr
from IroXMusic.core.git import git as core_git
from IroXMusic.core.db import dbb as core_dbb
from IroXMusic.core.heroku import heroku as core_heroku

# Defining APIs dictionary with various music platforms and their corresponding API classes
APIS = {
    "Apple": AppleAPI,
    "Carbon": CarbonAPI,
    "SoundCloud": SoundAPI,
    "Spotify": SpotifyAPI,
}

def dirr():
    """Set up the directories"""
    try:
        core_dirr()
    except Exception as e:
        print(f"Error setting up directories: {e}")

def git():
    """Set up the git configuration"""
    try:
        core_git()
    except Exception as e:
        print(f"Error setting up git configuration: {e}")

def dbb():
    """Set up the database configuration"""
    try:
        core_dbb()
    except Exception as e:
        print(f"Error setting up database configuration: {e}")

def heroku():
    """Set up the heroku configuration"""
    try:
        core_heroku()
    except Exception as e:
        print(f"Error setting up heroku configuration: {e}")

# Calling dirr, git, dbb, and heroku functions to set up the directories, git, database, and heroku configurations
dirr()
git()
dbb()
heroku
