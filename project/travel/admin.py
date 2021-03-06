# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, PostPhoto, Country, PostLinks
from forms import UserCreationForm
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
    list_display = ('id', 'value', 'slug', 'country')
    list_editable = ('value', 'slug')
    search_fields = ['id', 'value', 'slug']


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title_en', 'title_en', 'worky', 'ready')
    list_editable = ('worky', 'ready')
    list_filter = ('worky', 'ready')
    search_fields = ['slug', 'title']


class PostPhotoAdmin(TranslationStackedInline):
    model = PostPhoto
    extra = 2
    fieldsets = (
        ('Text', {'fields': ('text', 'comment', )}),
        ('Photo', {'fields': ('photo', 'photo_tag', 'panorama', 'source')}),
        ('Photo Right', {'fields': ('photoRight', 'photoRight_tag', 'panoramaRight', 'sourceRight')}),
    )
    readonly_fields = ('photo_tag', 'photoRight_tag')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('photo', 'photoRight', 'photo_tag', 'photoRight_tag',
                    'text_ru', 'text_en', 'panorama', 'panoramaRight',
                    'source', 'sourceRight')
        else:
            return super(PostPhotoAdmin, self).get_readonly_fields(request, obj)


class PostLinksAdmin(TranslationStackedInline):
    model = PostLinks
    extra = 2
    fieldsets = (
        ('Text', {'fields': ('description', 'url')}),
        ('Photo Right', {'fields': ('isPoint', 'published')}),
    )


class PostAdmin(tags_input_admin.TagsInputAdmin, TranslationAdmin):
    list_display = ('id', 'title', 'slug', 'created', 'updated', 'draft',
                    'checked')
    list_editable = ('title', 'slug', 'draft')
    list_filter = ('checked', 'draft')
    search_fields = ['id', 'title', ]
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('updated')
    save_as = True
    inlines = [PostPhotoAdmin, PostLinksAdmin, ]
    raw_id_fields = ('country',)
    autocomplete_lookup_fields = {
        'fk': ['country'],
    }
    fieldsets = (
        ('Technical', {'fields': ('created', 'draft', 'checked')}),
        ('Titles', {'fields': ('title', 'slug', 'country', 'tags', )}),
        ('Post', {'fields': ('headImage', 'headImage_tag', 'titleImage',
                             'titleImage_tag', 'mapDirections', 'sources', )}),
        ('Meta', {'fields': ('metaDesc', )}),
    )
    readonly_fields = ('headImage_tag', 'titleImage_tag')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('created', 'draft',
                    'country', 'tags', 'headImage', 'titleImage',
                    'mapDirections', 'sources_en', 'sources_ru',
                    'title_en',
                    'headImage_tag', 'titleImage_tag',
                    'metaDesc_ru', 'metaDesc_en')
        else:
            return super(PostAdmin, self).get_readonly_fields(request, obj)


admin.site.register(User, ProfileUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Country, CountryAdmin)
