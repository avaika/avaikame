# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-04 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20180204_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postphoto',
            name='private',
        ),
        migrations.RemoveField(
            model_name='postphoto',
            name='privateRight',
        ),
        migrations.AddField(
            model_name='postphoto',
            name='sourceRight',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Photo source'),
        ),
    ]
