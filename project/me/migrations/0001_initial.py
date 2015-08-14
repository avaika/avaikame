# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.me.models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('notifyEmail', models.EmailField(max_length=150, null=True, verbose_name='email for notifications', blank=True)),
                ('notifyGlobal', models.BooleanField(default=False, verbose_name='send global notifications')),
                ('notifyNewposts', models.BooleanField(default=False, verbose_name='send new posts notifications')),
                ('notifyReplied', models.BooleanField(default=False, verbose_name='send replied comments notifications')),
                ('registered', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-registered', 'id'),
                'get_latest_by': 'registered',
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headImage', models.ImageField(upload_to=project.me.models.headImagePath, blank=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('metaTitle', models.CharField(max_length=150, verbose_name='Meta title', blank=True)),
                ('metaDesc', models.CharField(max_length=150, verbose_name='Meta description', blank=True)),
            ],
            options={
                'ordering': ('-title',),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(verbose_name='Creation time', blank=True)),
                ('headImage', models.ImageField(upload_to=project.me.models.headImagePath, verbose_name=b'Head image 3863x1524', blank=True)),
                ('titleImage', models.ImageField(upload_to=project.me.models.imagePath, verbose_name=b'Title image 1980x1315', blank=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(max_length=150, verbose_name='Slug')),
                ('post', models.TextField(null=True, verbose_name='Post body', blank=True)),
                ('metaTitle', models.CharField(max_length=150, verbose_name='Meta title', blank=True)),
                ('metaDesc', models.CharField(max_length=150, verbose_name='Meta description', blank=True)),
                ('draft', models.BooleanField(default=True, verbose_name='Is draft')),
                ('mapSize', models.IntegerField(null=True, blank=True)),
                ('sources', models.TextField(null=True, verbose_name='Sources', blank=True)),
                ('author', models.ForeignKey(related_name='post_author', verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='Category', to='me.Category')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PostMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=150, verbose_name='Place')),
                ('order', models.IntegerField(null=True, blank=True)),
                ('post', models.ForeignKey(verbose_name='Post', to='me.Post')),
            ],
            options={
                'ordering': ('order', '-id'),
                'verbose_name': 'Post map direction',
                'verbose_name_plural': 'Post map directions',
            },
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True, verbose_name='Post body', blank=True)),
                ('photo', models.ImageField(upload_to=project.me.models.imagePath, blank=True)),
                ('panorama', models.BooleanField(default=False, verbose_name='Is panorama')),
                ('private', models.BooleanField(default=False, verbose_name='Is private')),
                ('photoRight', models.ImageField(upload_to=project.me.models.imagePath, blank=True)),
                ('panoramaRight', models.BooleanField(default=False, verbose_name='Is panorama')),
                ('privateRight', models.BooleanField(default=False, verbose_name='Is private')),
                ('post', models.ForeignKey(to='me.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=150, verbose_name='Title')),
                ('category', models.ForeignKey(verbose_name='Category', to='me.Category')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='me.Tag', verbose_name='Tags', blank=True),
        ),
    ]
