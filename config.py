import os
import re
import sys
from typing import Optional

import pyrogram
from pyrogram.errors import Value Error
from pydantic import BaseModel

class CustomBaseModel(BaseModel):
    def dict(self, *args, **kwargs):
        return super().dict(exclude_unset=True, *args, **kwargs)

