# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20160219_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]