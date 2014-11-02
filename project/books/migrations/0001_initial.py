# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'books_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('wiki_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wiki_url_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'books', ['Author'])

        # Adding model 'Genre'
        db.create_table(u'books_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'books', ['Genre'])

        # Adding model 'Book'
        db.create_table(u'books_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('title_orig', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('wiki_url', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('wiki_url_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'books', ['Book'])

        # Adding M2M table for field author on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_author')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('author', models.ForeignKey(orm[u'books.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'books_author')

        # Deleting model 'Genre'
        db.delete_table(u'books_genre')

        # Deleting model 'Book'
        db.delete_table(u'books_book')

        # Removing M2M table for field author on 'Book'
        db.delete_table(db.shorten_name(u'books_book_author'))


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
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title_orig': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'wiki_url': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wiki_url_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'books.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['books']