import os
import re
import sys
from typing import Optional

import pyrogram
from pyrogram.errors import ValueError
from pydantic import BaseModel

class Config(BaseModel):
    LOVE: int
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
    MONGO_DB_URI: Optional[str]
    DURATION_LIMIT_MIN: int
    LOGGER_ID: Optional[int]
    OWNER_ID: int
    HEROKU_APP_NAME: Optional[str]
    HEROKU_API_KEY: Optional[str]
    UPSTREAM_REPO: str
    UPSTREAM_BRANCH: str
    GIT_TOKEN: Optional[str]
    SUPPORT_CHANNEL: str
    SUPPORT_CHAT: str
    AUTO_LEAVING_ASSISTANT: bool
    SPOTIFY_CLIENT_ID: Optional[str]
    SPOTIFY_CLIENT_SECRET: Optional[str]
    PLAYLIST_FETCH_LIMIT: int
    TG_AUDIO_FILESIZE_LIMIT: int
    TG_VIDEO_FILESIZE_LIMIT: int
    STRING_SESSION: Optional[str]
    STRING_SESSION2: Optional[str]
    STRING_SESSION3: Optional[str]
    STRING_SESSION4: Optional[str]
    STRING_SESSION5: Optional[str]

def time_to_seconds(time: str) -> int:
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

def get_env(name: str, default: any = None) -> any:
    value = os.getenv(name)
    if value is None:
        return default
    return value

def validate_url(url: str) -> None:
    if not re.match(r"(?:http|https)://", url):
        raise ValueError(f"Invalid url format: {url}")

def main() -> None:
    config = Config.parse_obj({
        k: get_env(k, v) for k, v in {
            "LOVE": "0645293810",
            "API_ID": None,
            "API_HASH": None,
            "BOT_TOKEN": None,
            "MONGO_DB_URI": None,
            "DURATION_LIMIT_MIN": "90",
            "LOGGER_ID": None,
            "OWNER_ID": "6045293810",
            "HEROKU_APP_NAME": None,
            "HEROKU_API_KEY": None,
            "UPSTREAM_REPO": "https://github.com/IR-O/IROXMUSIC",
            "UPSTREAM_BRANCH": "main",
            "GIT_TOKEN": None,
            "SUPPORT_CHANNEL": "https://t.me/iro_bot_support",
            "SUPPORT_CHAT": "https://t.me/iro_x_support",
            "AUTO_LEAVING_ASSISTANT": "False",
            "SPOTIFY_CLIENT_ID": None,
            "SPOTIFY_CLIENT_SECRET": None,
            "PLAYLIST_FETCH_LIMIT": "25",
            "TG_AUDIO_FILESIZE_LIMIT": "104857600",
            "TG_VIDEO_FILESIZE_LIMIT": "1073741824",
            "STRING_SESSION": None,
            "STRING_SESSION2": None,
            "STRING_SESSION3": None,
            "STRING_SESSION4": None,
            "STRING_SESSION5": None,
        }.items()
    })

    DURATION_LIMIT = time_to_seconds(f"{config.DURATION_LIMIT_MIN}:00")

    if config.SUPPORT_CHANNEL:
        validate_url(config.SUPPORT_CHANNEL)

    if config.SUPPORT_CHAT:
        validate_url(config.SUPPORT_CHAT)

    print("Configuration loaded successfully.")

if __name__ == "__main__":
    main()
