from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.song_genre.Rendering import Rendering


class VerboseSongRenderingSerializer(serializers.ModelSerializer):
    song_id = serializers.ReadOnlyField(source='artist.id')
    song_title = serializers.ReadOnlyField(source='artist.title')

    class Meta:
        model = Rendering
        fields = ('song_id', 'song_title')