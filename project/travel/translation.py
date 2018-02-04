# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from .models import Post, PostPhoto, Tag, PostLinks


class PostTranslationOptions(TranslationOptions):
        fields = ('title', 'metaTitle', 'metaDesc', 'sources', )
translator.register(Post, PostTranslationOptions)


class PostPhotoTranslationOptions(TranslationOptions):
        fields = ('text', )
translator.register(PostPhoto, PostPhotoTranslationOptions)


class PostLinksTranslationOptions(TranslationOptions):
        fields = ('description', 'url')
translator.register(PostLinks, PostLinksTranslationOptions)


class TagTranslationOptions(TranslationOptions):
        fields = ('value', )
translator.register(Tag, TagTranslationOptions)
