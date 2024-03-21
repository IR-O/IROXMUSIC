import json
import subprocess

def get_readable_time(seconds: int) -> str:
    """
    Convert a given number of seconds into a human-readable time string in the format of "Xh Ym Zs".

    This function takes an integer representing the number of seconds and returns a string
    with a formatted time representation, using hours, minutes, and seconds.

    :param seconds: The number of seconds to convert to a human-readable time string.
    :return: A string representation of the time in the format of "Xh Ym Zs".
    """
    time_list = []
    time_suffix_list = ["s", "m", "h"]

    for i in range(3):
        if seconds == 0:
            break
        div, mod = divmod(seconds, 60)
        time_list.append(mod)
        seconds = div

    time_list = [f"{t}{suf}" for t, suf in zip(reversed(time_list), time_suffix_list)]

    if len(time_list) == 3:
        time_list[-1], time_list[-2] = time_list[-2], time_list[-1]

    return ":".join(time_list)

def convert_bytes(size: float) -> str:
    """
    Convert a given number of bytes into a human-readable string with appropriate units.

    This function takes a floating-point number representing the size in bytes and returns
    a string with a formatted size representation, using units such as KB, MB, GB, or TB.

    :param size: The number of bytes to convert to a human-readable string.
    :return: A string representation of the size with appropriate units.
    """
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: "B", 1: "KiB", 2: "MiB", 3: "GiB", 4: "TiB"}

    while size > power:
        size /= power
        t_n += 1

    return f"{size:.2f} {power_dict[t_n]}"

def convert_base(n: str, to_base: int = 10) -> str:
    """
    Convert a number from base 10 to a given base.

    This function takes a string representing a number in base 10 and an optional parameter
    for the base to convert the number to. It returns a string representation of the number
    in the desired base.

    :param n: The base-10 number to convert.
    :param to_base: The base to convert the number to. Default is 10.
    :return: A string representation of the number in the desired base.
    """
    alphabet = "0123456789abcdefghij"
    result = ""

    for char in n[::-1]:
        result += alphabet[int(char)]

    num = int(result[::-1])
    result = ""

    while num:
        num, rem = divmod(num, to_base)
        result += str(rem)

    return result[::-1]

def time_to_seconds(time: str) -> int:
    """
    Convert a time string in the format of "Xh Ym Zs" to seconds.

    This function takes a time string in the format of "Xh Ym Zs" and returns the number
    of seconds represented by the time string.

    :param time: The time string to convert to seconds.
    :return: The number of seconds represented by the time string.
    """
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

def seconds_to_min(seconds: int) -> str:
    """
    Convert a given number of seconds to a formatted time string.

    This function takes an integer representing the number of seconds and returns a
    formatted time string in the format of "Xh Ym Zs" or "Xm Zs", depending on the number
    of hours.

    :param seconds: The number of seconds to convert to a formatted time string.
    :return: A string representation of the time in the format of "Xh Ym Zs" or "Xm Zs".
    """
    if seconds
