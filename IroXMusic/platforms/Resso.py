import re
from typing import Union

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython.__future__ import VideosSearch

class RessoAPI:
    def __init__(self):
        self.regex = re.compile(r"^https?://m\.resso\.com/.*$")
        self.base = "https://m.resso.com/"

    async def valid(self, link: str) -> bool:
        return bool(self.regex.fullmatch(link))

    async def track(self, url: str, playid: Union[bool, str] = None) -> dict:
        if playid:
            url = self.base + url
        async with aiohttp.ClientSession() as session:
            async with session.request("GET", url) as response:
                if response.status != 200:
                    return {"error": f"Invalid response status: {response.status}"}
                html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        title_tag = soup.find("meta", property="og:title")
        if title_tag is None:
            return {"error": "Missing og:title meta tag"}
        title = title_tag.get("content", None)
        desc_tag = soup.find("meta", property="og:description")
        if desc_tag is None:
            return {"error": "Missing og:description meta tag"}
        des = desc_tag.get("content", None)
        try:
            des = des.split("·")[0]
        except:
            pass
        if des == "":
            return {}
        results = VideosSearch(title, limit=1)
        try:
            result = (await results.next())["result"][0]
        except (IndexError, KeyError):
            return {"error": "No YouTube search results found"}
        title = result["title"]
        ytlink = result["link"]
        vidid = result["id"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        track_details = {
            "title": title,
            "link": ytlink,
            "vidid": vidid,

