# -*- coding: utf-8 -*-
from django.core.management.base import NoArgsCommand
from BeautifulSoup import BeautifulSoup
from project.me.models import Country
from django.conf import settings
import urllib2
import json
import re
import os


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        req = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=parse&page=Gallery_of_sovereign_state_flags&format=json&prop=text")
        page_json = json.load(req)
        page = BeautifulSoup(str(page_json["parse"]["text"]))

        flag_dir = settings.MEDIA_ROOT + "/flags"
        if not os.path.exists(flag_dir):
            os.makedirs(flag_dir)

        for img in page.findAll('img', attrs={'alt': re.compile('Flag of.*')}):
            name = img.get('alt').replace('Flag of', '').strip().replace('the ', '')
            country, created = Country.objects.get_or_create(value=name)
            if created or country.flag != name:
                flag_file = "flags/" + name.replace(" ", "_").lower() + ".png"
                country.flag = flag_file
                im_file = open(settings.MEDIA_ROOT + "/" + flag_file, "wb")
                im_file.write(urllib2.urlopen("https:" + img.get('src')).read())
                im_file.close()
                country.save()
