# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from sorl.thumbnail import get_thumbnail
from datetime import datetime
import uuid


# I have no idea why I created this model
# Probably need to check dependencies and remove it one day...
class User(AbstractUser):
    notifyEmail = models.EmailField(max_length=150, blank=True, null=True)
    notifyGlobal = models.BooleanField(default=False)
    notifyNewposts = models.BooleanField(default=False)
    notifyReplied = models.BooleanField(default=False)
    registered = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ('-registered', 'id')
        get_latest_by = 'registered'

    def __unicode__(self):
        return unicode(self.username)


def headImagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_head_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%d/%s" % (now.year, now.month, now.day, filename)


def imagePath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "avaika_title_%s.%s" % (str(uuid.uuid4())[1:8], ext)
    now = datetime.now()
    return "%d/%d/%d/%s" % (now.year, now.month, now.day, filename)


class Country(models.Model):
    slug = models.CharField(max_length=150, verbose_name=_("Slug"))
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    flag = models.ImageField(upload_to='flags/', height_field=None,
                             blank=True, null=True,
                             width_field=None, max_length=100,
                             verbose_name="Country flag")
    ball = models.ImageField(upload_to='balls/', height_field=None,
                             blank=True, null=True,
                             width_field=None, max_length=100,
                             verbose_name="Country ball")
    example = models.ImageField(upload_to='ball_examples/', height_field=None,
                                blank=True, null=True,
                                width_field=None, max_length=100,
                                verbose_name="Example")
    psdfile = models.FileField(upload_to='ball_psd/', blank=True, null=True,
                               max_length=100, verbose_name="PSD file")
    worky = models.BooleanField(default=False, blank=True,
                                verbose_name=_("Scheduled?"))
    ready = models.BooleanField(default=False, blank=True,
                                verbose_name=_("Ready?"))

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "slug__icontains",)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    value = models.CharField(max_length=150, blank=True, null=True,
                             verbose_name=_("Title"))
    slug = models.CharField(max_length=150, verbose_name=_("Tag url"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('tag_list', kwargs={'tag': self.slug})

    def save(self, *args, **kwargs):
        if not self.value_en:
            self.value_en = self.slug.title()
        if not self.value_ru:
            self.value_ru = self.slug
        if " " in self.slug:
            self.slug = self.slug.replace(" ", "_")
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author',
                               verbose_name=_("Author"))
    created = models.DateTimeField(editable=True, blank=True,
                                   verbose_name=_("Creation time"))
    updated = models.DateTimeField(auto_now=True, blank=True,
                                   verbose_name=_("Update time"))
    headImage = models.ImageField(upload_to=headImagePath, blank=True,
                                  height_field=None,
                                  width_field=None, max_length=100,
                                  verbose_name="Head image 3863x1524")
    titleImage = models.ImageField(upload_to=imagePath, blank=True,
                                   height_field=None,
                                   width_field=None, max_length=100,
                                   verbose_name="Title image 1980x1315")
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    country = models.ForeignKey(Country, verbose_name=_("Country"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))
    metaDesc = models.CharField(max_length=150, blank=True,
                                verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True,
                                verbose_name=_("Is draft"))
    checked = models.BooleanField(default=False, blank=True,
                                verbose_name=_("Verified by editor"))
    sources = models.TextField(blank=True, null=True, verbose_name=_("Sources"))
    mapDirections = models.TextField(blank=True, null=True,
                                     verbose_name=_("Map link"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_display', kwargs={'pk': self.id, 'slug': self.slug})

    def headImage_tag(self):
        if self.headImage:
            return u'<img src="%s" height="100px" />' % (get_thumbnail(self.headImage,
                                                                       "150x150",
                                                                       quality=95).url)
        else:
            return
    headImage_tag.short_description = 'Image'
    headImage_tag.allow_tags = True

    def titleImage_tag(self):
        if self.titleImage:
            return u'<img src="%s" height="100px" />' % (get_thumbnail(self.titleImage,
                                                                       "150x150",
                                                                       quality=95).url)
        else:
            return
    titleImage_tag.short_description = 'Image'
    titleImage_tag.allow_tags = True


class PostPhoto(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    comment = models.TextField(blank=True, null=True, verbose_name=_("Editor comment"))
    photo = models.ImageField(upload_to=imagePath, blank=True,
                              height_field=None, width_field=None,
                              max_length=100)
    panorama = models.BooleanField(default=False, blank=True,
                                   verbose_name=_("Is panorama"))
    source = models.CharField(max_length=1000, blank=True, null=True,
                              verbose_name=_("Photo source"))
    photoRight = models.ImageField(upload_to=imagePath, blank=True,
                                   height_field=None, width_field=None,
                                   max_length=100)
    panoramaRight = models.BooleanField(default=False, blank=True,
                                        verbose_name=_("Is panorama"))
    sourceRight = models.CharField(max_length=1000, blank=True, null=True,
                                   verbose_name=_("Photo source"))

    def photo_tag(self):
        if self.photo:
            return u'<img src="%s" height="100px" />' % (get_thumbnail(self.photo,
                                                                       "150x150",
                                                                       quality=95).url)
        else:
            return
    photo_tag.short_description = 'Image'
    photo_tag.allow_tags = True

    def photoRight_tag(self):
        if self.photoRight:
            return u'<img src="%s" height="100px" />' % (get_thumbnail(self.photoRight,
                                                                       "150x150",
                                                                       quality=95).url)
        else:
            return
    photoRight_tag.short_description = 'Image'
    photoRight_tag.allow_tags = True


class PostLinks(models.Model):
    post = models.ForeignKey(Post)
    url = models.CharField(max_length=1000, verbose_name=_("Link"))
    description = models.CharField(max_length=256,
                                   verbose_name=_("Link description"))
    isPoint = models.BooleanField(default=True, blank=True,
                                  verbose_name=_("Is point?"))
    published = models.BooleanField(default=True, blank=True,
                                    verbose_name=_("Is published?"))
