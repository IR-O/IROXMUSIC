import time
import psutil
from typing import Tuple

from IroXMusic.misc import _boot_
from IroXMusic.utils.formatters import get_readable_time

async def bot_sys_stats() -> Tuple[str, str, str, str]:
    """
    This function returns the bot's uptime and system statistics (CPU, RAM, and DISK usage) as strings.
    """
    bot_uptime = int(time.time() - _boot_)  # Calculate bot uptime in seconds
    UP = f"{get_readable_time(bot_uptime)}"  # Convert uptime to a human-readable format

    try:
        # Set the minimum interval to 0.1 seconds to avoid potential freezing issues
        interval = max(0.1, 0.5) 
        CPU = f"{psutil.cpu_percent(interval=interval)}%"  # Get the CPU usage as a percentage
        RAM = f"{psutil.virtual_memory().percent}%"  # Get the RAM usage as a percentage

        # Default to the root partition for DISK usage calculation
        partition = "/"
        DISK = f"{psutil.disk_usage(partition).percent}%"  # Get the disk usage as a percentage

    except Exception as e:
        print(f"Error getting system stats: {e}")  # Print any exceptions encountered during execution
        CPU, RAM, DISK = "", "", ""  # Set the usage values to empty strings if an exception occurs

    return UP, CPU, RAM, DISK  # Return the calculated values
