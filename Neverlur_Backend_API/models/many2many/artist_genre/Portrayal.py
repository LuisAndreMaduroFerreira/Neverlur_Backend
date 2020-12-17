from django.db import models
from Neverlur_Backend_API.models.Artist import Artist
from Neverlur_Backend_API.models.Genre import Genre


# ArtistGenre
class Portrayal(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre,  on_delete=models.DO_NOTHING)