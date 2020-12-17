from django.http import JsonResponse, HttpResponse
from Neverlur_Backend_API.models.Genre import Genre
from Neverlur_Backend_API.serializers.model.genre.GenreSerializer import GenreSerializer


def listGenre(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return JsonResponse(serializer.data, safe=False)
