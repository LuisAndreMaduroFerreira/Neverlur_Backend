from rest_framework import serializers
from Neverlur_Backend_API.models.Genre import Genre


class GenreNameSuggestionDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']