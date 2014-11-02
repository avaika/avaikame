# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Post, ITTag
from tags_input import admin as tags_input_admin


class ITTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ['id', 'value']


class PostAdmin(tags_input_admin.TagsInputAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'draft')
    list_editable = ('title', 'slug', 'draft')
    search_fields = ['id', 'title', 'post']
    prepopulated_fields = {'slug': ['title']}
    adminfiles_fields = ('post',)
    save_as = True


admin.site.register(ITTag, ITTagAdmin)
admin.site.register(Post, PostAdmin)
