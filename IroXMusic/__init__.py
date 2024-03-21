# Importing necessary modules and libraries
import os
import sys

import IroXMusic.core.bot as bot_module
import IroXMusic.core.userbot as userbot_module
import IroXMusic.core.dir as dir_module
import IroXMusic.core.git as git_module
import IroXMusic.core.db as db_module
import IroXMusic.core.heroku as heroku_module
import IroXMusic.core.platforms.apple as apple_module
import IroXMusic.core.platforms.carbon as carbon_module
import IroXMusic.core.platforms.soundcloud as soundcloud_module
import IroXMusic.core.platforms.spotify as spotify_module

# Defining APIs dictionary with various music platforms and their corresponding API classes
APIS = {
    "Apple": apple_module.AppleAPI,
    "Carbon": carbon_module.CarbonAPI,
    "SoundCloud": soundcloud_module.SoundAPI,

