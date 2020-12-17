# Generated by Django 3.1.3 on 2020-11-26 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('artist_image', models.ImageField(default='../bass_clef.jpg', upload_to='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portrayal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Neverlur_Backend_API.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Neverlur_Backend_API.genre')),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='artists',
            field=models.ManyToManyField(through='Neverlur_Backend_API.Portrayal', to='Neverlur_Backend_API.Artist'),
        ),
        migrations.AddField(
            model_name='artist',
            name='genres',
            field=models.ManyToManyField(through='Neverlur_Backend_API.Portrayal', to='Neverlur_Backend_API.Genre'),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('total_duration_in_seconds', models.IntegerField()),
                ('total_duration_in_minutes', models.FloatField()),
                ('album_cover', models.ImageField(default='../bass_clef.jpg', upload_to='')),
                ('order_in_artist_discography', models.IntegerField()),
                ('number_of_tracks', models.IntegerField()),
                ('year_of_release', models.IntegerField()),
                ('location_folder_path', models.CharField(max_length=150)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='Neverlur_Backend_API.artist')),
            ],
            options={
                'ordering': ['order_in_artist_discography'],
                'unique_together': {('artist', 'order_in_artist_discography')},
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('total_duration_in_seconds', models.IntegerField()),
                ('total_duration_in_minutes', models.FloatField()),
                ('order_in_album', models.IntegerField()),
                ('location_path', models.CharField(max_length=150)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='Neverlur_Backend_API.album')),
                ('featured_artists', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='featured_artists', to='Neverlur_Backend_API.artist')),
                ('genres', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Neverlur_Backend_API.genre')),
            ],
            options={
                'ordering': ['order_in_album'],
                'unique_together': {('album', 'order_in_album')},
            },
        ),
    ]
