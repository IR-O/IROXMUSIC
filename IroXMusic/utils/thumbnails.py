import os
import re
import sys

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch
from pathlib import Path
from typing import Final, AsyncContextManager, List, Dict, Tuple, Optional
from contextlib import asynccontextmanager

import aiohttp
from youtubesearchpython.__future__ import VideosSearch
from IroXMusic import app
from config import YOUTUBE_IMG_URL

# Constants
CACHE_DIR: Final = Path("cache")
THUMBNAIL_FORMAT: Final = "thumb{}.png"
YOUTUBE_URL: Final = "https://www.youtube.com/watch?v={}"

def change_image_size(max_width: int, max_height: int, image: Image.Image) -> Image.Image:
    width_ratio = max_width / image.size[0]
    height_ratio = max_height / image.size[1]
    new_width = int(width_ratio * image.size[0])
    new_height = int(height_ratio * image.size[1])
    new_image = image.resize((new_width, new_height))
    return new_image

def clear(text: str) -> str:
    words = text.split(" ")
    title = ""
    for word in words:
        if len(title) + len(word) < 60:
            title += " " + word
    return title.strip()

@asynccontextmanager
async def aopen(file: Union[str, Path], mode: str) -> AsyncContextManager[aiofiles.AIOFile]:
    async with aiofiles.open(file, mode) as f:
        yield f

async def get_thumb(videoid: str) -> Optional[str]:
    cache_file: Path = CACHE_DIR / THUMBNAIL_FORMAT.format(videoid)
    if cache_file.exists():
        return str(cache_file)

    url = YOUTUBE_URL.format(videoid)
    try:
        results = VideosSearch(url, limit=1)
        result = await results.next()["result"][0]
    except (IndexError, VideosSearchError, aiohttp.ClientError):
        print(f"Error fetching video info for {videoid}", file=sys.stderr)
        return YOUTUBE_IMG_URL

    try:
        title = unidecode(result["title"])
        title = re.sub(r"\W+", " ", title)
        title = title.title()
    except KeyError:
        title = "Unsupported Title"

    try:
        duration = result["duration"]
    except KeyError:
        duration = "Unknown Mins"

    thumbnail = result["thumbnails"][0]["url"].split("?")[0]

    try:
        views = result["viewCount"]["short"]
    except KeyError:
        views = "Unknown Views"

    try:
        channel = result["channel"]["name"]
    except KeyError:
        channel = "Unknown Channel"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    async with aopen(cache_file, "wb") as f:
                        await f.write(await resp.read())
    except (aiohttp.ClientError, OSError):
        print(f"Error downloading thumbnail for {videoid}", file=sys.stderr)
        return YOUTUBE_IMG_URL

    youtube = Image.open(str(cache_file))
    image1 = change_image_size(1280, 720, youtube)
    image2 = image1.convert("RGBA")
    background = image2.filter(filter=ImageFilter.BoxBlur(10))
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.5)
    draw = ImageDraw.Draw(background)
    arial = ImageFont.truetype("IroXMusic/assets/font2.ttf", 30)
    font = ImageFont.truetype("IroXMusic/assets/font.ttf", 30)
    draw.text((1110, 8), unidecode(app.name), fill="white", font=arial)
    draw.text(
        (55, 560),
        f"{channel} | {views[:23]}",
        (255, 255, 255),
        font=arial,
    )
    draw.text(
        (57, 600),
        clear(title),
        (255, 255, 255),
        font=font,
    )
    draw.line(
        [(55, 660), (1220, 660)],
