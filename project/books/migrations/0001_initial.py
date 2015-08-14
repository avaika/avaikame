# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=150, verbose_name='Author')),
                ('wiki_url', models.TextField(null=True, verbose_name='Wikipedia url', blank=True)),
                ('wiki_url_en', models.TextField(null=True, verbose_name='Wikipedia url english', blank=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Creation time')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('title_orig', models.CharField(max_length=250, verbose_name='Title in original language')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('wiki_url', models.TextField(null=True, verbose_name='Wikipedia url', blank=True)),
                ('wiki_url_en', models.TextField(null=True, verbose_name='Wikipedia url english', blank=True)),
                ('about', models.TextField(null=True, verbose_name='Short description about', blank=True)),
                ('recommend', models.BooleanField(default=False, verbose_name='Do you recommend?')),
                ('read', models.BooleanField(default=False, verbose_name='Did you read?')),
                ('author', models.ManyToManyField(to='books.Author', verbose_name='Author', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=150, verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='books.Genre', verbose_name='Genre', blank=True),
        ),
    ]
