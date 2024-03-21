import re
import typing
import asyncio
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch
import config


class SpotifyAPI:
    """
    A class that provides methods to interact with the Spotify API and search for
    corresponding YouTube videos.
    """

    def __init__(self):
        """
        Initialize the SpotifyAPI object with the necessary attributes.
        """
        self.regex = re.compile(r"^https?://open\.spotify\.com/.*$")
        self.client_id = config.SPOTIFY_CLIENT_ID  # Spotify API client ID
        self.client_secret = config.SPOTIFY_CLIENT_SECRET  # Spotify API client secret
        self.scope = "playlist-read-private user-library-read"  # Spotify API scope
        self.redirect_uri = "http://localhost:8888/callback"  # Spotify API redirect URI
        self.sp = None  # Spotify API client

    def get_auth_manager(self):
        """
        Return an authenticated SpotifyOAuth object if the client_id and client_secret
        are provided, otherwise raise a ValueError.
        """
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

    async def authenticate(self):
        """
        Authenticate the Spotify API client and set the self.sp attribute.
        """
        self.sp = spotipy.Spotify(auth_manager=self.get_auth_manager())

    async def valid(self, link: str) -> bool:
        """
        Return True if the given link matches the Spotify track URL pattern, otherwise
        return False.
        """
        return bool(self.regex.match(link))

    async def track(self, link: str) -> typing.Tuple[dict, str]:
        """
        Fetch track details from the Spotify API and search for the corresponding
        YouTube video. Return a tuple containing the track details and YouTube video
        ID if found, otherwise raise a ValueError.
        """
        await self.authenticate()
        if not self.regex.match(link):
            raise ValueError("Invalid Spotify track link")

        track = self.sp.track(link)
        info = self.get_artist_names(track['artists']) + " " + track['name']
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
        """
        Fetch playlist details from the Spotify API and return a tuple containing
        the list of track names and the playlist ID.
        """
        await self.authenticate()
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify playlist link")

        playlist = self.sp.playlist(url)
        results = [
            self.get_artist_names(item['track']['artists']) + " " + item['track']['name']
            for item in playlist["tracks"]["items"]
        ]
        return results, playlist["id"]

    async def album(self, url: str) -> typing.Tuple[list, str]:
        """
        Fetch album details from the Spotify API and return a tuple containing
        the list of track names and the album ID.
        """
        await self.authenticate()
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify album link")

        album = self.sp.album(url)
        results = [
            self.get_artist_names(item['artists']) + " " + item['name']
            for item in album["tracks"]["items"]
        ]
        return results, album["id"]

    async def artist(self, url: str) -> typing.Tuple[list, str]:
        """
        Fetch artist details from the Spotify API and return a tuple containing
        the list of top tracks and the artist ID.
        """
        await self.authenticate()
        if not self.regex.match(url):
            raise ValueError("Invalid Spotify artist link")

        artistinfo = self.sp.artist(url)
        artist_id = artistinfo["id"]
        results = [
            self.get_artist_names(item['artists']) + " " + item['name']
            for item in self.sp.artist_top_tracks(url)["tracks"]
        ]
        return results, artist_id

    async def search_youtube(self, query: str) -> list:
        """
        Search for YouTube videos using the youtubesearchpython library and return
        a list of results.
        """
        vs = VideosSearch(query, limit=5)
        tasks = [self.fetch_youtube_result(vs, i) for i in range(5)]
        results = await asyncio.gather(*tasks)
        return [result for result in results if result]

    def fetch_youtube_result(self, vs, index):
        """
        Fetch a single YouTube search result and return a dictionary containing
        the result details.
        """
        try:
            result = vs.result["result"][index]
            return {
                "title": result["title"],
                "link": result["link"],
                "vidid": result["
