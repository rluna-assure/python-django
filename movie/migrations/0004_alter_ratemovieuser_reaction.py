# Generated by Django 5.1.1 on 2024-09-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_ratemovieuser_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratemovieuser',
            name='reaction',
            field=models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=10),
        ),
    ]
