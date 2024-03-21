import random
from typing import (
    Dict,
    Final,
    List,
    Optional,
    Union,
)

import asyncpg
from pymongo import MongoClient

from IroXMusic import userbot

mongo_client = MongoClient()
db = mongo_client.IroXMusic

authdb = db.adminauth
authuserdb = db.authuser
autoenddb = db.autoend
assdb = db.assistants
blacklist_chatdb = db.blacklistChat
blockeddb = db.blockedusers
chatsdb = db.chats
channeldb = db.cplaymode
countdb = db.upcount
gbansdb = db.gban
langdb = db.language
onoffdb = db.onoffper
playmodedb = db.playmode
playtypedb = db.playtypedb
skipdb = db.skipmode
sudoersdb = db.sudoers
usersdb = db.tgusersdb

active: Final[list] = []
activevideo: Final[list] = []
assistantdict: Final[dict] = {}
autoend: Final[dict] = {}
count: Final[dict] = {}
channelconnect: Final[dict] = {}
langm: Final[dict] = {}
loop: Final[dict] = {}
maintenance: Final[list] = []
nonadmin: Final[dict] = {}
pause: Final[dict] = {}
playmode: Final[dict] = {}
playtype: Final[dict] = {}
skipmode: Final[dict] = {}

