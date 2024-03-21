import re
from typing import Union, List

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch

class LyricScraper:
    """
    This class contains functions for scraping song lyrics and related metadata
    from various online sources.
    """

    # The `re` module is used for regular expressions, which are helpful for
    # extracting specific patterns of text from HTML content.

    # The `typing` module is used to specify the expected types of function
    # arguments and return values, which can help with code readability and
    # static analysis tools.

    # The `aiohttp` module is used for asynchronous HTTP requests, which can
    # help improve the performance of the module by allowing multiple requests
    # to be made concurrently.

    # The `bs4` module is used for parsing HTML content. It provides a convenient
    # API for navigating and searching the HTML document tree.

    # The `VideosSearch` class from `youtube_search_python` is used for searching
    # YouTube for videos related to a given song or artist.

    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def search_song_on_youtube(self, query: str) -> Union[List[str], None]:
        """
        Searches YouTube for videos related to the given song or artist query.

        Args:
            query (str): The search query for YouTube.

        Returns:
            A list of video URLs if any videos were found, or None if no videos
            were found.
        """
        try:
            videos_search = VideosSearch(query, limit=10)
            result_videos = await self.session.get(videos_search.result()['search_url'])
            soup = BeautifulSoup(await result_videos.text(), 'html.parser')
            videos = [video['href'] for video in soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd
