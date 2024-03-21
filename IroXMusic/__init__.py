import os
from IroXMusic.core.bot import Irop
from IroXMusic.core.dir import dirr
from IroXMusic.core.git import git
from IroXMusic.core.db import dbb
from IroXMusic.core.heroku import heroku
from IroXMusic.misc import LOGGER

dirr()
git()
dbb()
heroku()

app = Irop()
userbot = IroXMusic.core.userbot.Userbot()

APIs = {
    "Apple": "IroXMusic.platforms.AppleAPI",
    "Carbon": "IroXMusic.platforms.CarbonAPI",
    "SoundCloud": "IroXMusic.platforms.SoundAPI",
    "Spotify": "IroXMusic.platforms.SpotifyAPI",

