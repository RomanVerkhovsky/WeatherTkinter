from __future__ import annotations

import tkinter

from src.core.settings import DataSettings
from src.gui.factory.factories import IWidgetFactory, GreenFactory, GreyFactory
from src.core.observer import WeatherService
from tkinter import *


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


# Главный класс-клиент для построения интерфейса и его конфигурации.
class ClientApp(Frame):

    settings = DataSettings()
    weather = DataWeather(settings.get_key())
    # weather = WeatherService(settings.get_key())

    size_window = settings.get_size_window()
    title = 'Погода'

    root = Tk()
    root.geometry(size_window)
    root.title(title)
    root.resizable(width=False, height=False)

    def __init__(self, master=None) -> None:

        super().__init__(master)
        self.pack()

        self.themes = self.settings.get_themes()

        self.factory: IWidgetFactory = self.init_theme()

        self.build_widgets()

        self.app = None

    def init_theme(self, theme: str = None) -> IWidgetFactory():

        if theme is None: theme = self.themes[0]

        assert theme in self.themes, ValueError

        factory = None

        if theme == "зеленая":
            factory = GreenFactory()

        elif theme == "серая":
            factory = GreyFactory()

        return factory

    def change_theme(self, theme: str):

        if theme == "зеленая":
            self.factory = GreenFactory()

        elif theme == "серая":
            self.factory = GreyFactory()

        self.build_widgets()

    def build_widgets(self):

        # очистка фрейма
        for widget in self.root.winfo_children():
            widget.destroy()

        # установка цвета окна и меню
        menubar = tkinter.Menu()

        menu_theme = tkinter.Menu(menubar, tearoff=0)

        menu_theme.add_command(label="Зеленая", command=lambda: self.change_theme(theme="зеленая"))
        menu_theme.add_command(label="Серая", command=lambda: self.change_theme(theme="серая"))

        menubar.add_cascade(label="Тема", menu=menu_theme)

        self.root.config(background=self.factory.create_config().set_bgcolor(),
                         menu=menubar)

        # наполнение

        # выбор города и обновление
        cbox_city = self.factory.create_combobox()

        cbox_city.get_tk_object().place(x=10, y=15)

        btn_choice_city = self.factory.create_button("Выбрать",
                                                     click_handler=lambda:
                                                     (self.weather.set_city(cbox_city.get_tk_object().get()),
                                                      self.build_widgets()))

        btn_choice_city.get_tk_object().place(x=160, y=10)

        # запрос на обновление данных
        btn_update_info = self.factory.create_button("Обновить",
                                                     click_handler=lambda: self.build_widgets())
        btn_update_info.get_tk_object().place(x=230, y=10)

        # создание лейблов
        label_1 = self.factory.create_label(f"{self.weather.get_weather()['city']}")
        label_1.get_tk_object().place(relx=0.5, y=80, anchor=CENTER)

        label_2 = self.factory.create_label(f"Температура\n {self.weather.get_weather()['temp']}\N{DEGREE SIGN}")
        label_2.get_tk_object().place(relx=0.5, y=150, anchor=CENTER)

        label_3 = self.factory.create_label(f"Влажность\n {self.weather.get_weather()['hum']}%")
        label_3.get_tk_object().place(relx=0.5, y=250, anchor=CENTER)

        label_4 = self.factory.create_label(f"Ветер\n {self.weather.get_weather()['wind']} м/с")
        label_4.get_tk_object().place(relx=0.5, y=350, anchor=CENTER)

        label_5 = self.factory.create_label(f"Давление\n {self.weather.get_weather()['pres']} мм")
        label_5.get_tk_object().place(relx=0.5, y=450, anchor=CENTER)

    def run(self):
        self.mainloop()
