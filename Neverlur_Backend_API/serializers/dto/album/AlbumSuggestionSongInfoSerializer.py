from rest_framework import serializers
from Neverlur_Backend_API.models.Album import Album
from Neverlur_Backend_API.models.Song import Song
from Neverlur_Backend_API.serializers.model.song.SongSerializer import SongSerializer

# genres, song info (title, total_duration_in_seconds,
# order_in_album, genres, featured_artists, external_service_location_id,), album info (artist,
# title, total_duration_in_seconds, album_cover, number_of_tracks, year_of_release)


class AlbumSuggestionSongInfoSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'songs', 'total_duration_in_seconds',
                  'album_cover', 'number_of_tracks', 'year_of_release']