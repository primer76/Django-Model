# Generated by Django 4.1.2 on 2022-10-25 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0005_rename_artiste_song_artiste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicapp.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='Artiste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Musicapp.artiste'),
        ),
    ]
