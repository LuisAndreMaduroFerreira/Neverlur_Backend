from django.contrib import admin
from .models.Album import Album
from .models.Genre import Genre
from .models.Artist import Artist
from .models.Song import Song
from Neverlur_Backend_API.models.many2many.artist_genre.Portrayal import Portrayal
from Neverlur_Backend_API.models.many2many.song_genre.Rendering import Rendering
from Neverlur_Backend_API.models.many2many.features.Feature import Feature



admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Portrayal)
admin.site.register(Rendering)
admin.site.register(Feature)
