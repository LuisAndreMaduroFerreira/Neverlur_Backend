from django.http import JsonResponse, Http404
from django.db.models import Q
from Neverlur_Backend_API.models.Genre import Genre
from Neverlur_Backend_API.serializers.dto.genre.GenreNameSuggestionDTOSerializer\
    import GenreNameSuggestionDTOSerializer


def getGenreMatchSuggestions(request, current_string):
        if request.method == 'GET':
            recommended = Genre.objects.filter(
                Q(name__contains=current_string)
            )
            serializer = GenreNameSuggestionDTOSerializer(recommended, many=True)
            print(recommended)
            return JsonResponse(serializer.data, safe=False)
        else:
            return Http404('Service does not exist!')