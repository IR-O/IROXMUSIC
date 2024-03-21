import pathlib
from typing import Dict, Any
import yaml
from contextlib import suppress

languages: Dict[str, Any] = {}
languages_present: Dict[str, str] = {}

def get_string(lang: str, key: str) -> str:
    """
    Returns the translated string for the given language and key.
    """
    return languages[lang].get(key, f"Missing translation for key '{key}' in language '{lang}'")


base_path = pathlib.Path("./strings/langs/")

for filename in base_path.iterdir():
    if not filename.suffix == ".yml":
        continue

    lang_code = filename.stem
    if lang_code == "en":
        continue

    with filename.open(encoding="utf8") as f:
        lang_data = yaml.safe_load(f)

    languages.setdefault(lang_code, {})
    languages[lang_code].update(lang_data)

    try:
        languages_present[lang_code] = languages[lang_code]["name"]
    except KeyError:
        print(f"Warning: missing 'name' key in language data for '{lang_code}'")

    except KeyError:
        print(f"Warning: language '{lang_code}' not found in languages")
