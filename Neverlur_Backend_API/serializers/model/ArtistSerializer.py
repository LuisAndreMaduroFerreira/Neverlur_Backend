from rest_framework import serializers
from Neverlur_Backend_API.models.Artist import Artist
from Neverlur_Backend_API.serializers.many2many.portrayal.VerboseGenrePortrayalSerializer\
    import VerboseGenrePortrayalSerializer


class ArtistSerializer(serializers.ModelSerializer):
    genres = VerboseGenrePortrayalSerializer(source='portrayal_set', many=True)

    class Meta:
        model = Artist
        fields = ['name', 'genres', 'artist_image', 'date_added']