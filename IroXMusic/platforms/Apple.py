import re
from typing import Union, List

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython.__future__ import VideosSearch

class AppleAPI:
    """
    Class for scraping data from Apple Music playlists.
    """

    def __init__(self):
        """
        Initialize the AppleAPI class with a regular expression for validating Apple Music playlist links
        and the base URL for Apple Music playlists.
        """
        self.regex = re.compile(r"^https?://music\.apple\.com/.*playlist/.*$")
        self.base = "https://music.apple.com/in/playlist/"

    async def valid(self, link: str) -> bool:
        """
        Check if the given link is a valid Apple Music playlist link.

        Args:
            link (str): The link to check.

        Returns:
            bool: True if the link is valid, False otherwise.
        """
        return bool(self.regex.match(link))

    async def track(self, url: str, playid: Union[bool, str] = None) -> dict:
        """
        Scrape track details from a given Apple Music playlist link.

        Args:
            url (str): The Apple Music playlist link.
            playid (bool or str, optional): The playlist ID. Defaults to None.

        Returns:
            dict: A dictionary containing the track details.
        """
        if playid:
            url = self.base + url

        # Create a new aiohttp ClientSession and get the HTML content of the URL
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return False
                html = await response.text()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Find the Open Graph title tag to get the name of the playlist
        search = None
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:title":
                search = tag.get("content", None)

        # If the Open Graph title tag is not found, return False
        if search is None:
            return False

        # Search for the playlist on YouTube and extract the track details
        results = VideosSearch(search, limit=1)
        track_details = {}
        for result in (await results.next())["result"]:
            title = result["title"]
            ytlink = result["link"]
            vidid = result["id"]
            duration_min = result["duration"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]

            # Store the track details in a dictionary
            track_details = {
                "title": title,
                "link": ytlink,
                "vidid": vidid,
                "duration_min": duration_min,
                "thumb": thumbnail,
            }

        return track_details, vidid

    async def playlist(self, url: str, playid: Union[bool, str] = None) -> List[str]:
        """
        Scrape playlist details from a given Apple Music playlist link.

        Args:
            url (str): The Apple Music playlist link.
            playid (bool or str, optional): The playlist ID. Defaults to None.

        Returns:
            List[str]: A list of track names in the playlist.
        """
        if playid:
            url = self.base + url

        # Extract the playlist ID from the URL
        playlist_id = url.split("playlist/")[1]

        # Create a new aiohttp ClientSession and get the HTML content of the URL
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return False
                html = await response.text()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # TODO: Implement the logic for scraping the track names from the parsed HTML content

