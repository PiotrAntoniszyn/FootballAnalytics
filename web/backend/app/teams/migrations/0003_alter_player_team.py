# Generated by Django 3.2.3 on 2021-05-27 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0002_alter_player_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="players",
                to="teams.team",
            ),
        ),
    ]
