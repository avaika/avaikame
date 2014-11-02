# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ITTag'
        db.create_table(u'it_ittag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'it', ['ITTag'])

        # Adding model 'Post'
        db.create_table(u'it_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('titleImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('post', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('metaTitle', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('metaDesc', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'it', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name(u'it_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'it.post'], null=False)),
            ('ittag', models.ForeignKey(orm[u'it.ittag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'ittag_id'])


    def backwards(self, orm):
        # Deleting model 'ITTag'
        db.delete_table(u'it_ittag')

        # Deleting model 'Post'
        db.delete_table(u'it_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name(u'it_post_tags'))


    models = {
        u'it.ittag': {
            'Meta': {'object_name': 'ITTag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'it.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post'},
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metaDesc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'metaTitle': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['it.ITTag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'titleImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['it']