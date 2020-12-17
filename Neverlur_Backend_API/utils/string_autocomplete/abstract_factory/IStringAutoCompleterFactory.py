from abc import ABC, abstractmethod
from typing import List


class IStringAutoCompleterFactory(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getStringAutoCompleter(self, data: dict, current_string: str):
        pass