from src.core.observer import WeatherService


class DataWeather:

    def __init__(self, api_key: str) -> None:
        self.observer = WeatherService(api_key)

        self.data = {
            "city": ">> Выберите город <<",
            "temp": "_ _",
            "hum": "_ _",
            "pres": "_ _",
            "wind": "_ _"
        }

    def set_city(self, city: str) -> None:
        if city == "Введите город...":
            return

        weather = self.observer.request_weather_api(city)

        if weather is not None:

            self.data["city"] = weather["location"]["name"]
            self.data["temp"] = weather["current"]["temp_c"]
            self.data["hum"] = weather["current"]["humidity"]
            self.data["pres"] = round(weather["current"]["pressure_mb"] * 0.75006)
            self.data["wind"] = round(weather["current"]["wind_mph"] / 3.6)

    def get_weather(self) -> dict:
        return self.data

    def update(self): pass
