# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    slug = models.CharField(max_length=150, verbose_name=_("List url"))
    parent = models.ForeignKey('self', blank=True, null=True)
    description = models.TextField(blank=True, null=True,
                                   verbose_name=_("List description"))
    published = models.BooleanField(default=False, blank=True,
                                    verbose_name=_("Publiished?"))
    listImage = models.ImageField(upload_to="lists/", blank=True,
                                  height_field=None, width_field=None,
                                  max_length=100, verbose_name="Title image")
    fields = models.TextField(verbose_name=_("Fields"))

    class Meta:
        verbose_name = _("List")
        verbose_name_plural = _("Lists")

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    listItem = models.ForeignKey(List)
    published = models.BooleanField(default=False, blank=True,
                                    verbose_name=_("Published?"))
    created = models.DateTimeField(auto_now=True,
                                   verbose_name=_("Creation time"))
    item = models.TextField(verbose_name=_("Item"))
    link = models.TextField(blank=True, null=True, verbose_name=_("Link"))
    value = models.TextField(blank=True, null=True, verbose_name=_("Value"))
    comment = models.TextField(blank=True, null=True,
                               verbose_name=_("Comment"))
    itemImage = models.ImageField(upload_to="lists/", blank=True, null=True,
                                  height_field=None, width_field=None,
                                  max_length=100, verbose_name="Title image")

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
        ordering = ('created',)

    def __unicode__(self):
        return self.title
