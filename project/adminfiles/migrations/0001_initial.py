# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FileUpload'
        db.create_table(u'adminfiles_fileupload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('upload', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sub_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'adminfiles', ['FileUpload'])

        # Adding model 'FileUploadReference'
        db.create_table(u'adminfiles_fileuploadreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('upload', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adminfiles.FileUpload'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'adminfiles', ['FileUploadReference'])

        # Adding unique constraint on 'FileUploadReference', fields ['upload', 'content_type', 'object_id']
        db.create_unique(u'adminfiles_fileuploadreference', ['upload_id', 'content_type_id', 'object_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'FileUploadReference', fields ['upload', 'content_type', 'object_id']
        db.delete_unique(u'adminfiles_fileuploadreference', ['upload_id', 'content_type_id', 'object_id'])

        # Deleting model 'FileUpload'
        db.delete_table(u'adminfiles_fileupload')

        # Deleting model 'FileUploadReference'
        db.delete_table(u'adminfiles_fileuploadreference')


    models = {
        u'adminfiles.fileupload': {
            'Meta': {'object_name': 'FileUpload'},
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'adminfiles.fileuploadreference': {
            'Meta': {'unique_together': "(('upload', 'content_type', 'object_id'),)", 'object_name': 'FileUploadReference'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'upload': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['adminfiles.FileUpload']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['adminfiles']