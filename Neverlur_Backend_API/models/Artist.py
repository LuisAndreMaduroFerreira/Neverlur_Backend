from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genres = models.ManyToManyField('Genre', through='Portrayal')
    artist_image = models.ImageField(default='../bass_clef.jpg')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name
