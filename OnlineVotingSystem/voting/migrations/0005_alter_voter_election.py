# Generated by Django 5.1.4 on 2024-12-15 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voting", "0004_voter_election"),
    ]

    operations = [
        migrations.AlterField(
            model_name="voter",
            name="election",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="voting.election",
            ),
        ),
    ]