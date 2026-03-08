# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from project.lists.models import List, Entry
from urllib.request import Request, urlopen


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        page_en_url = options['url'][0]
        page_en = Request(page_en_url)
        optionsPage = urlopen(page_en)
        soup = BeautifulSoup(optionsPage, 'html.parser')
        event_name_en = soup.find('title').contents[0][:-12]
        source_ru = 'wikipedia'
        source_en = 'wikipedia'
        try:
          page_ru = soup.find('li', attrs={'class': 'interlanguage-link interwiki-ru'}).contents[0]
          page_ru_url = page_ru['href']
          event_name_ru = page_ru['title'][:-13]
        except:
          page_ru_url = page_en_url
          source_ru = 'wikipedia (en)'
          event_name_ru = event_name_en
        print(event_name_en)

        listItem = List.objects.get(id=3)
        entry, _ = Entry.objects.get_or_create(listItem=listItem,
                                               published=False,
                                               item_ru=event_name_ru,
                                               item_en=event_name_en,
                                               link_ru=page_ru_url,
                                               link_en=page_en_url,
                                               value_ru=source_ru,
                                               value_en=source_en,
                                               ImageSource='<a href=""></a>')
        entry.save()
