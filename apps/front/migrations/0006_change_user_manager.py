# Generated by Django 2.2.9 on 2020-03-05 22:55

import django.contrib.auth.models
from django.db import migrations

import apps.front.models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0005_remove_user_twitter"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("users", apps.front.models.CustomUserManager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
