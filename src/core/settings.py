import json
import os.path


class DataSettings:
    path_to_settings = "resource/config/settings.json"

    def __init__(self) -> None:

        assert os.path.exists(self.path_to_settings) is True, FileNotFoundError

        with open(self.path_to_settings, "r", encoding="utf8") as settings_json:
            self.settings = json.load(settings_json)

        self._size_window = self.settings["size_window"]
        self._themes = self.settings["colors"]
        self._key = self.settings["key_api"]
        self._favour_cities = self.settings["favour_cities"]

    def get_size_window(self) -> str:
        return self._size_window

    def get_themes(self) -> list:
        return self._themes

    def get_key(self) -> str:
        return self._key

    def get_cities(self) -> list:
        return self._favour_cities

    def add_city(self, city: [str]) -> None:

        assert os.path.exists(self.path_to_settings) is True, FileNotFoundError

        if city in self._favour_cities or city == ">> Выберите город <<":
            return

        self._favour_cities.append(city)

        self.settings["favour_cities"] = self._favour_cities

        with open(self.path_to_settings, "w", encoding="utf8") as settings_json:
            json.dump(self.settings, settings_json)

    def remove_city(self, city: str):

        assert os.path.exists(self.path_to_settings) is True, FileNotFoundError

        if city not in self._favour_cities:
            return

        self._favour_cities.remove(city)

        self.settings["favour_cities"] = self._favour_cities

        with open(self.path_to_settings, "w", encoding="utf8") as settings_json:
            json.dump(self.settings, settings_json)
