import glob
import os

def list_all_modules() -> list[str]:
    """
    List all modules in the current working directory and its subdirectories.

    Returns:
        A sorted list of module names.
    """
    try:
        work_dir = os.path.abspath(os.path.dirname(__file__))
    except Exception as e:
        print(f"Error determining current working directory: {e}")
        return []

    mod_paths = glob.glob(os.path.join(work_dir, "**", "*.py"), recursive=True)

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if os.path.isfile(f) and f.endswith(".py") and
        not f.endswith("__init__.py") and
        not f.startswith("_") and
        f != __file__
    ]

    return sorted(all_modules)

ALL_MODULES = list_all_modules()

__all__ = ALL_MODULES + ["ALL_MODULES"]


import os

def list_all_modules() -> list[str]:
    """
    List all modules in the current working directory and its subdirectories.

    Returns:
        A sorted list of module names.
    """
    try:
        work_dir =
