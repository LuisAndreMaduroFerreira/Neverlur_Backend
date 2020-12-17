from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.Genre import Genre
from Neverlur_Backend_API.serializers.model.genre.GenreSerializer import GenreSerializer
# from rest_framework import views


def listGenres(request):
        if request.method == 'GET':
            genres = Genre.objects.all()
            serializer = GenreSerializer(genres, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = GenreSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)