from os import path  # Importing path from os module for file path manipulation

from yt_dlp import YoutubeDL  # Importing YoutubeDL from yt\_dlp module for downloading youtube videos

from IroXMusic.utils.formatters import seconds_to_min  # Importing seconds\_to\_min from formatters for converting seconds to minutes

class SoundAPI:
    def __init__(self):
        """
        Initializes the SoundAPI class with default options for YoutubeDL.
        """
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",  # Output template for the downloaded file
            "format": "best",  # Format of the downloaded file
            "retries": 3,  # Number of retries for failed downloads
            "nooverwrites": False,  # Whether to overwrite existing files
            "continuedl": True,  # Whether to continue downloading a partially downloaded file
        }

    async def valid(self, link: str):
        """
        Checks if the given link is a soundcloud link.
        :param link: The link to check
        :return: True if the link is a soundcloud link, False otherwise
        """
        if "soundcloud" in link:
            return True
        else:
            return False

    async def download(self, url):
        """
        Downloads the given url and returns the track details and the filepath of the downloaded file.
        :param url: The url to download
        :return: A tuple containing the track details and the filepath of the downloaded file
        """
        d = YoutubeDL(self.opts)  # Initialize YoutubeDL with the default options
        try:
            info = d.extract_info(url)  # Extract information about the url
        except:
            return False  # If an exception occurs, return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")  # Construct the filepath of the downloaded file
        duration
