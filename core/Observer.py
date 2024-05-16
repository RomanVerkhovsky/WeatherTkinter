from __future__ import annotations
import requests
from abc import ABC, abstractmethod

from config import TOKEN


# Интерфейс подписки
class ISubject(ABC):

    @abstractmethod
    def add(self, observer: IReportObserver):
        pass

    @abstractmethod
    def remove(self, observer: IReportObserver):
        pass

    def notify(self):
        pass


# Интерфейс сервиса
class IReportObserver(ABC):
    
    @abstractmethod
    def update(self, user: ISubject):
        pass


# Интерфейс пользователя
class IUser(ABC):

    @abstractmethod
    def get_info(self):
        pass


# Класс пользователя, реализует интерфейс пользователя и подписки
class User(ISubject, IUser):

    def __init__(self, city) -> None:
        super().__init__()
        self.city = city
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

    def get_info(self, new_info):
        self.weather_data = new_info
        

class ReportService(IReportObserver):

    def update(self, user: ISubject, ):
        api_key = TOKEN
        city_name = user.city

    # Типовой пример, надо дописать
        try:
            weather_data = self.__get_weather(city_name, api_key)
            print("Current Temperature:", weather_data['current']['temp_c'], "°C")
            user.get_info(weather_data)
            print('Info was delivered to user')
        except Exception as e:
            print(e)

        
    
    # Функция запроса через API
    def __get_weather(self, city_name, api_key):
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Fail retrieve weather data: {response.status_code} {response.text}")

def main(city):

    service = ReportService()

    app = User(city)
    app.add(service)

    service.update(app)

    print(app.weather_data)


city = 'Moscow'
main(city)