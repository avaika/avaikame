# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from .models import List, Entry


class ListTranslationOptions(TranslationOptions):
        fields = ('name', 'description')


translator.register(List, ListTranslationOptions)


class EntryTranslationOptions(TranslationOptions):
        fields = ('item', 'link', 'value', 'comment')


translator.register(Entry, EntryTranslationOptions)
