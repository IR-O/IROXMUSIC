import pathlib
from typing import Dict, Any
import yaml
from contextlib import suppress

languages: Dict[str, Any] = {}
languages_present: Dict[str, str] = {}


def get_string(lang: str) -> str:
    return languages[lang]


base_path = pathlib.Path("./strings/langs/")

for filename in base_path.glob("*.yml"):
    lang_code = filename.stem
    if lang_code == "en":
        continue

    with filename.open(encoding="utf8") as f:
        lang_data = yaml.safe_load(f)

    languages.setdefault(lang_code, {})
    languages[lang_code] = {**languages["en"], **lang_data}

    with suppress(KeyError):
        languages_present[lang_code] = languages[lang_code]["name"]
