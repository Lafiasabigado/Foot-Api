# Generated by Django 5.1.3 on 2024-12-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fplayers", "0008_rename_surname_player_firstname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="assists",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="player",
            name="firstname",
            field=models.CharField(max_length=300, verbose_name="Surname"),
        ),
        migrations.AlterField(
            model_name="player",
            name="goals",
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name="player",
            name="lastname",
            field=models.CharField(max_length=300, verbose_name="Lastname"),
        ),
        migrations.AlterField(
            model_name="player",
            name="salary",
            field=models.IntegerField(default=70000),
        ),
    ]
