from django.db import models
from Neverlur_Backend_API.models.Song import Song
from Neverlur_Backend_API.models.Genre import Genre


# SongGenre
class Rendering(models.Model):
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre,  on_delete=models.DO_NOTHING)