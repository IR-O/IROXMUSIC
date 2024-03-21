import os

def list_files(directory):
    """
    This function lists all files in a given directory.

    :param directory: The directory for which files need to be listed
    :return: A list of file names in the specified directory
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def file_exists(file_path):
    """
    This function checks if a file exists at the given file path.

    :param file_path: The file path to check for file existence
    :return: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)


def directory_exists(directory_path):
    """

