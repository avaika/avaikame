# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import User, Post, Tag, PostMap, Category, PostPhoto
from forms import UserCreationForm
# from project.adminfiles.admin import FilePickerAdmin
from tags_input import admin as tags_input_admin


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


class PostPhotoAdmin(admin.StackedInline):
    model = PostPhoto
    extra = 2


class PostAdmin(tags_input_admin.TagsInputAdmin):
    list_display = ('id', 'title', 'slug', 'category', 'created', 'draft')
    list_editable = ('title', 'slug', 'draft')
    search_fields = ['id', 'title', 'post']
    prepopulated_fields = {'slug': ['title']}
    adminfiles_fields = ('post',)
    # filter_horizontal = ('tags',)
    inlines = [MapInline, ]
    save_as = True
    inlines = [PostPhotoAdmin]


admin.site.register(User, ProfileUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
