def list_files(directory):
    """
    This function lists all files in a given directory.

    :param directory: The directory for which files need to be listed
    :return: A list of file names in the specified directory
    """
    return os.listdir(directory)


def file_exists(file_path):
    """
    This function checks if a file exists at the given file path.

    :param file_path: The file path to check for file existence
    :return: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)


def directory_exists(directory_path):
    """
    This function checks if a directory exists at the given directory path.

    :param directory_path: The directory path to check for directory existence
    :return: True if the directory exists, False otherwise
    """
    return os.path.isdir(directory_path)


def make_directory(directory_path):

