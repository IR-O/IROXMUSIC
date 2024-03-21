import re
import typing
import asyncio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch
import config


class SpotifyAPI:
    def __init__(self):
        self.regex = re.compile(r"^https?://open\.spotify\.com/.*$")
        self.client_id = config.SPOTIFY_CLIENT_ID
        self.client_secret = config.SPOTIFY_CLIENT_SECRET
        self.scope = "playlist-read-private user-library-read"
        self.redirect_uri = "http://localhost:8888/callback"
        self.sp = spotipy.Spotify(auth_manager=self.get_auth_manager())

    def get_auth_manager(self):
        if self.client_id and self.client_secret:
            return SpotifyOAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                redirect_uri=self.redirect_uri,
                scope=self.scope,
                open_browser=False,
            )
        else:
            raise ValueError("Missing Spotify API credentials")

    async def valid(self, link: str) -> bool:
        return bool(self.regex.match(link))

    async def track(self, link: str) -> typing.Tuple[dict, str]:
        if not self.regex.match(link):
            raise ValueError("Invalid Spotify track link")
        track = self.sp.track(link)
        info = f"{track['name']} {self.get_artist_names(track['artists'])}"
        results = await self.search_youtube(info)
        if not results:
            raise ValueError("No YouTube video found for the track")
        track_details = {
            "title": results[0]["title"],
            "link": results[0]["link"],
            "vidid": results[0]["vidid"],
            "duration_min": results[0]["duration_min"],
            "thumb": results[0]["thumb"],
        }
        return track_details, results[0]["vidid"]

    async def playlist(self, url: str) -> typing.Tuple[list, str]:
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify playlist link")
        playlist = self.sp.playlist(url)
        results = [
            f"{item['track']['name']} {self.get_artist_names(item['track']['artists'])}"
            for item in playlist["tracks"]["items"]
        ]
        return results, playlist["id"]

    async def album(self, url: str) -> typing.Tuple[list, str]:
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify album link")
        album = self.sp.album(url)
        results = [
            f"{item['name']} {self.get_artist_names(item['artists'])}"
            for item in album["tracks"]["items"]
        ]
        return results, album["id"]

    async def artist(self, url: str) -> typing.Tuple[list, str]:
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify artist link")
        artistinfo = self.sp.artist(url)
        artist_id = artistinfo["id"]
        results = [
            f"{item['name']} {self.get_artist_names(item['artists'])}"
            for item in self.sp.artist_top_tracks(url)["tracks"]
        ]
        return results, artist_id

    async def search_youtube(self, query: str) -> list:
        vs = VideosSearch(query, limit=5)
        tasks = [self.fetch_youtube_result(vs, i) for i in range(5)]
        results = await asyncio.gather(*tasks)
        return [result for result in results if result]

    def fetch_youtube_result(self, vs, index):
        try:
            result = vs.result["result"][index]
            return {
                "title": result["title"],
                "link": result["link"],
                "vidid": result["id"],
                "duration_min": int(result["duration"][:-1]) // 60,
                "thumb": result["thumbnails"][0]["url"].split("?")[0],
            }
        except IndexError:
            return None
