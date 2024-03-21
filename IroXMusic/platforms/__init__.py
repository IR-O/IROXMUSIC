# music_platforms.py
music_platforms = {
    "AppleMusic": "Apple",
    "TikTok": "Carbon",
    "Resso": "Resso",
    "Soundcloud": "Soundcloud",
    "Spotify": "Spotify",
}

__all__ = list(music_platforms.keys())


# api_classes.py
from .Apple import AppleAPI  # Apple Music API
from .Carbon import CarbonAPI  # TikTok (formerly Musical.ly) API
from .Resso import RessoAPI  # Resso API
from .Soundcloud import SoundAPI  # Soundcloud API
from .Spotify import SpotifyAPI  # Spotify API

def get_api_class(platform):
    if platform.lower() in music_platforms:
        module_name = music_platforms[platform.lower()]
        return globals()[module_name] + "API"
    else:
        raise ValueError(f"Invalid platform: {platform}")

__all__ = [get_api_class(platform) for platform in music_platforms.values()]


# telegram_api.py
from .Telegram import TeleAPI  # Telegram API

def get_api_class():
    return TeleAPI

__all__ = ["get_api_class"]


# youtube_api.py
from .Youtube import YouTubeAPI  # YouTube API

def get_api_class():
    return YouTubeAPI

__all__ = ["get_api_class"]


# main.py
from api_classes import *
from music_platforms import *
from youtube_api import *
from telegram_api import *

def main():
    # Initialize APIs
   
