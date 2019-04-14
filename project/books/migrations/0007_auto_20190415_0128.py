# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-14 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0021_auto_20190415_0045'),
        ('books', '0006_auto_20190415_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='country',
        ),
        migrations.AddField(
            model_name='book',
            name='countries',
            field=models.ManyToManyField(blank=True, null=True, to='travel.Country', verbose_name='Country'),
        ),
    ]
