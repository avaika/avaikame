# -*- coding: utf-8 -*-
from django.contrib import admin
from models import List, Entry
from modeltranslation.admin import TranslationAdmin


class ListAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'slug')
    list_editable = ('name', 'slug')
    search_fields = ['id', 'name', 'slug', 'description']


class EntryAdmin(TranslationAdmin):
    list_display = ('id', 'listItem', 'item', 'created', 'published')
    search_fields = ['id', 'item', 'value']
    list_filter = ('listItem', 'published')


admin.site.register(List, ListAdmin)
admin.site.register(Entry, EntryAdmin)
