# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime
import uuid


class User(AbstractUser):
    notifyEmail = models.EmailField(max_length=150, blank=True, null=True, verbose_name=_("email for notifications"))
    notifyGlobal = models.BooleanField(default=False, verbose_name=_("send global notifications"))
    notifyNewposts = models.BooleanField(default=False, verbose_name=_("send new posts notifications"))
    notifyReplied = models.BooleanField(default=False, verbose_name=_("send replied comments notifications"))
    registered = models.DateTimeField(auto_now=True, editable=False, verbose_name="Время регистрации")

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('-registered', 'id')
        get_latest_by = 'registered'

    def __unicode__(self):
        return unicode(self.username)


class Tag(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.value


def headImagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_head_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%s" % (now.year, now.month, filename)


def imagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_title_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%s" % (now.year, now.month, filename)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', verbose_name=_("Author"))
    # created = models.DateTimeField(auto_now=True, editable=True, blank=True, verbose_name=_("Creation time"))
    created = models.DateTimeField(editable=True, blank=True, verbose_name=_("Creation time"))
    headImage = models.ImageField(upload_to=headImagePath, blank=True, height_field=None, width_field=None, max_length=100)
    titleImage = models.ImageField(upload_to=imagePath, blank=True, height_field=None, width_field=None, max_length=100)
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    post = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))
    metaTitle = models.CharField(max_length=150, blank=True, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, blank=True, verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True, verbose_name=_("Is draft"))
    mapSize = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey(Site, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_redirect', kwargs={'pk': self.id})


class PostMap(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("Post"))
    place = models.CharField(max_length=150, verbose_name=_("Place"))
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Post map direction")
        verbose_name_plural = _("Post map directions")
        ordering = ('order', '-id')

    def __unicode__(self):
        return self.place
