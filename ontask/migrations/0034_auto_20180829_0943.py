# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-29 00:13
from __future__ import unicode_literals

from django.db import migrations




class Migration(migrations.Migration):

    dependencies = [
        ('ontask', '0038_auto_20180826_1505'),
        ('ontask', '0033_auto_20180829_0940'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scheduledaction', unique_together={('name', 'action')}
        )
    ]
