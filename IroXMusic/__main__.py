import asyncio
import importlib
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os:path.abspath(os.path.join(current_directory, ".."))
sys.path.insert(0, parent_directory)

def import_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        print(f"Error: {e}. Check the module name and try again.")
        sys.exit(1)

def run_main():
    main_module = import_module("main")
    main_module.main()

if __name__ == "__main__":
    run_main()
