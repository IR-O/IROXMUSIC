import os
from config import autoclean # Import the autoclean list from the config module

async def auto_clean(file: str) -> None:
    """
    This function removes a file from the `autoclean` list and the file system if it exists.

    Args:
        file (str): The path of the file to be removed.

    Returns:
        None
    """
    try:
        rem = file # Assign the file parameter to a shorter variable name for readability

        # Check if the file parameter is a non-empty string and return if it's not
        if not rem or not isinstance(rem, str) or rem == "":
            return

        # Remove the file from the autoclean list
        autoclean.remove(rem)

        # Check if the file is still in the autoclean list after removal
        if autoclean.count(rem) != 0:
            return

        # Check if the file is not a video, live, or index file
        if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
            try:
                # Check if the file exists and remove it if it does
                if os.path.isfile(rem):
                    os.remove(rem)
            except Exception as e:
                # Print an error message if there's an issue removing the file
                print(f"Error removing file {rem}: {str(e)}")
    except Exception as e:
        # Print an error message if there's an issue in the auto_clean function
        print(f"Error in auto_clean: {str(e)}")
