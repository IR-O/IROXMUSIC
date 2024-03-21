import asyncio
import os
from dotenv import load_dotenv

from pyrogram import Client
from pyrogram.errors import LoginRequired
from logging import getLogger
import config

