# Generated by Django 5.1.3 on 2024-12-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fplayers", "0006_alter_player_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="assists",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="player",
            name="goals",
            field=models.IntegerField(null=True),
        ),
    ]
