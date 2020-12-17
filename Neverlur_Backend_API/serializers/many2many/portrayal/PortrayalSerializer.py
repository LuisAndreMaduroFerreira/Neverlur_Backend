from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.artist_genre.Portrayal import Portrayal


class PortrayalSerializer(serializers.ModelSerializer):
    genre_id = serializers.ReadOnlyField(source='genre.id')
    artist_id = serializers.ReadOnlyField(source='artist.id')

    class Meta:
        model = Portrayal
        fields = ('genre_id', 'artist_id')