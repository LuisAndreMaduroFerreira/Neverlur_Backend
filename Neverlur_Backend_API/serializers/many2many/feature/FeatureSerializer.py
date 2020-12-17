from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.features.Feature import Feature


class FeatureSerializer(serializers.ModelSerializer):
    song_id = serializers.ReadOnlyField(source='song.id')
    artist_id = serializers.ReadOnlyField(source='artist.id')

    class Meta:
        model = Feature
        fields = ('song_id', 'artist_id')