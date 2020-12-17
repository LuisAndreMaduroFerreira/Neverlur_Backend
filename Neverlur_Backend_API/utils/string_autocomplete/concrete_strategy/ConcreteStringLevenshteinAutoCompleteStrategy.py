from Neverlur_Backend_API.utils.string_autocomplete.abstract_strategy.IAutoCompleteStrategy \
    import IAutoCompleteStrategy
from typing import List
from fast_autocomplete import AutoComplete


class ConcreteStringLevenshteinAutoCompleterStrategy(IAutoCompleteStrategy):

    def __init__(self):
        super().__init__()

    def execute_algorithm(self, data: dict, current_string: str):
        print(data)
        autocomplete = AutoComplete(words=data)
        print(autocomplete)
        # word -> what to search by, max_cost -> , size -> number of results to propagate back
        return autocomplete.search(word=current_string, max_cost=3, size=3)
        # might want to do a separate microservice, suggestion engine with machine learning

