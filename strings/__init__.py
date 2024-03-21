import pathlib
from typing import Dict, Any
import yaml
from contextlib import suppress

def load_language(file_path: pathlib.Path) -> Dict[str, Any]:
    """
    Loads the language data from a YAML file.
    """
    with file_path.open(encoding="utf8") as f:
        lang_data = yaml.safe_load(f)
    return lang_data

def get_string(lang: str, key: str) -> str:
    """
    Returns the translated string for the given language and key.
    If the key is not found in the language data, it returns a default message.
    """
    try:
        return languages[lang][key]
    except KeyError:
        return f"Missing translation for key '{key}' in language '{lang}'"

# Initialize an empty dictionary to store language codes and their corresponding names
languages_present: Dict[str, str] = {}

# Initialize an empty dictionary to store language data
languages: Dict[str, Any] = {}

# Define the base path for language files
base_path = pathlib.Path("./strings/langs/")

# Iterate over all files in the base path
for filename in base_path.iterdir():
    # Skip files that do not have the .yml extension
    if not filename.suffix == ".yml":
        continue

    # Extract the language code from the filename
    lang_code = filename.stem

    # Skip the English language file
    if lang_code == "en":
        continue

    # Load the language data from the YAML file
    lang_data = load_language(filename)

    # Add the language data to the languages dictionary using the language code as the key
    languages[lang_code] = lang_data

    # Add the language code and name to the languages_present dictionary
    try:
        languages_present[lang_code] = lang_data["name"]
    # Print a warning if the 'name' key is missing in the language data
    except KeyError:
        print(f"Warning: missing 'name' key in language data for '{lang_code}'")

# Print a warning if the language is not found in the languages dictionary
except KeyError:
    print(f"Warning: language '{lang_code}' not found in languages")
