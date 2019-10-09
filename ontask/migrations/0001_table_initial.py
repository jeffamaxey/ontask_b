# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 02:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontask', '0013_auto_20171209_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description_text', models.CharField(blank=True, default='', max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('filter', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Preselect rows satisfying this condition', null=True)),
                ('columns', models.ManyToManyField(related_name='views', to='ontask.Column')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='ontask.Workflow')),
            ],
        ),
    ]