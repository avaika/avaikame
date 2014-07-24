# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
import uuid


TAG_CHOICES = (
    ('TCI', _("Travel city")),
    ('TCO', _("Travel country")),
    ('ITT', _("IT technology")),
    ('ITS', _("IT subject")),
)


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
    tagType = models.CharField(max_length=3, choices=TAG_CHOICES, verbose_name=_("Tag type"))
    value = models.CharField(max_length=150, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.tagType + ' : ' + self.value


def imagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%s" % (now.year, now.month, filename)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', verbose_name=_("Author"))
    created = models.DateTimeField(auto_now=True, verbose_name=_("Creation time"))
    headImage = models.ImageField(upload_to=imagePath, height_field=None, width_field=None, max_length=100)
    titleImage = models.ImageField(upload_to=imagePath, height_field=None, width_field=None, max_length=100)
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    post = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    tags = models.ManyToManyField(Tag, verbose_name=_("Tags"))
    metaTitle = models.CharField(max_length=150, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True, verbose_name=_("Is draft"))
    mapSize = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title


class PostMap(models.Model):
    post = models.ForeignKey(Post, verbose_name=_("Post"))
    place = models.CharField(max_length=150, verbose_name=_("Place"))
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Post map direction")
        verbose_name_plural = _("Post map directions")
        ordering = ('order',)

    def __unicode__(self):
        return self.place


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment_author', verbose_name=_("Comment author"))
    post = models.ForeignKey(Post, verbose_name=_("Post"))
    text = models.TextField(blank=True, null=True, verbose_name=_("Comment body"))
    created = models.DateTimeField(auto_now=True, verbose_name=_("Creation time"))
    repliedTo = models.ForeignKey('self', blank=True, null=True, verbose_name=_("Replied to"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ('-created', 'id')

    def __unicode__(self):
        return self.post
