# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from .models import Post, PostPhoto, Tag, PostLinks, Country


class PostTranslationOptions(TranslationOptions):
        fields = ('title', 'metaDesc', 'sources', )
translator.register(Post, PostTranslationOptions)


class PostPhotoTranslationOptions(TranslationOptions):
        fields = ('text', 'comment',)
translator.register(PostPhoto, PostPhotoTranslationOptions)


class PostLinksTranslationOptions(TranslationOptions):
        fields = ('description', 'url')
translator.register(PostLinks, PostLinksTranslationOptions)


class TagTranslationOptions(TranslationOptions):
        fields = ('value', )
translator.register(Tag, TagTranslationOptions)

class CountryTranslationOptions(TranslationOptions):
        fields = ('title', )
translator.register(Country, CountryTranslationOptions)
