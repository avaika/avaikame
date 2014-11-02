# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
import uuid


class ITTag(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.value


def imagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_title_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%s" % (now.year, now.month, filename)


class Post(models.Model):
    created = models.DateTimeField(editable=True, blank=True, verbose_name=_("Creation time"))
    titleImage = models.ImageField(upload_to=imagePath, blank=True, height_field=None, width_field=None, max_length=100)
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    post = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    tags = models.ManyToManyField(ITTag, blank=True, verbose_name=_("Tags"))
    metaTitle = models.CharField(max_length=150, blank=True, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, blank=True, verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True, verbose_name=_("Is draft"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_redirect', kwargs={'pk': self.id})
