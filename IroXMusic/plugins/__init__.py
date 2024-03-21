import glob
from os.path import dirname, isfile

# Define the function to list all modules
def __list_all_modules():
    # Get the current working directory
    work_dir = dirname(__file__)
    
    # Find all .py files in the current working directory and its subdirectories
    mod_paths = glob.glob(work_dir + "/*/*.py")

    # Filter out directories, `__init__.py` files, and non-Python files
    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    # Sort and return the list of modules
    return sorted(all_modules)

# Call the function and store the result in ALL_MODULES
ALL_MODULES = __list_all_modules()

# Add ALL_MODULES to the list of publicly available variables (__all__)
__all__ = ALL_MODULES + ["ALL_MODULES"]
