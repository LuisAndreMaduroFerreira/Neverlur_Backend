from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.many2many.artist_genre.Portrayal import Portrayal
from Neverlur_Backend_API.serializers.many2many.portrayal.PortrayalSerializer import PortrayalSerializer
# from rest_framework import views


def listPostrayals(request):
        if request.method == 'GET':
            portrayals = Portrayal.objects.all()
            serializer = PortrayalSerializer(portrayals, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PortrayalSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)