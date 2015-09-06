# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, PostMap, Category, PostPhoto
from forms import UserCreationForm
# from project.adminfiles.admin import FilePickerAdmin
from tags_input import admin as tags_input_admin
from modeltranslation.admin import TranslationStackedInline, TranslationAdmin


class ProfileUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'notifyEmail')
    search_fields = ['id', 'username', 'first_name', 'last_name', 'notifyEmail']
    fieldsets = UserAdmin.fieldsets + (
        ('User data', {'fields': ('notifyEmail', )}),
    )
    add_form = UserCreationForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ['id', 'title']


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


class PostPhotoAdmin(TranslationStackedInline):
    model = PostPhoto
    extra = 2
    fieldsets = (
        ('Text', {'fields': ('text', )}),
        ('Photo', {'fields': ('photo', 'photo_tag', 'panorama', 'private')}),
        ('Photo Right', {'fields': ('photoRight', 'photoRight_tag', 'panoramaRight', 'privateRight')}),
    )
    readonly_fields = ('photo_tag', 'photoRight_tag')


class PostAdmin(tags_input_admin.TagsInputAdmin, TranslationAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'created', 'draft')
    list_editable = ('title', 'slug', 'draft')
    search_fields = ['id', 'title', 'post']
    prepopulated_fields = {'slug': ['title']}
    # adminfiles_fields = ('post',)
    # filter_horizontal = ('tags',)
    save_as = True
    inlines = [PostPhotoAdmin, MapInline, ]
    fieldsets = (
        ('Technical', {'fields': ('author', 'category', 'created', 'draft', 'mapSize',)}),
        ('Titles', {'fields': ('title', 'slug', 'tags', )}),
        ('Post', {'fields': ('headImage', 'headImage_tag', 'titleImage', 'titleImage_tag', 'sources', 'post')}),
    )
    readonly_fields = ('headImage_tag', 'titleImage_tag')

admin.site.register(User, ProfileUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
