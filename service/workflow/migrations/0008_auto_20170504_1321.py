# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_workflow_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to='workflow.Action'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='actions',
            field=models.ManyToManyField(blank=True, null=True, related_name='workflows', to='workflow.Action'),
        ),
    ]
