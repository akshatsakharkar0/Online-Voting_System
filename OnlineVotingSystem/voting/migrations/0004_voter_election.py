# Generated by Django 5.1.4 on 2024-12-15 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0003_vote_candidate"),
    ]

    operations = [
        migrations.AddField(
            model_name="voter",
            name="election",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="voting.election",
            ),
        ),
    ]
