# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0009_auto_20170504_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='content',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='condition',
            name='state',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]