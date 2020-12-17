from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.Song import Song
from Neverlur_Backend_API.serializers.model.song.SongSerializer import SongSerializer
# from rest_framework import views


def listSongs(request):
        if request.method == 'GET':
            songs = Song.objects.all()
            serializer = SongSerializer(songs, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = SongSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)