# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0010_auto_20181027_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemset',
            name='category',
        ),
        migrations.AlterField(
            model_name='solved',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=0),
        ),
        migrations.AlterField(
            model_name='solved',
            name='topic',
            field=models.CharField(choices=[('DP', 'Dynamic Programming'), ('GRAPH', 'Graph Theory'), ('STRING', 'String'), ('GEO', 'Geometry')], default='None', max_length=20),
        ),
    ]
