from __future__ import annotations
from abc import ABC, abstractmethod
from gui.factory.frame_config import AConfigProduct, GreenConfigProduct, GreyConfigProduct
from gui.factory.button import AButtonProduct, GreenButtonProduct, GreyButtonProduct
from gui.factory.label import ALabelProduct, GreenLabelProduct, GreyLabelProduct
from gui.factory.combobox import AComboboxProduct, GreenComboboxProduct, GreyComboboxProduct


class IWidgetFactory(ABC):
    @abstractmethod
    def create_config(self) -> AConfigProduct: pass

    @abstractmethod
    def create_label(self, text) -> ALabelProduct: pass

    @abstractmethod
    def create_button(self, text: str, click_handler=None) -> AButtonProduct: pass

    @abstractmethod
    def create_combobox(self, values: list = None) -> AComboboxProduct: pass


# Фабрика цвет зеленый
class GreenFactory(IWidgetFactory):

    def create_config(self) -> AConfigProduct:
        return GreenConfigProduct()

    def create_label(self, text) -> ALabelProduct:
        return GreenLabelProduct(text)

    def create_button(self, text: str, click_handler=None) -> AButtonProduct:
        return GreenButtonProduct(text, click_handler)

    def create_combobox(self, values: list = None) -> AComboboxProduct:
        return GreenComboboxProduct(values)


# Фабрика цвет серый
class GreyFactory(IWidgetFactory):

    def create_config(self) -> AConfigProduct:
        return GreyConfigProduct()

    def create_label(self, text: str) -> ALabelProduct:
        return GreyLabelProduct(text)

    def create_button(self, text, click_handler=None) -> AButtonProduct:
        return GreyButtonProduct(text, click_handler)

    def create_combobox(self, values: list = None) -> AComboboxProduct:
        return GreyComboboxProduct(values)