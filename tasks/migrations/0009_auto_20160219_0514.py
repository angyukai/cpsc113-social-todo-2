# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_collabemails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='collaborators',
            field=models.ManyToManyField(to='tasks.CollabEmails'),
        ),
    ]
