from django.db import models
from Neverlur_Backend_API.models.Artist import Artist
from Neverlur_Backend_API.models.Song import Song


# Feature of an Artist in a Song
class Feature(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(Song,  on_delete=models.DO_NOTHING)