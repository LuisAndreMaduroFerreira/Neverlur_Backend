from django.db import models


class Song(models.Model):
    album = models.ForeignKey('Album', related_name='songs', on_delete=models.DO_NOTHING)
    artist = models.ForeignKey('Artist', related_name='songs', on_delete=models.DO_NOTHING, default="")
    title = models.CharField(max_length=200)
    total_duration_in_seconds = models.IntegerField()
    order_in_album = models.IntegerField()
    genres = models.ManyToManyField('Genre', through='Rendering')
    featured_artists = models.ManyToManyField('Artist', through='Feature')
    external_service_location_id = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['album', 'order_in_album']
        ordering = ['order_in_album']

    def __str__(self):
        return '%s' % self.title