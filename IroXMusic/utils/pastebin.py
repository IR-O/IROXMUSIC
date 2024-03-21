import aiohttp
import asyncio
import typing

async def fetch(session: aiohttp.ClientSession, url: str) -> typing.Optional[str]:
    """Fetches the content of the given URL."""
    try:
        async with session.get(url) as response:
            return await response.text()
    except aiohttp.ClientError as exc:
        print(f"Failed to fetch {url}: {exc}")
    return None

async def main() -> None:
    """The main function that fetches the content of multiple URLs."""
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.google.com",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            if response is not None:
                print(response[:100] + "...")

if __name__ == "__main__":
    asyncio.run(main())
