import re
from typing import Union, List

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch

# This module contains functions for scraping song lyrics and related metadata
# from various online sources.

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

# TODO: Add docstrings to each function with a brief description, arguments,
# and return values.
