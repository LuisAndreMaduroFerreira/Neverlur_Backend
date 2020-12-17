from Neverlur_Backend_API.utils.string_autocomplete.abstract_factory.IStringAutoCompleterFactory \
    import IStringAutoCompleterFactory
from Neverlur_Backend_API.utils.string_autocomplete.concrete_strategy.ConcreteStringLevenshteinAutoCompleteStrategy \
    import ConcreteStringLevenshteinAutoCompleterStrategy
from typing import List
from Neverlur_Backend_API.utils.string_autocomplete.concrete_autocompleter.StringAutoCompleter \
    import StringAutoCompleter


class ConcreteStringLevenshteinAutoCompleterFactory(IStringAutoCompleterFactory):

    def __init__(self):
        super().__init__()

    def getStringAutoCompleter(self):
        #return and instance of ConcreteStringLevenshteinAutoCompleter with the strategy instance inside
        strategy = ConcreteStringLevenshteinAutoCompleterStrategy()
        result = StringAutoCompleter(strategy)
        return result

