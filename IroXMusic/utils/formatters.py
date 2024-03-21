import json
import subprocess

def get_readable_time(seconds: int) -> str:
    """
    Convert a given number of seconds into a human-readable time string in the format of "Xh Ym Zs".
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
    """
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds: int) -> str:
    """
    Convert a given number of seconds to a formatted time string.
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    time_str = ""
    if h:
        time_str += f"{h}h "
    if m:
        time_str += f"{m}m "
    time_str += f"{s}s"

    return time_str

# Example usage:
if __name__ == "__main__":
    time_str = "1h 30m 45s"
    seconds = time_to_seconds(time_str)
    print(f"{time_str} is equivalent to {seconds} seconds.")

    time_str = seconds_to_time(seconds)
    print(f"{seconds} seconds is equivalent to {time_str}.")

    size = 123456789
    size_str = convert_bytes(size)
    print(f"{size} bytes is equivalent to {size_str}.")

    n = "101"
    base10 = int(n, 3)
    base3 = convert_base(str(base10), 3)
    print(f"The base-3 representation of {base10} is {base3}.")
