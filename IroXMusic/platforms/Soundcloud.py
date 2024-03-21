import os
from pathlib import Path
from typing import Tuple, Dict

import youtube_dl
from IroXMusic.utils.formatters import seconds_to_min

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

    def is_soundcloud_link(self, link: str) -> bool:
        """
        Checks if the given link is a soundcloud link.
        :param link: The link to check
        :return: True if the link is a soundcloud link, False otherwise
        """
        return "soundcloud" in link

    def download(self, url: str) -> Tuple[Dict, str]:
        """
        Downloads the given url and returns the track details and the filepath of the downloaded file.
        :param url: The url to download
        :return: A tuple containing the track details and the filepath of the downloaded file
        """
        download_dir = Path("downloads")
        download_dir.mkdir(parents=True, exist_ok=True)

        ydl = youtube_dl.YoutubeDL(self.opts)
        try:
            info = ydl.extract_info(url)  # Extract information about the url
        except youtube_dl.DownloadError:
            return False, ""

        filepath = download_dir / f"{info['id']}.{info['ext']}"
        return info, str(filepath)
