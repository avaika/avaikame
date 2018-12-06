from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from project.travel.models import Post as TravelPost, Tag as TravelTag


class StaticSitemap(Sitemap):
    priority = 0.5
    protocol = 'https'
    changefreq = 'weekly'
    i18n = True

    def items(self):
        return ['index', 'books']

    def location(self, item):
        return reverse(item)


class TravelPostSitemap(Sitemap):
    changefreq = "weekly"
    protocol = 'https'
    priority = 0.5
    i18n = True

    def items(self):
        return TravelPost.objects.filter(draft=False)

    def lastmod(self, obj):
        return obj.updated


class TravelTagSitemap(Sitemap):
    changefreq = "monthly"
    protocol = 'https'
    priority = 0.5
    i18n = True

    def items(self):
        return TravelTag.objects.all()
