from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.features.Feature import Feature


class VerboseArtistFeatureSerializer(serializers.ModelSerializer):
    artist_id = serializers.ReadOnlyField(source='artist.id')
    artist_name = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Feature
        fields = ('artist_id', 'artist_name')