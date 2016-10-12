# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.conf import settings


def site_processor(request):
    return {'site': Site.objects.get_current()}


def debug_processor(request):
    return {'debug': settings.DEBUG}
