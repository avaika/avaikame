# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from BeautifulSoup import BeautifulSoup
from project.books.models import Author, Book, Genre
try:
        from urllib.request import Request, urlopen  # Python 3
except:
        from urllib2 import Request, urlopen  # Python 2


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        page_ru = Request(options['url'][0])
        optionsPage = urlopen(page_ru)
        soup = BeautifulSoup(optionsPage)
        book_name_ru = soup.find('title').contents[0][:-12].encode('utf-8')
        author_ru_raw = soup.find('span', attrs={'data-wikidata-property-id': 'P50'}).contents[0]
        author_name_ru = author_ru_raw.contents[0].encode('utf-8')
        author_link_ru = "https://ru.wikipedia.org" + author_ru_raw['href']
        try:
            book_genre = soup.find('span', attrs={'data-wikidata-property-id': 'P136'}).text.encode('utf-8')
        except:
            book_genre = 'default'
        try:
            book_year = soup.find('span', attrs={'data-wikidata-property-id': 'P577'}).text
        except:
            book_year = 0
        book_en = soup.find('li', attrs={'class': 'interlanguage-link interwiki-en'}).contents[0]
        book_name_en = book_en['title'][:-13]
        book_link_en = book_en['href']
        genre, _ = Genre.objects.get_or_create(value_ru=book_genre, value_en='change_me')
        author_en = urlopen(Request(author_link_ru))
        result = BeautifulSoup(author_en)
        author_en_raw = result.find('li', attrs={'class': 'interlanguage-link interwiki-en'}).contents[0]
        author_name_en = author_en_raw['title'][:-13]
        author_link_en = author_en_raw['href']
        author, _ = Author.objects.get_or_create(value_ru=author_name_ru,
                                                 wiki_url_ru=author_link_ru,
                                                 value_en=author_name_en,
                                                 wiki_url_en=author_link_en)
        book, _ = Book.objects.get_or_create(title_ru=book_name_ru,
                                             title_en=book_name_en,
                                             year=book_year,
                                             wiki_url_ru=options['url'][0],
                                             wiki_url_en=book_link_en)
        book.author = [author, ]
        book.genre = [genre, ]
        book.save()
