# Importing required libraries
import asyncpg  # Asynchronous PostgreSQL database connector
from typing import (
    # Importing various types from the typing module
    Dict,
    Final,
    List,
    Optional,
    Union,
)

import random
import pymongo  # PyMongo is a Python driver for MongoDB
from IroXMusic import userbot  # Importing the userbot module from IroXMusic package

# Creating a connection to MongoDB
mongo_client = pymongo.MongoClient()

# Selecting the database 'IroXMusic'
db = mongo_client.IroXMusic

# Defining a dictionary to store collections in the database
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

# Defining a dictionary with final variables
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

