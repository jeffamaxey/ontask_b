# Generated by Django 2.1.3 on 2018-12-08 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontask_oauth', '0002_auto_20181208_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ontaskoauthusertokens',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oauth2_token', to=settings.AUTH_USER_MODEL),
        ),
    ]
