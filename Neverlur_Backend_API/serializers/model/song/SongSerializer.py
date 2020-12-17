from rest_framework import serializers
from Neverlur_Backend_API.models.Song import Song
from Neverlur_Backend_API.serializers.many2many.rendering.VerboseGenreRenderingSerializer \
    import VerboseGenreRenderingSerializer
from Neverlur_Backend_API.serializers.many2many.feature.VerboseArtistFeatureSerializer \
    import VerboseArtistFeatureSerializer


class SongSerializer(serializers.ModelSerializer):
    genres = VerboseGenreRenderingSerializer(source='rendering_set', many=True)
    featured_artists = VerboseArtistFeatureSerializer(source='feature_set', many=True)

    class Meta:
        model = Song
        featured_artists = serializers.StringRelatedField(many=True, read_only=True)
        fields = ['id', 'title', 'album', 'artist', 'order_in_album', 'total_duration_in_seconds', 'genres',
                  'external_service_location_id', 'date_added', 'featured_artists']