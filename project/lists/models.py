# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models


class List(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    slug = models.CharField(max_length=150, verbose_name=_("List url"))
    description = models.TextField(blank=True, null=True,
                                   verbose_name=_("List description"))
    published = models.BooleanField(default=False, blank=True,
                                    verbose_name=_("Publiished?"))
    listImage = models.ImageField(upload_to="lists/", blank=True,
                                  height_field=None, width_field=None,
                                  max_length=100, verbose_name="Title image")
    template = models.CharField(max_length=150, blank=True, null=True,
                                verbose_name=_("List template"))

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
    item = models.TextField(verbose_name=_("Short description"))
    link = models.TextField(blank=True, null=True, verbose_name=_("Link"))
    value = models.TextField(blank=True, null=True, verbose_name=_("Value"))
    comment = models.TextField(blank=True, null=True,
                               verbose_name=_("Comment"))
    itemImage = models.ImageField(upload_to="lists/", blank=True, null=True,
                                  height_field=None, width_field=None,
                                  max_length=100, verbose_name="Title image")
    ImageSource = models.TextField(blank=True, null=True, verbose_name=_("Image source"))

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")
        ordering = ('created',)

    def __unicode__(self):
        return self.item
