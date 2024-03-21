import socket
import time
import asyncio
from typing import List, Dict, Optional

import heroku3
from pyrogram import filters
from pymongo import MongoClient

import config
from .logging import LOGGER

_boot_ = time.time()

def is_heroku() -> bool:
    """Returns True if the code is running on Heroku, else False.

    This function checks if the code is running on Heroku by inspecting the fully qualified domain name (fqdn)
    of the socket.
    """
    return "heroku" in socket.getfqdn()

XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "main",
]

async def init_db() -> None:
    """Initializes an empty dictionary 'db' and logs a message indicating that the local database has been initialized.

    This asynchronous function is used to initialize an empty local database as a dictionary.
    """
    global db
    db = {}
    LOGGER(__name__).info("Local Database Initialized.")

async def load_sudoers() -> None:
    """Loads the sudoers list from the MongoDB database and adds the owner ID to it if it's not already present.

    This asynchronous function is used to load the sudoers list from the MongoDB database and adds the owner ID
    to it if it's not already present. It also logs a message indicating that the sudoers have been loaded.
    """
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = MongoClient(config.MONGO_URL, connect=False).IroXMusic.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudo else sudo

async def main():
    await init_db()
    await load_sudoers()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
