import json
import subprocess


def get_readable_time(seconds: int) -> str:
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
    """Humanize size."""
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
    """Convert a number from base 10 to a given base."""
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
    """Convert time string to seconds."""
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def seconds_to_min(seconds: int) -> str:
    """Convert seconds to a formatted time string."""
    if seconds is None:
        return ""
    d, h, m, s = divmod(seconds, 86400), divmod(seconds, 3600), divmod(seconds, 60), seconds % 60
    return f"{d:02d}:{h:02d}:{m:02d}:{s:02d}" if d else f"{h:02d}:{m:02d}:{s:02d}"


def speed_converter(seconds: float, speed: float) -> tuple[str, float]:
    """Convert time and speed to a formatted time string."""
    if speed == 0.5:
        seconds *= 2
    elif speed == 0.75:
        seconds += (50 * seconds) // 100
    elif speed == 1.5:
        seconds -= (25 * seconds) // 100
    elif speed == 2.0:
        seconds -= (50 * seconds) // 100
    return seconds_to_min(seconds), seconds


def check_duration(file_path: str) -> float:
    """Check the duration of a video file."""
    command = [
        "ffprobe",
        "-loglevel",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file_path,
    ]

    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = pipe.communicate()
    json_data = json.loads(out)

    if "format" in json_data:
        if "duration" in json_data["format"]:
            return float(json_data["format"]["duration"])

    if "streams" in json_data:
        for stream in json_data["streams"]:
            if "duration" in stream:
                return float(stream["duration"])

    return -1


# List of supported video formats
FORMATS: list[str] = [
    "webm",
    "mkv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "rrc",
    "gifv",
    "mng",
    "mov",
    "avi",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
   
