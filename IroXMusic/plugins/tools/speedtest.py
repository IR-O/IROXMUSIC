import asyncio
import speedtest
from pyrogram import filters, Client as TelegramClient
from pyrogram.types import Message

from config import SUDOERS, LOVE
from utils.decorators.language import language


