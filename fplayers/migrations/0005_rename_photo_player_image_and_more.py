# Generated by Django 5.1.3 on 2024-12-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fplayers", "0004_rename_price_player_salary"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="photo",
            new_name="image",
        ),
        migrations.AlterField(
            model_name="player",
            name="date_of_birthday",
            field=models.DateField(
                blank=True, null=True, verbose_name="Date of birthday"
            ),
        ),
    ]
