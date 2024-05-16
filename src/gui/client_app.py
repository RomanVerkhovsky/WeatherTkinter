from __future__ import annotations
from src.core.settings import DataSettings
from src.gui.factory.factories import IWidgetFactory, GreenFactory, GreyFactory
from src.core.testdataserver import DataWeather
from tkinter import *


# Главный класс-клиент для построения интерфейса и его конфигурации.
class ClientApp(Frame):

    settings = DataSettings()
    weather = DataWeather('2d8ccb3419bc4d9692f115020241105')

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

        # установка цвета окна
        self.root.config(background=self.factory.create_config().set_bgcolor())

        # наполнение

        # выбор темы
        cbox_theme = self.factory.create_combobox(values=self.themes)
        cbox_theme.get_tk_object().place(x=10, y=10)

        btn_choice_theme = self.factory.create_button(text="Выбрать тему",
                                                      click_handler=lambda:
                                                      self.change_theme(cbox_theme.get_tk_object().get()))
        btn_choice_theme.get_tk_object().place(x=160, y=10)

        # выбор города и обновление
        cbox_city = self.factory.create_combobox(values=["город"])
        cbox_city.get_tk_object().place(x=10, y=40)

        btn_choice_city = self.factory.create_button("Выбрать город",
                                                     click_handler=lambda:
                                                     (self.weather.set_city(cbox_city.get_tk_object().get()),
                                                      self.update_label()))
        btn_choice_city.get_tk_object().place(x=160, y=40)

        # запрос на обновление данных
        btn_update_info = self.factory.create_button("Обновить \nданные",
                                                     click_handler=lambda: self.update_label())
        btn_update_info.get_tk_object().place(x=290, y=20)

        # создание лейблов
        self.update_label()

    def update_label(self) -> None:
        self.factory.create_label(f"Температура: {self.weather.temp} С").get_tk_object().place(x=10, y=130)
        self.factory.create_label(f"Скорость ветра: {self.weather.wind} м/с").get_tk_object().place(x=10, y=200)
        self.factory.create_label(f"Давление: {self.weather.press} мм рт.ст.").get_tk_object().place(x=10, y=270)
        self.factory.create_label(f"Влажность: {self.weather.hum} %").get_tk_object().place(x=10, y=340)

    def run(self):
        self.mainloop()
