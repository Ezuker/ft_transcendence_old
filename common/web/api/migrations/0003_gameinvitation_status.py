# Generated by Django 5.0.6 on 2024-07-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gameinvitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinvitation',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
