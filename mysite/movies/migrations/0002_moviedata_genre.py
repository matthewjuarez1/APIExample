# Generated by Django 4.1.3 on 2023-02-12 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='favorites', max_length=200),
        ),
    ]