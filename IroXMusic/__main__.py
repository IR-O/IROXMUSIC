#!/usr/bin/env python3

import argparse
import importlib
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PARENT_DIR = SCRIPT_DIR.parent

sys.path.insert(0, str(PARENT_DIR))

def import_module(module_name: str) -> object:
    """
    Import a module with a given name. If the module is not found, print an error message and exit the program.
    """
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        print(f"Error: {e}. Check the module name and try again.")
        sys.exit(1)

def run_main(module: object) -> None:
    """
    Run the "main" function of a given module.
    """
    if hasattr(module, "main") and callable(module.main):
        module.main()
    else:
        print(f"Error: The 'main' module does not have a 'main' function or it is not callable.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the main function of a given module.")
    parser.add_argument("module", help="The name of the module to import and run.")
    args = parser.parse_args()

    if str(PARENT_DIR) == str(Path.cwd()):
        run_main(import_module(args.module))
    else:
        print
