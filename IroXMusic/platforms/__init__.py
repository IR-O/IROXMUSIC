# Import various API classes for different music streaming platforms and other services
from .Apple import AppleAPI  # Apple Music API
from .Carbon import CarbonAPI  # TikTok (formerly Musical.ly) API
from .Resso import RessoAPI  # Resso API
from .Soundcloud import SoundAPI  # Soundcloud API
from .Spotify import SpotifyAPI  # Spotify API
from .Telegram import TeleAPI  # Telegram API
from .Youtube import YouTubeAPI  # YouTube API

# Each API class provides a set of methods to interact with the corresponding service's API
# These classes can be used to build custom integrations with these services in your application
