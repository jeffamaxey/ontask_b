# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-11 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontask', '0001_action_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='content',
            field=models.TextField(blank=True, default='{% comment %}Your action content here{% endcomment %}'),
        ),
    ]