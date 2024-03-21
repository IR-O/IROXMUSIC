import os
from config import autoclean  # Import the autoclean list from the config module

async def auto_clean(file_path: str) -> None:
    """
    This function removes a file from the `autoclean` list and the file system if it exists.

    Args:
        file_path (str): The path of the file to be removed.

    Returns:
        None
    """
    # Check if the file_path is a valid string
    if not file_path or not isinstance(file_path, str) or file_path == "":
        return

    try:
        # Remove the file from the autoclean list
        autoclean.remove(file_path)

        # Check if the file is still in the autoclean list after removal
        if autoclean.count(file_path) != 0:
            return

        # Check if the file is not a video, live, or index file
        if "vid_" not in file_path and "live_" not in file_path and "index_" not in file_path:
            # Check if the file exists in the file system
            if os.path.isfile(file_path):
                try:
                    # Remove the file from the file system
                    os.remove(file_path)
                except Exception as e:
                    # Print the error message if there is an error in removing the file
                    print(f"Error removing file {file_path}: {str(e)}")
            else:
                # Print a message if the file is not found in the file system
                print(f"File {file_path} not found in the file system.")
    except ValueError:
        # Print a message if the file is not found in the autoclean list
        print(f"File {file_path} not found in the autoclean list.")
    except Exception as e:
        # Print a message if there is an error in the function
        print(f"Error in auto_clean: {str(e)}")
