# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-18 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0005_auto_20180911_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemset',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
