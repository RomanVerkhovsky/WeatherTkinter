from __future__ import annotations
import requests
from abc import ABC, abstractmethod


# Интерфейс подписки
class ISubject(ABC):
    """
    Интерфейс субъекта, за которым будут наблюдать
    """

    @abstractmethod
    def add(self, observer: IReportObserver): pass

    @abstractmethod
    def remove(self, observer: IReportObserver): pass
    
    @abstractmethod
    def notify(self): pass


# Интерфейс сервиса
class IReportObserver(ABC):
    """
    Интерфейс передачи обновления отслеживаемой информации
    """
    
    @abstractmethod
    def update(self, user: ISubject): pass


# Интерфейс пользователя
class IUser(ABC):
    """
    Интерфейс пользователя для получения информации
    """

    @abstractmethod
    def set_info(self): pass


# Класс пользователя, реализует интерфейс пользователя и подписки
class WeatherService(ISubject, IUser):
    """
    Класс пользователя, реализует методы связи с подписками и передачи информации
    """

    def __init__(self, TOKEN) -> None:
        super().__init__()

        self.token = TOKEN
        self.weather_data = None
        self.__observers = []

    def add(self, observer: IReportObserver):

        assert isinstance(observer, IReportObserver)

        if observer in self.__observers: return

        self.__observers.append(observer)

    def remove(self, observer: IReportObserver):
        
        assert isinstance(observer, IReportObserver)

        if not (observer in self.__observers): return

        self.__observers.remove(observer)

    def notify(self):

        if len(self.__observers) == 0: return

        for observer in self.__observers:
            observer.update()

    def set_info(self, new_info):

        self.weather_data = new_info
        
    # Этот метод связывать с кнопкой обновить погоду
    def request_weather_api(self, city: str):
        return self.__get_weather(city)

        # Функция запроса через API
    def __get_weather(self, city_name):

        url = f"http://api.weatherapi.com/v1/current.json?key={self.token}&q={city_name}&aqi=no"

        try:
            response = requests.get(url, timeout=1, verify=True)

            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Fail retrieve weather data: {response.status_code} {response.text}")

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])

        except requests.exceptions.ReadTimeout as errrt:
            print("Time out")

        except requests.exceptions.ConnectionError as conerr:
            print("Connection error")

        except requests.exceptions.RequestException as errex:
            print("Exception request")
