# music_platforms.py
# This module defines a dictionary of music platforms and their corresponding
# API module names. This is used to dynamically import the appropriate API
# modules in api_classes.py.

MUSIC_PLATFORMS = {
    "AppleMusic": "apple_music",
    "TikTok": "tik_tok",
    "Resso": "resso",
    "Soundcloud": "soundcloud",
    "Spotify": "spotify",
}

__all__ = list(MUSIC_PLATFORMS.keys())


# api_classes.py
# This module dynamically imports the API modules specified in music_platforms.py
# and provides a function to get the appropriate API class by platform name.

import importlib

class_map = {
    "apple_music": "AppleAPI",
    "tik_tok": "TikTokAPI",
    "resso": "RessoAPI",
    "soundcloud": "SoundcloudAPI",
    "spotify": "SpotifyAPI",
}

def get_api_class(platform):
    if platform.lower() in MUSIC_PLATFORMS:
        api_module = importlib.import_module(f".{MUSIC_PLATFORMS[platform.lower()]}", package="music_api.apis")
        return getattr(api_module, class_map[MUSIC_PLATFORMS[platform.lower()]])
    else:
        raise ValueError(f"Invalid platform: {platform}")

__all__ = ["get_api_class"]
