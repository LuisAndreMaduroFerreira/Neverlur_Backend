from rest_framework import serializers
from Neverlur_Backend_API.models.many2many.features.Feature import Feature


class VerboseSongFeatureSerializer(serializers.ModelSerializer):
    song_id = serializers.ReadOnlyField(source='song.id')
    song_title = serializers.ReadOnlyField(source='song.title')

    class Meta:
        model = Feature
        fields = ('song_id', 'song_title')