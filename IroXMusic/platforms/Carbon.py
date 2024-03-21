import random
import os
import typing
from pathlib import Path

import aiohttp
from aiohttp import client_exceptions


class UnableToFetchCarbon(Exception):
    pass

