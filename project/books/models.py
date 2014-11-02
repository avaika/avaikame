# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
# from django.core.urlresolvers import reverse
from django.db import models


class Author(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Author"))
    wiki_url = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url"))
    wiki_url_en = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url english"))

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __unicode__(self):
        return self.value


class Genre(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Genre"))

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __unicode__(self):
        return self.value


class Book(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name=_("Creation time"))
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    title_orig = models.CharField(max_length=250, verbose_name=_("Title in original language"))
    year = models.PositiveIntegerField(verbose_name=_("Year"))
    wiki_url = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url"))
    wiki_url_en = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url english"))
    about = models.TextField(blank=True, null=True, verbose_name=_("Short description about"))
    author = models.ManyToManyField(Author, blank=True, verbose_name=_("Author"))
    genre = models.ManyToManyField(Genre, blank=True, verbose_name=_("Genre"))
    recommend = models.BooleanField(default=False, blank=True, verbose_name=_("Do you recommend?"))
    read = models.BooleanField(default=False, blank=True, verbose_name=_("Did you read?"))

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title
