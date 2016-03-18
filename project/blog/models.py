# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    metaTitle = models.CharField(max_length=150, blank=True, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, blank=True, verbose_name=_("Meta description"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('-title',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.id})


class Tag(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.value


class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    created = models.DateTimeField(editable=True, blank=True, verbose_name=_("Creation time"))
    titleImage = models.ImageField(upload_to="blog_posts/", blank=True, height_field=None,
                                   width_field=None, max_length=100,
                                   verbose_name="Title image")
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    post = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))
    metaTitle = models.CharField(max_length=150, blank=True, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, blank=True, verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True, verbose_name=_("Is draft"))
    sources = models.TextField(blank=True, null=True, verbose_name=_("Sources"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_redirect', kwargs={'pk': self.id})

    def titleImage_tag(self):
        if self.titleImage:
            return u'<img src="/media/%s" height="100px" />' % self.titleImage
        else:
            return
    titleImage_tag.short_description = 'Image'
    titleImage_tag.allow_tags = True
