import json
import os.path


class DataSettings:
    def __init__(self) -> None:

        assert os.path.exists("src/gui/settings.json") is True, FileNotFoundError

        with open("src/gui/settings.json", "r", encoding="utf8") as settings_json:
            self.settings = json.load(settings_json)

        self._size_window = self.settings["size_window"]
        self._themes = self.settings["colors"]
        self._key = self.settings["key_api"]
        self._last_cities = self.settings["last_cities"]

    def get_size_window(self) -> str:
        return self._size_window

    def get_themes(self) -> list:
        return self._themes

    def get_key(self) -> str:
        return self._key

    def get_cities(self) -> list:
        return self._last_cities

    def update_cities(self, cities: [str]) -> None:

        assert os.path.exists("src/gui/settings.json") is True, FileNotFoundError

        self.settings["last_cities"] = cities

        with open("src/gui/settings.json", "w", encoding="utf8") as settings_json:
            json.dump(self.settings, settings_json)
