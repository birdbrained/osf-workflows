# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_auto_20170502_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='data',
            new_name='parameter',
        ),
        migrations.AlterField(
            model_name='case',
            name='initial_state',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='case',
            name='state',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
    ]