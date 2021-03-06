# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-08 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0019_auto_20181007_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='Verified by editor'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Editor comment'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='comment_en',
            field=models.TextField(blank=True, null=True, verbose_name='Editor comment'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='comment_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Editor comment'),
        ),
    ]
