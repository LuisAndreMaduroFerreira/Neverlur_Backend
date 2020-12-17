from django.db import models


class Album(models.Model):
    artist = models.ForeignKey('Artist', related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_duration_in_seconds = models.IntegerField()
    album_cover = models.ImageField(default='../bass_clef.jpg')
    order_in_artist_discography = models.IntegerField()
    number_of_tracks = models.IntegerField()
    year_of_release = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['artist', 'order_in_artist_discography']
        ordering = ['order_in_artist_discography']

    def __str__(self):
        return '%s' % self.title