# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 20:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0012_auto_20181027_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solved',
            name='topic',
        ),
    ]
