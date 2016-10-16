# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_auto_20161013_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='ball',
            field=models.ImageField(blank=True, null=True, upload_to=b'balls/', verbose_name=b'Country ball'),
        ),
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='country',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='Ready?'),
        ),
        migrations.AddField(
            model_name='country',
            name='worky',
            field=models.BooleanField(default=False, verbose_name='Scheduled?'),
        ),
    ]