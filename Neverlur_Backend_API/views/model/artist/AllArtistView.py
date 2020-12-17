from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.Artist import Artist
from Neverlur_Backend_API.serializers.model.ArtistSerializer import ArtistSerializer
# from rest_framework import views


def listArtists(request):
        if request.method == 'GET':
            artists = Artist.objects.all()
            serializer = ArtistSerializer(artists, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ArtistSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)