import asyncio
import time

# Pyrogram libraries
import pyrogram
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message

# IroXMusic libraries
import app
from IroXMusic.core.call import Irop
from IroXMusic.misc import db
from IroXMusic.utils.database import get_assistant, get_authuser_names, get_cmode
from IroXMusic.utils.decorators import ActualAdminCB, AdminActual
from IroXMusic.utils.formatters import alpha_to_int, get_readable_time

# Configuration
import config

# Assigning the imported modules to variables with lowercase names is a common convention
# to distinguish between classes and functions (uppercase) and variables (lowercase)
banned_users = config.BANNED_USERS
adminlist = config.adminlist
lyrical = config.lyrical
