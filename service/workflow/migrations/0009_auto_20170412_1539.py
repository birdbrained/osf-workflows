# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_auto_20170412_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transition',
            name='view',
        ),
        migrations.AddField(
            model_name='message',
            name='view',
            field=models.TextField(blank=True, null=True),
        ),
    ]
