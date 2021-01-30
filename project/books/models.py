# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
# from django.core.urlresolvers import reverse
from django.db import models
from ..travel.models import Country


class Author(models.Model):
    value = models.CharField(max_length=150, null=True, verbose_name=_("Author"))
    wiki_url = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url"))

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __unicode__(self):
        return self.value


class Genre(models.Model):
    value = models.CharField(max_length=150, null=True, verbose_name=_("Genre"))

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __unicode__(self):
        return self.value


class Book(models.Model):
    created = models.DateTimeField(auto_now=True, verbose_name=_("Creation time"))
    finished = models.DateTimeField(null=True, verbose_name=_("Read time"))
    title = models.CharField(max_length=250, null=True, verbose_name=_("Title"))
    year = models.PositiveIntegerField(verbose_name=_("Year"))
    wiki_url = models.TextField(blank=True, null=True, verbose_name=_("Wikipedia url"))
    about = models.TextField(blank=True, null=True, verbose_name=_("Short description about"))
    author = models.ManyToManyField(Author, blank=True, verbose_name=_("Author"))
    genre = models.ManyToManyField(Genre, blank=True, verbose_name=_("Genre"))
    recommend = models.BooleanField(default=False, blank=True, verbose_name=_("Do you recommend?"))
    read = models.BooleanField(default=False, blank=True, verbose_name=_("Did you read?"))
    source = models.TextField(blank=True, null=True, verbose_name=_("Where I found the book from?"))
    down_url = models.TextField(blank=True, null=True, verbose_name=_("Download url"))
    countries = models.ManyToManyField(Country, blank=True, verbose_name=_("Country"))
    active = models.BooleanField(default=False, blank=True, verbose_name=_("Is active?"))

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ('-finished',)

    def __unicode__(self):
        return self.title
