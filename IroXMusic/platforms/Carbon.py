import random
import os
import typing
from pathlib import Path
import aiohttp
from aiohttp import client_exceptions

class UnableToFetchCarbon(Exception):
    """This class defines a custom exception named 'UnableToFetchCarbon' that inherits from the built-in 'Exception' class.
    This exception can be raised when there is an issue with fetching carbon data."""
    pass

