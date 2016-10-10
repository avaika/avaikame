# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Book, Author, Genre
from tags_input import admin as tags_input_admin
from modeltranslation.admin import TranslationAdmin


class AuthorAdmin(TranslationAdmin):
    list_display = ('id', 'value', 'wiki_url')
    list_editable = ('value', 'wiki_url')
    search_fields = ['id', 'value']


class GenreAdmin(TranslationAdmin):
    list_display = ('id', 'value')
    search_fields = ['id', 'value']


class BookAdmin(tags_input_admin.TagsInputAdmin, TranslationAdmin):
    list_display = ('id', 'title', 'wiki_url', 'read')
    list_editable = ('title', 'wiki_url', 'read')
    search_fields = ['id', 'title']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
