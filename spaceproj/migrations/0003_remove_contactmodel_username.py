# Generated by Django 4.1.4 on 2022-12-12 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spaceproj', '0002_bookflight_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='UserName',
        ),
    ]
