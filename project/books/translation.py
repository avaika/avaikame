# -*- coding: utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from .models import Author, Genre, Book


class AuthorTranslationOptions(TranslationOptions):
        fields = ('value', 'wiki_url')
translator.register(Author, AuthorTranslationOptions)


class GenreTranslationOptions(TranslationOptions):
        fields = ('value', )
translator.register(Genre, GenreTranslationOptions)


class BookTranslationOptions(TranslationOptions):
        fields = ('title', 'wiki_url', 'about', 'down_url')
translator.register(Book, BookTranslationOptions)
