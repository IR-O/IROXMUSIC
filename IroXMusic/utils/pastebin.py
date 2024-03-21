import aiohttp
import asyncio
import typing

async def fetch(session: aiohttp.ClientSession, url: str) -> typing.Optional[str]:
    """
    Asynchronously fetches the content of the given URL.

    :param session: The aiohttp ClientSession object to use for the request.
    :param url: The URL to fetch the content from.
    :return: A string containing the content of the URL or None if an error occurred.
    """
    try:
        async with session.get(url) as response:  # Use the session to send a GET request to the URL.
            return await response.text()  # Return the response content as a string.
    except aiohttp.ClientError as exc:  # If an aiohttp ClientError occurs,
        print(f"Failed to fetch {url}: {exc}")  # print an error message and return None.
    return None

async def main() -> None:
    """
    The main function that fetches the content of multiple URLs asynchronously.

    It creates an aiohttp ClientSession, initializes a list of URLs to fetch,
    creates a list of coroutines by calling fetch() for each URL,
    runs all the coroutines concurrently using asyncio.gather(),
    and prints the first 100 characters of each successful response.
    """
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.google.com",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]  # Create a list of coroutines.
        responses = await asyncio.gather(*tasks)  # Run all the coroutines concurrently.
        for response in responses:
            if response is not None:
                print(response[:100] + "...")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main() function using asyncio.run().
