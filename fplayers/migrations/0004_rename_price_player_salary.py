# Generated by Django 5.1.3 on 2024-12-04 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fplayers", "0003_player_photo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="price",
            new_name="salary",
        ),
    ]
