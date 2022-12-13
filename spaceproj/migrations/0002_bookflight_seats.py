# Generated by Django 4.1.3 on 2022-12-11 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=50)),
                ('TotalSeats', models.CharField(max_length=200)),
                ('TotalPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeatName', models.CharField(blank=True, max_length=50)),
                ('Flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spaceproj.bookflight')),
            ],
        ),
    ]
