from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter


class ALabelProduct(ABC):
    def __init__(self, text) -> None:
        self.text = text
        self._tk_object = self._configurate_object()

    @abstractmethod
    def _configurate_object(self) -> tkinter.Label: pass

    def get_tk_object(self) -> tkinter.Label:
        return self._tk_object


class GreenLabelProduct(ALabelProduct):
    def __init__(self, text) -> None:
        super().__init__(text)

    def _configurate_object(self) -> tkinter.Label:
        return tkinter.Label(text=self.text, padx=10, pady=10, font=("Arial", 15, "bold"),
                             bg="white", bd=5, relief=tkinter.RAISED)


class GreyLabelProduct(ALabelProduct):
    def __init__(self, text) -> None:
        super().__init__(text)

    def _configurate_object(self) -> tkinter.Label:
        return tkinter.Label(text=self.text, padx=10, pady=10, font=("Arial", 15, "bold"),
                             bg="blue", bd=5, relief=tkinter.RAISED)
