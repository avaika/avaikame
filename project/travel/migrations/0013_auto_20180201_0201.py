# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-31 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_country_psdfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmap',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mapSize',
        ),
        migrations.AddField(
            model_name='post',
            name='mapDirections',
            field=models.TextField(blank=True, null=True, verbose_name='Map link'),
        ),
        migrations.AlterField(
            model_name='country',
            name='psdfile',
            field=models.FileField(blank=True, null=True, upload_to=b'ball_psd/', verbose_name=b'PSD file'),
        ),
        migrations.DeleteModel(
            name='PostMap',
        ),
    ]
