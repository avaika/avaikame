# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from project.travel.models import Post, PostLinks
try:
        from urllib.request import Request, urlopen  # Python 3
except:
        from urllib2 import Request, urlopen  # Python 2


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('post', nargs='+', type=int)
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        point_url_ru = Request(options['url'][0])
        post_id = options['post'][0]
        post = Post.objects.get(id=post_id)

        optionsPage = urlopen(point_url_ru)
        soup = BeautifulSoup(optionsPage)
        point_title_ru = soup.find('title').contents[0][:-12].encode('utf-8')
        point_en = soup.find('li', attrs={'class': 'interlanguage-link interwiki-en'}).contents[0]
        point_title_en = point_en['title'][:-13].encode('utf-8')
        point_url_en = point_en['href'].encode('utf-8')
        point, _ = PostLinks.objects.get_or_create(post=post,
                                                   url_ru=options['url'][0],
                                                   url_en=point_url_en,
                                                   description_ru=point_title_ru,
                                                   description_en=point_title_en)
        point.save()
