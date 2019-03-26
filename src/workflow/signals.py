# -*- coding: utf-8 -*-

import logging

from django.db.models.signals import post_delete
from django.dispatch import receiver

from dataops import pandas_db
from workflow.models import Workflow

logger = logging.getLogger("project")


@receiver(post_delete, sender=Workflow)
def delete_data_frame_table(sender, instance, **kwargs):
    del sender
    del kwargs
    if instance.has_table():
        pandas_db.delete_table(instance.get_data_frame_table_name())