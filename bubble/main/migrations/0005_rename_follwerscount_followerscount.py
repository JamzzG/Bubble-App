# Generated by Django 4.2 on 2023-05-06 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_follwerscount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FollwersCount',
            new_name='FollowersCount',
        ),
    ]
