import pathlib
from typing import Dict, Any
import yaml
from contextlib import suppress

# Initialize an empty dictionary to store language data
languages: Dict[str, Any] = {}

# Initialize an empty dictionary to store language codes and their corresponding names
languages_present: Dict[str, str] = {}

def get_string(lang: str, key: str) -> str:
    """
    Returns the translated string for the given language and key.
    If the key is not found in the language data, it returns a default message.
    """
    # Return the translated string or a default message if the key is not found
    return languages[lang].get(key, f"Missing translation for key '{key}' in language '{lang}'")

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

    # Open the language file and load its contents
    with filename.open(encoding="utf8") as f:
        lang_data = yaml.safe_load(f)

    # Add the language data to the languages dictionary using the language code as the key
    languages.setdefault(lang_code, {})
    languages[lang_code].update(lang_data)

    # Add the language code and name to the languages_present dictionary
    try:
        languages_present[lang_code] = languages[lang_code]["name"]
    # Print a warning if the 'name' key is missing in the language data
    except KeyError:
        print(f"Warning: missing 'name' key in language data for '{lang_code}'")

    # Print a warning if the language is not found in the languages dictionary
    except KeyError:
