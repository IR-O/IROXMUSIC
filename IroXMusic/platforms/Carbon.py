import random
import os
import typing
from pathlib import Path
import aiohttp  # Asynchronous HTTP client/server for Python
from aiohttp import client_exceptions  # Exceptions for aiohttp client

class UnableToFetchCarbon(Exception):
    """
    This custom exception class can be raised when there is an issue with fetching carbon data.
    By defining a custom exception, it becomes easier to handle and identify specific errors related to fetching carbon data.
    """
    pass

async def fetch_carbon_data(url: str) -> typing.Union[str, UnableToFetchCarbon]:
    """
    This function asynchronously fetches carbon data from a given URL.
    If the request is successful, it returns the response content as a string.
    If there is an issue with the request, it raises a UnableToFetchCarbon exception.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise UnableToFetchCarbon(f"Failed to fetch carbon data. Status code: {response.status}")
        except client_exceptions.ClientConnectorError as error:
            raise UnableToFetchCarbon(f"Failed to connect to server: {error}")
        except aiohttp.ServerDisconnectedError as error:
            raise UnableToFetchCarbon(f"Server disconnected during carbon data fetch: {error}")
