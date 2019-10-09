# Generated by Django 2.1.7 on 2019-03-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontask', '0025_auto_20190317_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(choices=[('string', 'string'), ('integer', 'integer'), ('double', 'double'), ('boolean', 'boolean'), ('datetime', 'datetime')], max_length=512, verbose_name='type of data to store in the column'),
        ),
    ]