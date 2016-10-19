# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Post, Tag, Category
from tags_input import admin as tags_input_admin
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ['id', 'title']


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ['id', 'value']


class PostAdmin(tags_input_admin.TagsInputAdmin, TranslationAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'created', 'updated', 'draft', )
    list_editable = ('title', 'slug', 'draft', )
    search_fields = ['id', 'title', 'post', ]
    prepopulated_fields = {'slug': ['title']}
    save_as = True
    fieldsets = (
        ('Technical', {'fields': ('category', 'draft', )}),
        ('Titles', {'fields': ('title', 'slug', 'tags', )}),
        ('Post', {'fields': ('titleImage', 'titleImage_tag', 'post', 'sources', )}),
        ('Meta', {'fields': ('metaTitle', 'metaDesc', )}),
    )
    readonly_fields = ('titleImage_tag', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
