import asyncio
import importlib
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
# Get the current directory where this script is located

parent_directory = os.path.abspath(os.path.join(current_directory, ".."))
# Join the current directory and ".." to move one level up to the parent directory

sys.path.insert(0, parent_directory)
# Insert the parent directory into the list of paths where Python looks for modules

def import_module(module_name):
    """
    Import a module with a given name. If the module is not found, print an error message and exit the program.
    """
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        print(f"Error: {e}. Check the module name and try again.")
        sys.exit(1)

def run_main():
    """
    Import the "main" module and run its "main" function.
    """
    main_module = import_module("main")
    main_module.main()

if __name__ == "__main__":
    # This block is executed only if the script is run directly, not imported as a module.
    run_main()
