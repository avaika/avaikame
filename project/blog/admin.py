# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, PostMap
from forms import UserCreationForm
from project.adminfiles.admin import FilePickerAdmin
from tags_input import admin as tags_input_admin


class ProfileUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'notifyEmail')
    search_fields = ['id', 'username', 'first_name', 'last_name', 'notifyEmail']
    fieldsets = UserAdmin.fieldsets + (
        ('User data', {'fields': ('notifyEmail', )}),
    )
    add_form = UserCreationForm


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    search_fields = ['id', 'value']


class MapInline(admin.StackedInline):
    model = PostMap
    extra = 10
    max_num = 30
    fieldsets = (
        (None, {'fields': ('place', 'order')}),
    )


class PostAdmin(tags_input_admin.TagsInputAdmin, FilePickerAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'draft')
    list_editable = ('title', 'slug', 'draft')
    search_fields = ['id', 'title', 'post']
    prepopulated_fields = {'slug': ['title']}
    adminfiles_fields = ('post',)
    # filter_horizontal = ('tags',)
    inlines = [MapInline, ]
    save_as = True


admin.site.register(User, ProfileUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
