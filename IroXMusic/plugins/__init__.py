import glob
import os

def list_all_modules() -> list[str]:
    """
    List all modules in the current working directory and its subdirectories.

    This function uses the `glob` module to find all Python files (.py) in the
    current working directory and its subdirectories. It then filters out any
    files that should not be considered modules (e.g., `__init__.py`, files
    starting with an underscore, or the current file itself). The function
    returns a sorted list of module names.

    Returns:
        A sorted list of module names.
    """
    try:
        # Get the absolute path of the current file's directory
        work_dir = os.path.abspath(os.path.dirname(__file__))
    except Exception as e:
        print(f"Error determining current working directory: {e}")
        return []

    # Find all .py files in the current working directory and its subdirectories
    mod_paths = glob.glob(os.path.join(work_dir, "**", "*.py"), recursive=True)

    all_modules = [
        # Generate the module name by removing the current working directory
        # path, replacing the directory separator with a dot, and removing
        # the .py extension and the last dot
        os.path.splitext(os.path.relpath(f, work_dir).replace(os.sep, "."))[0]
        for f in mod_paths
        if os.path.isfile(f) and not f.endswith("__init__.py") and
        not f.startswith("_") and
        f != __file__
    ]

    return sorted(all_modules)

# Call the function to list all modules and store the result in ALL_MODULES
ALL_MODULES = list_all_modules()

# Add ALL_MODULES to the __all__ list, along with any other desired modules
__all__ = ALL_MODULES + ["list_all_modules"]
