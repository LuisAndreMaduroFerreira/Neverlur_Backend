from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.song_genre.Rendering import Rendering


class RenderingSerializer(serializers.ModelSerializer):
    genre_id = serializers.ReadOnlyField(source='genre.id')
    song_id = serializers.ReadOnlyField(source='song.id')

    class Meta:
        model = Rendering
        fields = ('genre_id', 'song_id')