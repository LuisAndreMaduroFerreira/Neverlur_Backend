from django.http import JsonResponse, Http404
from django.db.models import Q
from Neverlur_Backend_API.models.Album import Album
from Neverlur_Backend_API.serializers.dto.album.AlbumSuggestionSongInfoSerializer\
    import AlbumSuggestionSongInfoSerializer


def getAlbumMatchSuggestions(request, current_string):
        if request.method == 'GET':
            recommended = Album.objects.filter(
                Q(title__contains=current_string)
            )
            serializer = AlbumSuggestionSongInfoSerializer(recommended, many=True)
            print(recommended)
            return JsonResponse(serializer.data, safe=False)
        else:
            return Http404('Service does not exist!')