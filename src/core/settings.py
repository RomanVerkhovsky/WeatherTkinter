import json
import os.path


class DataSettings:
    def __init__(self) -> None:

        assert os.path.exists("src/gui/settings.json") is True, FileNotFoundError

        with open("src/gui/settings.json", "r", encoding="utf-8") as settings_json:
            self.settings = json.load(settings_json)

        self._size_window = self.settings["size_window"]
        self._themes = self.settings["colors"]
        self._key = self.settings["key_api"]

    def get_size_window(self) -> str:
        return self._size_window

    def get_themes(self) -> list:
        return self._themes

    def get_key(self) -> str:
        return self._key
