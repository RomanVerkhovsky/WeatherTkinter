from __future__ import annotations
from abc import ABC, abstractmethod
import tkinter


class AButtonProduct(ABC):
    def __init__(self, text: str, click_handler=None) -> None:
        self.text = text
        self._click_handler = click_handler
        self._tk_object = self._configurate_object()

    @abstractmethod
    def _configurate_object(self) -> tkinter.Button: pass

    def get_tk_object(self) -> tkinter.Button:
        return self._tk_object

    def _add_click(self):
        if self._click_handler is None:
            return

        self._click_handler()


class GreenButtonProduct(AButtonProduct):
    def __init__(self, text: str, click_handler=None) -> None:
        super().__init__(text, click_handler)

    def _configurate_object(self) -> tkinter.Button:
        return tkinter.Button(text=self.text, command=self._add_click)


class GreyButtonProduct(AButtonProduct):
    def __init__(self, text: str, click_handler=None) -> None:
        super().__init__(text, click_handler)

    def _configurate_object(self) -> tkinter.Button:
        return tkinter.Button(text=self.text, command=self._add_click)
