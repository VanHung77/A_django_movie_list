# Generated by Django 4.2 on 2023-05-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailer_urls',
        ),
    ]
