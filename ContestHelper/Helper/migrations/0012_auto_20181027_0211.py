# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-26 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helper', '0011_auto_20181027_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solved',
            name='topic',
            field=models.CharField(choices=[('NONE', 'NONE'), ('DP', 'Dynamic Programming'), ('GRAPH', 'Graph Theory'), ('STRING', 'String'), ('GEO', 'Geometry')], default='NONE', max_length=20),
        ),
    ]