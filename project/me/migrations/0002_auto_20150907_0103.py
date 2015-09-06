# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='metaDesc_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='metaDesc_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='metaTitle_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='metaTitle_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_en',
            field=models.TextField(null=True, verbose_name='Post body', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_ru',
            field=models.TextField(null=True, verbose_name='Post body', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sources_en',
            field=models.TextField(null=True, verbose_name='Sources', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sources_ru',
            field=models.TextField(null=True, verbose_name='Sources', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Post body', blank=True),
        ),
        migrations.AddField(
            model_name='postphoto',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Post body', blank=True),
        ),
    ]
