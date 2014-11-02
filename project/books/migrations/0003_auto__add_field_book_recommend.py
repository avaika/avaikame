# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.recommend'
        db.add_column(u'books_book', 'recommend',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding M2M table for field genre on 'Book'
        m2m_table_name = db.shorten_name(u'books_book_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'books.book'], null=False)),
            ('genre', models.ForeignKey(orm[u'books.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'genre_id'])


    def backwards(self, orm):
        # Deleting field 'Book.recommend'
        db.delete_column(u'books_book', 'recommend')

        # Removing M2M table for field genre on 'Book'
        db.delete_table(db.shorten_name(u'books_book_genre'))


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
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['books.Genre']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'read': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recommend': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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