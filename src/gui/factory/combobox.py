from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter.ttk


class AComboboxProduct(ABC):
    def __init__(self, values: list) -> None:
        self._values = values
        self._tk_object = self._configurate_object()

    @abstractmethod
    def _configurate_object(self) -> tkinter.ttk.Combobox: pass

    def get_tk_object(self) -> tkinter.ttk.Combobox:
        return self._tk_object


class GreenComboboxProduct(AComboboxProduct):
    def __init__(self, values: list) -> None:
        super().__init__(values)

    def _configurate_object(self) -> tkinter.ttk.Combobox:
        return tkinter.ttk.Combobox(values=self._values)


class GreyComboboxProduct(AComboboxProduct):
    def __init__(self, values: list) -> None:
        super().__init__(values)

    def _configurate_object(self) -> tkinter.ttk.Combobox:
        return tkinter.ttk.Combobox(values=self._values)

