# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-29 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ontask', '0032_auto_20180829_0939'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scheduledaction',
            unique_together=set([]),
        ),
    ]