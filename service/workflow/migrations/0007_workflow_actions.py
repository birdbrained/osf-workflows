# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20170502_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='actions',
            field=models.ManyToManyField(related_name='workflows', to='workflow.Action'),
        ),
    ]
