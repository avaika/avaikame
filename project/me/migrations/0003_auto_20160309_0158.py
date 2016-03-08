# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command
import os

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'countries.json'


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    call_command('loaddata', fixture_file)


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20150907_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=150, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=150, verbose_name='Title')),
                ('flag', models.ImageField(upload_to=b'flags/', null=True, verbose_name=b'Country flag', blank=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='cities',
            field=models.ManyToManyField(to='me.City', verbose_name='Cities', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.ForeignKey(default=1, verbose_name='Country', to='me.Country'),
            preserve_default=False,
        ),
        migrations.RunPython(load_fixture),
    ]
