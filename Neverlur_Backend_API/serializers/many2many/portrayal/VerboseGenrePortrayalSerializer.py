from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.artist_genre.Portrayal import Portrayal


class VerboseGenrePortrayalSerializer(serializers.ModelSerializer):
    genre_id = serializers.ReadOnlyField(source='genre.id')
    genre_name = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Portrayal
        fields = ('genre_id', 'genre_name')