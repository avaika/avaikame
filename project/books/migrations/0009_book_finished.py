# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-27 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20190522_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='finished',
            field=models.DateTimeField(null=True, verbose_name='Read time'),
        ),
    ]
