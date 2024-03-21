import re
from typing import Union, Dict

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch  # Corrected import statement

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
        async with aiohttp.ClientSession() as session:  # Create a new session for the request
            async with session.request("GET", url) as response:  # Send a GET request to the URL
                if response.status != 200:  # Check if the response status is 200 OK
                    return {"error": f"Invalid response status: {response.status}"}  # Return an error message if not
                html = await response.text()  # Get the response content as text
        soup = BeautifulSoup(html, "html.parser")  # Parse the HTML content
        title_tag = soup.find("meta", property="og:title")  # Find the og:title meta tag
        if title_tag is None:  # Check if the tag was found
            return {"error": "Missing og:title meta tag"}  # Return an error message if not
        title = title_tag.get("content", None)  # Get the content attribute of the tag
        desc_tag = soup.find("meta", property="og:description")  # Find the og:description meta tag
        if desc_tag is None:  # Check if the tag was found
            return {"error": "Missing og:description meta tag"}  # Return an error message if not
        des = desc_tag.get("content", None)  # Get the content attribute of the tag
        try:
            des = des.split("·")[0]  # Split the content by "·" and get the first part
        except:
            pass
        if des == "":
            return {}  # Return an empty dictionary if the description is empty
        results = VideosSearch(title, limit=1)  # Search for the track title on YouTube
        try:
            result = (await results.next())["result"][0]  # Get the first search result
        except (IndexError, KeyError):
            return {"error": "No YouTube search results found"}  # Return an error message if no results were found
        title = result["title"]  # Get the title of the track
        ytlink = result["link"]  # Get the link to the track on YouTube
        vidid = result["id"]  # Get the ID of the track on YouTube
        duration_min = result["duration"]  # Get the duration of the track
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]  # Get the URL of the thumbnail
        track_details = {
            "title": title,
            "link": ytlink,
            "vidid": vidid,
            "duration_min": duration_min,
            "thumbnail": thumbnail,
        }
        return track_details  # Return a dictionary containing the track details
