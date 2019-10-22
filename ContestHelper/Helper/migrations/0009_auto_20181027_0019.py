# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0008_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='solved',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='solved',
            name='topic',
            field=models.CharField(default='None', max_length=50),
        ),
    ]