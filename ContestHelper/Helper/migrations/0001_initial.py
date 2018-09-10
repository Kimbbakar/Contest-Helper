# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-10 17:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='sectioninfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sectionlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField()),
                ('section', models.ForeignKey(default='00001', on_delete=django.db.models.deletion.CASCADE, related_name='info', to='Helper.sectioninfo')),
            ],
        ),
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='userinfo', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('uva', models.CharField(max_length=20)),
                ('school', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='sectionlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sectioninfo',
            name='user',
            field=models.ForeignKey(default='00001', on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
