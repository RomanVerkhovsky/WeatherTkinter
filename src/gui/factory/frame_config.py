from __future__ import annotations
from abc import ABC, abstractmethod


class AConfigProduct(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def set_bgcolor(self) -> str:
        pass


class GreenConfigProduct(AConfigProduct):
    def __init__(self) -> None:
        super().__init__()

    def set_bgcolor(self) -> str:
        return "green"


class GreyConfigProduct(AConfigProduct):
    def __init__(self) -> None:
        super().__init__()

    def set_bgcolor(self) -> str:
        return "grey"
