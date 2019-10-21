# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from project.travel.models import Post, PostLinks
import json
try:
        from urllib.request import urlopen  # Python 3
except:
        from urllib2 import urlopen  # Python 2


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('post', nargs='+', type=int)
        parser.add_argument('title', nargs='+', type=str)

    def handle(self, *args, **options):
        post_id = options['post'][0]
        post = Post.objects.get(id=post_id)
        title = options['title'][0]
        base_api = 'https://en.wikipedia.org/w/api.php?action=query&format=json&titles='

        page_info_url = base_api + title + "&prop=info&inprop=url"
        lang_info_url = base_api + title + "&prop=langlinks&llprop=url&lllang=ru"

        page_info_raw = urlopen(page_info_url)
        lang_info_raw = urlopen(lang_info_url)

        page_info = json.load(page_info_raw)
        for page in page_info['query']['pages']:
            point_title_en = page_info['query']['pages'][page]['title']
            point_url_en = page_info['query']['pages'][page]['fullurl']
            break

        lang_info = json.load(lang_info_raw)
        if 'langlinks' in lang_info['query']['pages'][page]:
            for langs in lang_info['query']['pages'][page]['langlinks']:
                if langs['lang'] == 'ru':
                    point_title_ru = langs['*']
                    point_url_ru = langs['url']
        else:
            point_title_ru = point_title_en + ' (en)'
            point_url_ru = point_url_en
        point, _ = PostLinks.objects.get_or_create(post=post,
                                                   url_ru=point_url_ru,
                                                   url_en=point_url_en,
                                                   description_ru=point_title_ru,
                                                   description_en=point_title_en)
        point.save()
