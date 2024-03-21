# music_platforms.py
# This module defines a dictionary of music platforms and their corresponding
# API module names. This is used to dynamically import the appropriate API
# modules in api_classes.py.
music_platforms = {
    "AppleMusic": "Apple",
    "TikTok": "Carbon",
    "Resso": "Resso",
    "Soundcloud": "Soundcloud",
    "Spotify": "Spotify",
}

# The __all__ variable is a list of module-level public objects. In this case,
# we set it to the keys of the music_platforms dictionary, which are the
# public music platform names.
__all__ = list(music_platforms.keys())



# api_classes.py
# This module dynamically imports the API modules specified in music_platforms.py
# and provides a function to get the appropriate API class by platform name.

from .Apple import AppleAPI  # Apple Music API
from .Carbon import CarbonAPI  # TikTok (formerly Musical.ly) API
from .Resso import RessoAPI  # Resso API
from .Soundcloud import SoundAPI  # Soundcloud API
from .Spotify import SpotifyAPI  # Spotify API

# The get_api_class function takes a platform name as input and returns the
# corresponding API class. It does this by looking up the platform name in
# the music_platforms dictionary to get the API module name, and then
# dynamically importing the module and accessing the API class using globals().
def get_api_class(platform):
    if platform.lower() in music_platforms:
        module_name = music_platforms[platform.lower()]
        return globals()[module_name + "API"]
    else:
        raise ValueError(f"Invalid platform: {platform}")

# The __all__ variable is a list of module-level public
