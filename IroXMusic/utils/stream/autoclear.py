import os
from config import autoclean


async def auto_clean(file: str) -> None:
    """
    Removes a file from the `autoclean` list and the file system if it exists.

    Args:
        file (str): The path of the file to be removed.

    Returns:
        None
    """
    try:
        rem = file
        if not rem or not isinstance(rem, str) or rem == "":
            return

        autoclean.remove(rem)
        if autoclean.count(rem) != 0:
            return

        if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
            try:
                if os.path.isfile(rem):
                    os.remove(rem)
            except Exception as e:
                print(f"Error removing file {rem}: {str(e)}")
    except Exception as e:
        print(f"Error in auto_clean: {str(e)}")
