from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.song_genre.Rendering import Rendering


class VerboseGenreRenderingSerializer(serializers.ModelSerializer):
    genre_id = serializers.ReadOnlyField(source='genre.id')
    genre_name = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Rendering
        fields = ('genre_id', 'genre_name')