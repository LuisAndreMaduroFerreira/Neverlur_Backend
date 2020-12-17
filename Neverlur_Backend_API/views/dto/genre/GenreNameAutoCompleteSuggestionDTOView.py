from django.http import JsonResponse, Http404
# from rest_framework.parsers import JSONParser
# from rest_framework import views
from django.db.models import Q
from Neverlur_Backend_API.models.Genre import Genre
import itertools
from Neverlur_Backend_API.serializers.dto.genre.GenreNameSuggestionDTOSerializer\
    import GenreNameSuggestionDTOSerializer
from Neverlur_Backend_API.utils.string_autocomplete.concrete_factory.ConcreteStringLevenshteinAutoCompleterFactory\
    import ConcreteStringLevenshteinAutoCompleterFactory


def get_suggestion(request, current_string):
        if request.method == 'GET':
            # data = Genre.objects.values_list('name', flat=True)
            data = Genre.objects.filter(
                Q(name__contains=current_string)
            ).values_list('name', flat=True)
            data_list = list(data)
            # get factory for genre list of names extractor and another for the measuring
            # filter out names that do not match the suggestion, return
            dict_genres = dict.fromkeys(data_list, {})
            autocompleter_factory = ConcreteStringLevenshteinAutoCompleterFactory()
            autocompleter = autocompleter_factory.getStringAutoCompleter()
            autocomplete_result = autocompleter.autoComplete(dict_genres, current_string)
            print(autocomplete_result)
            recommended = itertools.chain(*autocomplete_result)
            recommended_objs = Genre.objects.filter(name__in=recommended)
            serializer = GenreNameSuggestionDTOSerializer(recommended_objs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return Http404('Service does not exist!')