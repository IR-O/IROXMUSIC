# Import necessary modules
import random
import os
import typing
from pathlib import Path
import aiohttp  # Asynchronous HTTP client/server for Python
from aiohttp import client_exceptions  # Exceptions for aiohttp client

# Define a custom exception class named 'UnableToFetchCarbon' that inherits from the built-in 'Exception' class
class UnableToFetchCarbon(Exception):
    """
    This custom exception class can be raised when there is an issue with fetching carbon data.
    By defining a custom exception, it becomes easier to handle and identify specific errors related to fetching carbon data.
    """
    pass
