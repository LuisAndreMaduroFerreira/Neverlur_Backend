from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.artist_genre.Portrayal import Portrayal


class VerboseArtistPortrayalSerializer(serializers.ModelSerializer):
    artist_id = serializers.ReadOnlyField(source='artist.id')
    artist_name = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Portrayal
        fields = ('artist_id', 'artist_name')