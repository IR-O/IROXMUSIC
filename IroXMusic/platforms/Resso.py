import re
from typing import Dict, Union

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch

class RessoAPI:
    """
    A class to interact with Resso music streaming service.
    """

    def __init__(self):
        """
        Initialize the RessoAPI class with a regular expression for valid Resso links
        and the base URL for Resso web requests.
        """
        self.regex = re.compile(r"^https?://m\.resso\.com/.*$")  # Regular expression to match valid Resso links
        self.base = "https://m.resso.com/"  # Base URL for Resso web requests

    async def valid(self, link: str) -> bool:
        """
        Check if a given link is a valid Resso link.

        :param link: The link to check for validity.
        :return: True if the link is valid, False otherwise.
        """
        return bool(self.regex.match(link))  # Check if the link matches the regular expression

    async def track(self, url: str, playid: Union[bool, str] = None) -> Dict[str, Union[str, int]]:
        """
        Fetch track details from a given Resso link.

        :param url: The Resso link to fetch the track details from.
        :param playid: An optional play ID to use in the request.
        :return: A dictionary containing the track details.
        """
        if playid:
            url = self.base + url  # Add the base URL if a play ID is provided

        try:
            async with aiohttp.ClientSession() as session:  # Create a new session for the request
                async with session.get(url) as response:  # Send a GET request to the URL
                    if response.status != 200:  # Check if the response status is 200 OK
                        return {"error": f"Invalid response status: {response.status}"}  # Return an error message if not

                    html = await response.text()  # Get the response content as text
        except aiohttp.ClientError as e:
            return {"error": f"Error fetching HTML content: {e}"}

        soup = BeautifulSoup(html, "html.parser")  # Parse the HTML content

        metadata = soup.find("meta", attrs={"name": "description"})  # Find the meta description tag
        if metadata is None:  # Check if the tag was found
            return {"error": "Missing meta description tag"}  # Return an error message if not

        description = metadata.get("content", None)  # Get the content attribute of the tag
        if description is None or description == "":  # Check if the description is empty
            return {}  # Return an empty dictionary if so

        try:
            title, duration_min = self._parse_description(description)  # Parse the title and duration from the description
        except ValueError as e:
            return {"error": f"Error parsing description: {e}"}

        try:
            track_details = await self._get_youtube_track_details(title)  # Search for the track on YouTube
        except Exception as e:
            return {"error": f"Error fetching YouTube track details: {e}"}

        track_details.update({
            "duration_min": duration_min,
            "thumbnail": soup.find("meta", property="og:image")["content"]  # Get the thumbnail URL
        })

        return track_details

    def _parse_description(self, description: str) -> tuple[str, int]:
        """
        Parse the title and duration from the Resso track description.

        :param description: The Resso track description.
        :return: A tuple containing the title and duration.
        """
        split_description = description.split("·")  # Split the description by "·"
        title = split_description[0].strip()  # Get the title
        duration_str = split_description[1].strip() if len(split_description) > 1 else ""  # Get the duration

        try:
            duration_min = int(duration_str)  # Convert the duration to an integer
        except ValueError:
            raise ValueError(f"Invalid duration format: {duration_str}")

        return title, duration_min

    async def _get_youtube_track_details(self, title: str) -> Dict[str, Union[str, int]]:
        """
        Search for the track on YouTube and return the track details.

        :param title: The title of the track.
        :return: A dictionary containing the YouTube track details.
        """
        results = VideosSearch(title, limit=1)  # Search for the track on YouTube
        result = (await results.next())["result"][0]  # Get the first search result

        return {
            "title": result["title"],
            "link": result["link"],
            "vidid": result["id"],
            "thumbnail": result["thumbnails"][0]["url"].split("?")[0]  # Get the URL of the thumbnail
        }
