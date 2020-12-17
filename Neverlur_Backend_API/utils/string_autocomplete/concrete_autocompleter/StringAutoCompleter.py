from typing import List
from Neverlur_Backend_API.utils.string_autocomplete.abstract_strategy.IAutoCompleteStrategy \
    import IAutoCompleteStrategy


class StringAutoCompleter:
    def __init__(self, strategy: IAutoCompleteStrategy):
        self.strategy = strategy

    def autoComplete(self, data: dict, current_string: str):
        return self.strategy.execute_algorithm(data, current_string)
