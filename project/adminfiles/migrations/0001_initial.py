# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.adminfiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='upload date')),
                ('upload', models.FileField(upload_to=project.adminfiles.models.imagePath, verbose_name='file')),
                ('content_type', models.CharField(max_length=100, editable=False)),
                ('sub_type', models.CharField(max_length=100, editable=False)),
            ],
            options={
                'verbose_name': 'file upload',
                'verbose_name_plural': 'file uploads',
            },
        ),
        migrations.CreateModel(
            name='FileUploadReference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('upload', models.ForeignKey(to='adminfiles.FileUpload')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='fileuploadreference',
            unique_together=set([('upload', 'content_type', 'object_id')]),
        ),
    ]
