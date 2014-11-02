# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.year'
        db.add_column(u'books_book', 'year',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='0'),
                      keep_default=False)


        # Changing field 'Book.created'
        db.alter_column(u'books_book', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):
        # Deleting field 'Book.year'
        db.delete_column(u'books_book', 'year')


        # Changing field 'Book.created'
        db.alter_column(u'books_book', 'created', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'books.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'wiki_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wiki_url_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'books.book': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Book'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.Author']", 'symmetrical': 'False', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title_orig': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'wiki_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wiki_url_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'books.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['books']
