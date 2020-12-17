# Generated by Django 3.1.3 on 2020-11-26 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Neverlur_Backend_API', '0005_auto_20201126_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='songs', to='Neverlur_Backend_API.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='songs', to='Neverlur_Backend_API.album'),
        ),
        migrations.RemoveField(
            model_name='song',
            name='featured_artists',
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Neverlur_Backend_API.artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Neverlur_Backend_API.song')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='featured_artists',
            field=models.ManyToManyField(through='Neverlur_Backend_API.Feature', to='Neverlur_Backend_API.Artist'),
        ),
    ]
