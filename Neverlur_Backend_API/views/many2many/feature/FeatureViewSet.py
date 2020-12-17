from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from Neverlur_Backend_API.models.many2many.features.Feature import Feature
from Neverlur_Backend_API.serializers.many2many.feature.FeatureSerializer import FeatureSerializer
# from rest_framework import views


def listFeatures(request):
        if request.method == 'GET':
            features = Feature.objects.all()
            serializer = FeatureSerializer(features, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = FeatureSerializer(data=data)
            # check if serializer is valid
            if serializer.is_valid():
                serializer.save()
                # 201 Created status
                return JsonResponse(serializer.data, 201)
            # 400 bad request status
            return JsonResponse(serializer.errors, 400)