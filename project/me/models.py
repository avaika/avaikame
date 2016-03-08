# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
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


class Category(models.Model):
    headImage = models.ImageField(upload_to=headImagePath, blank=True, height_field=None, width_field=None, max_length=100)
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


class Country(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))
    flag = models.ImageField(upload_to='flags/', height_field=None,
                             blank=True, null=True,
                             width_field=None, max_length=100,
                             verbose_name="Country flag")

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __unicode__(self):
        return self.value


class City(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __unicode__(self):
        return self.value


class Tag(models.Model):
    value = models.CharField(max_length=150, verbose_name=_("Title"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def save(self, *args, **kwargs):
        cat = self.value.find('_')
        self.category = Category.objects.get(slug=self.value[:cat])
        self.value = self.value[cat+1:]
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(User, related_name='post_author', verbose_name=_("Author"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    created = models.DateTimeField(editable=True, blank=True, verbose_name=_("Creation time"))
    headImage = models.ImageField(upload_to=headImagePath, blank=True, height_field=None,
                                  width_field=None, max_length=100,
                                  verbose_name="Head image 3863x1524")
    titleImage = models.ImageField(upload_to=imagePath, blank=True, height_field=None,
                                   width_field=None, max_length=100,
                                   verbose_name="Title image 1980x1315")
    title = models.CharField(max_length=150, verbose_name=_("Title"))
    slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
    post = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))
    country = models.ForeignKey(Country, verbose_name=_("Country"))
    cities = models.ManyToManyField(City, blank=True, verbose_name=_("Cities"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))
    metaTitle = models.CharField(max_length=150, blank=True, verbose_name=_("Meta title"))
    metaDesc = models.CharField(max_length=150, blank=True, verbose_name=_("Meta description"))
    draft = models.BooleanField(default=True, blank=True, verbose_name=_("Is draft"))
    mapSize = models.IntegerField(blank=True, null=True)
    sources = models.TextField(blank=True, null=True, verbose_name=_("Sources"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ('-created',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_redirect', kwargs={'pk': self.id})

    def headImage_tag(self):
        if self.headImage:
            return u'<img src="/media/%s" height="100px" />' % self.headImage
        else:
            return
    headImage_tag.short_description = 'Image'
    headImage_tag.allow_tags = True

    def titleImage_tag(self):
        if self.titleImage:
            return u'<img src="/media/%s" height="100px" />' % self.titleImage
        else:
            return
    titleImage_tag.short_description = 'Image'
    titleImage_tag.allow_tags = True


class PostPhoto(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField(blank=True, null=True, verbose_name=_("Post body"))
    photo = models.ImageField(upload_to=imagePath, blank=True, height_field=None, width_field=None, max_length=100)
    panorama = models.BooleanField(default=False, blank=True, verbose_name=_("Is panorama"))
    private = models.BooleanField(default=False, blank=True, verbose_name=_("Is private"))
    photoRight = models.ImageField(upload_to=imagePath, blank=True, height_field=None, width_field=None, max_length=100)
    panoramaRight = models.BooleanField(default=False, blank=True, verbose_name=_("Is panorama"))
    privateRight = models.BooleanField(default=False, blank=True, verbose_name=_("Is private"))

    def photo_tag(self):
        if self.photo:
            return u'<img src="/media/%s" height="100px" />' % self.photo
        else:
            return
    photo_tag.short_description = 'Image'
    photo_tag.allow_tags = True

    def photoRight_tag(self):
        if self.photoRight:
            return u'<img src="/media/%s" height="100px" />' % self.photoRight
        else:
            return
    photoRight_tag.short_description = 'Image'
    photoRight_tag.allow_tags = True


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
