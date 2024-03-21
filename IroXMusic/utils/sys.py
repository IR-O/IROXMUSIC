import time
import psutil
from typing import Tuple

from IroXMusic.misc import _boot_
from IroXMusic.utils.formatters import get_readable_time


async def bot_sys_stats() -> Tuple[str, str, str, str]:
    bot_uptime = int(time.time() - _boot_)
    UP = f"{get_readable_time(bot_uptime)}"

    try:
        interval = max(0.1, 0.5)  # Ensure interval is at least 0.1 seconds
        CPU = f"{psutil.cpu_percent(interval=interval)}%"
        RAM = f"{psutil.virtual_memory().percent}%"

        partition = "/"  # Default to root partition
        DISK = f"{psutil.disk_usage(partition).percent}%"

    except Exception as e:
        print(f"Error getting system stats: {e}")
        CPU, RAM, DISK = "", "", ""

    return UP, CPU, RAM, DISK
