import json
import subprocess


def get_readable_time(seconds: int) -> str:
    """
    Convert a given number of seconds into a human-readable time string in the format of "Xh Ym Zs".

    This function calculates the time components (hours, minutes, and seconds) by repeatedly dividing the input
    seconds value by 60 until all the time components are calculated. The time components are then formatted
    as a string with their respective time suffixes.

    :param seconds: The number of seconds to convert to a human-readable time string.
    :return: A string representation of the time in the format of "Xh Ym Zs".
    """
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    for i in range(4):
        if seconds == 0:
            break
        div, mod = divmod(seconds, 60)
        time_list.append(mod)
        seconds = div

    time_list = [f"{t}{suf}" for t, suf in zip(reversed(time_list), time_suffix_list)]

    if len(time_list) == 4:
        time_list[-1], time_list[-2] = time_list[-2], time_list[-1]

    return ":".join(time_list)


def convert_bytes(size: float) -> str:
    """
    Convert a given number of bytes into a human-readable string with appropriate units.

    This function converts the input size in bytes to the appropriate unit (KiB, MiB, GiB, or TiB) by repeatedly
    dividing the input size by 1024 until the resulting size is less than 1024. The final size is then formatted
    as a string with two decimal places and the corresponding unit.

    :param size: The number of bytes to convert to a human-readable string.
    :return: A string representation of the size with appropriate units.
    """
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}

    while size > power:
        size /= power
        t_n += 1

    return f"{size:.2f} {power_dict[t_n]}B"


def convert_base(n: str, to_base: int = 10) -> str:
    """
    Convert a number from base 10 to a given base.

    This function converts a base-10 number to a given base by repeatedly dividing the input number by the base
    until the quotient is zero. The remainders from the divisions are then used to build the number in the
    desired base. The digits in the resulting number are represented using an alphabet of lowercase letters.

    :param n: The base-10 number to convert.
    :param to_base: The base to convert the number to. Default is 10.
    :return: A string representation of the number in the desired base.
    """
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
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

    This function parses a time string in the format of "Xh Ym Zs" and converts it to seconds by calculating
    the number of hours, minutes, and seconds and multiplying each by the appropriate number of seconds.

    :param time: The time string to convert to seconds.
    :return: The number of seconds represented by the time string.
    """
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def seconds_to_min(seconds: int) -> str:
    """
    Convert a given number of seconds to a formatted time string.

    This function converts a given number of seconds to a formatted time string in the format of "Xh Ym Zs".
    If the input seconds value is less than 60, the function returns a string in the format of "Xm Zs".

    :param seconds: The number of seconds to convert to a formatted time string.
    :return: A string representation of the time in the format of "Xh Ym Zs" or "Xm Zs".
    """
    if seconds is None:
        return ""
    d, h, m, s = divmod(seconds, 86400), divmod(seconds, 3600), divmod(seconds, 60), seconds % 60
    return f"{d:02d}:{h:02d}:{m:02d}:{s:02d}" if d else f"{h:02d}:{m
