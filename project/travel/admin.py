# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, PostMap, PostPhoto,\
    Country, City
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


class TagAdmin(TranslationAdmin):
    list_display = ('id', 'value', 'slug')
    list_editable = ('value', 'slug')
    search_fields = ['id', 'value', 'slug']


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'worky', 'ready')
    search_fields = ['value']


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
    list_display = ('id', 'title', 'slug', 'created', 'updated', 'draft')
    list_editable = ('title', 'slug', 'draft')
    search_fields = ['id', 'title', ]
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('updated')
    save_as = True
    inlines = [PostPhotoAdmin, MapInline, ]
    raw_id_fields = ('country',)
    autocomplete_lookup_fields = {
        'fk': ['country'],
    }
    fieldsets = (
        ('Technical', {'fields': ('author', 'created', 'draft', 'mapSize',)}),
        ('Titles', {'fields': ('title', 'slug', 'country', 'cities', 'tags', )}),
        ('Post', {'fields': ('headImage', 'headImage_tag', 'titleImage', 'titleImage_tag', 'sources', )}),
        ('Meta', {'fields': ('metaTitle', 'metaDesc', )}),
    )
    readonly_fields = ('headImage_tag', 'titleImage_tag')

admin.site.register(User, ProfileUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City)
