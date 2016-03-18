# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from .models import Post, PostPhoto


class PostTranslationOptions(TranslationOptions):
        fields = ('title', 'post', 'metaTitle', 'metaDesc', 'sources', )
translator.register(Post, PostTranslationOptions)


class PostPhotoTranslationOptions(TranslationOptions):
        fields = ('text', )
translator.register(PostPhoto, PostPhotoTranslationOptions)
