from rest_framework import serializers
from Neverlur_Backend_API.models.Genre import Genre
from Neverlur_Backend_API.serializers.many2many.portrayal.VerboseArtistPortrayalSerializer\
    import VerboseArtistPortrayalSerializer
from Neverlur_Backend_API.serializers.many2many.rendering.VerboseSongRenderingSerializer\
    import VerboseSongRenderingSerializer


class GenreSerializer(serializers.ModelSerializer):
    artists = VerboseArtistPortrayalSerializer(source='portrayal_set', many=True)
    songs = VerboseSongRenderingSerializer(source='rendering_set', many=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'date_added', 'artists', 'songs']