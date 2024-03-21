import asyncpg
from typing import (
    Dict,
    Final,
    List,
    Optional,
    Union,
)

import random
import pymongo
from IroXMusic import userbot

mongo_client = pymongo.MongoClient()
db = mongo_client.IroXMusic

collections: Dict[str, pymongo.collection.Collection] = {
    "adminauth": db.adminauth,
    "authuser": db.authuser,
    "autoend": db.autoend,
    "assistants": db.assistants,
    "blacklistChat": db.blacklistChat,
    "blockedusers": db.blockedusers,
    "chats": db.chats,
    "cplaymode": db.cplaymode,
    "upcount": db.upcount,
    "gban": db.gban,
    "language": db.language,
    "onoffper": db.onoffper,
    "playmode": db.playmode,
    "playtypedb": db.playtypedb,
    "skipmode": db.skipmode,
    "sudoers": db.sudoers,
    "tgusersdb": db.tgusersdb,
}

FinalVars = Dict[str, Union[List, Dict]]
final_vars: FinalVars = {
    "active": [],
    "activevideo": [],
    "assistantdict": {},
    "autoend": {},
    "count": {},
    "channelconnect": {},
    "langm": {},
    "loop": {},
    "maintenance": [],
    "nonadmin": {},
    "pause": {},
    "playmode": {},
    "playtype": {},
    "skipmode": {},
}
