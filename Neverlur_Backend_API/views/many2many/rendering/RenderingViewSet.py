from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.many2many.song_genre.Rendering import Rendering
from Neverlur_Backend_API.serializers.many2many.rendering.RenderingSerializer import RenderingSerializer


def listRenderings(request):
        if request.method == 'GET':
            renderings = Rendering.objects.all()
            serializer = RenderingSerializer(renderings, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = RenderingSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)