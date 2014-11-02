# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Book, Author, Genre
from tags_input import admin as tags_input_admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'wiki_url', 'wiki_url_en')
    list_editable = ('value', 'wiki_url', 'wiki_url_en')
    search_fields = ['id', 'value']


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ['id', 'value']


class BookAdmin(tags_input_admin.TagsInputAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'title_orig', 'wiki_url', 'wiki_url_en', 'read')
    list_editable = ('title', 'title_orig', 'wiki_url', 'wiki_url_en', 'read')
    search_fields = ['id', 'title', 'title_orig']
    # prepopulated_fields = {'slug': ['title']}
    # filter_horizontal = ('tags',)
    # save_as = True


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
