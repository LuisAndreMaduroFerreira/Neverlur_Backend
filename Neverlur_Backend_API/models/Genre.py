from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField('Artist', through='Portrayal')
    songs = models.ManyToManyField('Song', through='Rendering')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name