# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180829_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='edited',
        ),
        migrations.DeleteModel(
            name='EditHistoryGeneric',
        ),
    ]