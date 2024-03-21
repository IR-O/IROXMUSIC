import socket
import time

import heroku3
from pyrogram import filters

import config
from IroXMusic.core.mongo import mongodb

from .logging import LOGGER
# Importing the LOGGER from logging.py to log messages

SUDOERS = filters.user()
_boot_ = time.time()

def is_heroku():
    # Returns True if the code is running on Heroku, else False
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

def dbb():
    # Initializes an empty dictionary 'db' and logs a message indicating that the local database has been initialized
    global db
    db = {}
    LOGGER(__name__).info(f"Local Database Initialized.")


async def sudo():
    # Loads the sudoers list from the MongoDB database and adds the owner ID to it if it's not already present
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"Sudoers Loaded.")


def heroku():
    # Initializes the Heroku app object if the code is running on Heroku and the required configuration variables are set
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"Heroku App Configured")
            except BaseException:
                LOGGER
