# Generated by Django 2.2.4 on 2020-12-04 02:00

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0166_auto_20201202_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathonevent',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
