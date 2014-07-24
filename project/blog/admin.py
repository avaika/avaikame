# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, Comment, PostMap
from forms import UserCreationForm
from project.adminfiles.admin import FilePickerAdmin


class ProfileUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'notifyEmail')
    search_fields = ['id', 'username', 'first_name', 'last_name', 'notifyEmail']
    fieldsets = UserAdmin.fieldsets + (
        ('User data', {'fields': ('notifyEmail', )}),
    )
    add_form = UserCreationForm


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tagType', 'value')
    list_filter = ('tagType',)
    search_fields = ['id', 'value']


class MapInline(admin.StackedInline):
    model = PostMap
    extra = 10
    max_num = 30
    fieldsets = (
        (None, {'fields': ('place', 'order')}),
    )


class PostAdmin(FilePickerAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'draft')
    search_fields = ['id', 'title', 'post']
    prepopulated_fields = {'slug': ['title']}
    adminfiles_fields = ('post',)
    filter_horizontal = ('tags',)
    inlines = [MapInline, ]
    save_as = True


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created')
    list_filter = ('author', 'post')
    search_fields = ['id', 'author', 'text']


admin.site.register(User, ProfileUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
