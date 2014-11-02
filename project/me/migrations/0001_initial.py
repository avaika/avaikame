# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'me_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('notifyEmail', self.gf('django.db.models.fields.EmailField')(max_length=150, null=True, blank=True)),
            ('notifyGlobal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notifyNewposts', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notifyReplied', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('registered', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'me', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'me_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'me.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'me_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'me.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Tag'
        db.create_table(u'me_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'me', ['Tag'])

        # Adding model 'Post'
        db.create_table(u'me_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='post_author', to=orm['me.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('headImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('titleImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('post', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('metaTitle', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('metaDesc', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('draft', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mapSize', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal(u'me', ['Post'])

        # Adding M2M table for field tags on 'Post'
        m2m_table_name = db.shorten_name(u'me_post_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'me.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'me.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])

        # Adding model 'PostMap'
        db.create_table(u'me_postmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['me.Post'])),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'me', ['PostMap'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'me_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'me_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'me_user_user_permissions'))

        # Deleting model 'Tag'
        db.delete_table(u'me_tag')

        # Deleting model 'Post'
        db.delete_table(u'me_post')

        # Removing M2M table for field tags on 'Post'
        db.delete_table(db.shorten_name(u'me_post_tags'))

        # Deleting model 'PostMap'
        db.delete_table(u'me_postmap')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'me.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'post_author'", 'to': u"orm['me.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'headImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapSize': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'metaDesc': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'metaTitle': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'post': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['me.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'titleImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'me.postmap': {
            'Meta': {'ordering': "('order', '-id')", 'object_name': 'PostMap'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['me.Post']"})
        },
        u'me.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'me.user': {
            'Meta': {'ordering': "('-registered', 'id')", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'notifyEmail': ('django.db.models.fields.EmailField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'notifyGlobal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notifyNewposts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notifyReplied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'registered': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['me']
