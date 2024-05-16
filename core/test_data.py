import requests


class DataWeather:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.temp = "30"
        self.hum = "50"
        self.press = "4"
        self.wind = "5"
        self.get_weather("Dubai", api_key)

    def get_weather(self, city_name, api_key):
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            weather = response.json()
        else:
            raise Exception(f"Fail retrieve weather data: {response.status_code} {response.text}")

        self.temp = weather["current"]["temp_c"]
        self.hum = weather["current"]["humidity"]
        self.wind = round(weather["current"]["wind_mph"] / 3.6)
        self.press = round(weather["current"]["pressure_mb"] * 0.75006)

    def set_city(self, city: str):
        self.get_weather(city, self.api_key)
