# Generated by Django 2.2.17 on 2020-12-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lecturers", "0002_auto_20201130_1115"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecturer",
            name="id",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="HSR ID"
            ),
        ),
    ]
