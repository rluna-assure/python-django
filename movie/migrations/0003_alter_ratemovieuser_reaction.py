# Generated by Django 5.1.1 on 2024-09-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_remove_movie_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratemovieuser',
            name='reaction',
            field=models.CharField(max_length=10),
        ),
    ]