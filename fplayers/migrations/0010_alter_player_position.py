# Generated by Django 5.1.3 on 2024-12-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fplayers", "0009_alter_player_assists_alter_player_firstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="position",
            field=models.CharField(max_length=150),
        ),
    ]
