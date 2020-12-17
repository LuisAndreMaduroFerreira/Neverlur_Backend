from rest_framework import serializers
from Neverlur_Backend_API.models.Album import Album


class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'date_added', 'songs']