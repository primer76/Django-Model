# Generated by Django 4.1.2 on 2022-10-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0002_alter_song_date_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.IntegerField(),
        ),
    ]
