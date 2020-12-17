from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.Album import Album
from Neverlur_Backend_API.serializers.model.album.AlbumSerializer import AlbumSerializer
# from rest_framework import views


def listAlbums(request):
        if request.method == 'GET':
            albums = Album.objects.all()
            serializer = AlbumSerializer(albums, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AlbumSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)