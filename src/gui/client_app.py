from __future__ import annotations

import tkinter

from src.core.settings import DataSettings
from src.core.data_weather import DataWeather
from src.gui.factory.factories import IWidgetFactory, GreenFactory, GreyFactory
from tkinter import *


# Главный класс-клиент для построения интерфейса и его конфигурации.
class ClientApp(Frame):

    settings = DataSettings()
    weather = DataWeather(settings.get_key())

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

        menubar.add_cascade(label="Настройки", menu=menu_theme)

        self.root.config(background=self.factory.create_config().set_bgcolor(),
                         menu=menubar)

        # наполнение

        # выбор города и обновление
        cbox_city = self.factory.create_combobox(values=self.settings.get_cities())

        cbox_city.get_tk_object().place(x=60, y=100)

        btn_choice_city = self.factory.create_button("Выбрать город",
                                                     click_handler=lambda:
                                                     (self.weather.set_city(cbox_city.get_tk_object().get()),
                                                      self.build_widgets()))

        btn_choice_city.get_tk_object().place(x=220, y=100)

        # Добавление и удаление в избранное
        btn_add_favour = self.factory.create_button("Добавить\nв избранное ",
                                                    click_handler=lambda:
                                                    self.add_favour(self.weather.get_weather()['city']))

        btn_add_favour.get_tk_object().place(x=10, y=5)

        btn_del_favour = self.factory.create_button("Удалить\nиз избранного",
                                                    click_handler=lambda:
                                                    self.del_favour(cbox_city.get_tk_object().get()))

        btn_del_favour.get_tk_object().place(x=110, y=5)

        # запрос на обновление данных
        btn_update_info = self.factory.create_button("Обновить\nданные",
                                                     click_handler=lambda: self.build_widgets())
        btn_update_info.get_tk_object().place(x=320, y=5)

        # создание лейблов
        label_1 = self.factory.create_label(f"{self.weather.get_weather()['city']}")
        label_1.get_tk_object().place(relx=0.5, y=200, anchor=CENTER)

        label_2 = self.factory.create_label(f"Температура\n {self.weather.get_weather()['temp']}\N{DEGREE SIGN}")
        label_2.get_tk_object().place(relx=0.5, y=300, anchor=CENTER)

        label_3 = self.factory.create_label(f"Влажность\n {self.weather.get_weather()['hum']}%")
        label_3.get_tk_object().place(relx=0.5, y=400, anchor=CENTER)

        label_4 = self.factory.create_label(f"Ветер\n {self.weather.get_weather()['wind']} м/с")
        label_4.get_tk_object().place(relx=0.5, y=500, anchor=CENTER)

        label_5 = self.factory.create_label(f"Давление\n {self.weather.get_weather()['pres']} мм")
        label_5.get_tk_object().place(relx=0.5, y=600, anchor=CENTER)

    def add_favour(self, city: str):
        self.settings.add_city(city)
        self.build_widgets()

    def del_favour(self, city: str):
        self.settings.remove_city(city)
        self.build_widgets()

    def run(self):
        self.mainloop()
