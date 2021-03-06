# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-06 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False, verbose_name='Published?')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Creation time')),
                ('item', models.TextField(verbose_name='Item')),
                ('item_ru', models.TextField(null=True, verbose_name='Item')),
                ('item_en', models.TextField(null=True, verbose_name='Item')),
                ('link', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('link_ru', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('link_en', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('value', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('value_ru', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('value_en', models.TextField(blank=True, null=True, verbose_name='Value')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('comment_ru', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('comment_en', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('itemImage', models.ImageField(blank=True, null=True, upload_to=b'lists/', verbose_name=b'Title image')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('slug', models.CharField(max_length=150, verbose_name='List url')),
                ('description', models.TextField(blank=True, null=True, verbose_name='List description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='List description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='List description')),
                ('published', models.BooleanField(default=False, verbose_name='Publiished?')),
                ('listImage', models.ImageField(blank=True, upload_to=b'lists/', verbose_name=b'Title image')),
                ('fields', models.TextField(verbose_name='Fields')),
                ('fields_ru', models.TextField(null=True, verbose_name='Fields')),
                ('fields_en', models.TextField(null=True, verbose_name='Fields')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='listItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
