from abc import ABC, abstractmethod
from typing import List


class IAutoCompleteStrategy(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def execute_algorithm(self, data: dict, current_string: str):
        pass