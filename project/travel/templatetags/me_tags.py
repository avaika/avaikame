from django.template import Library
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language
from ..models import Post
from datetime import datetime

register = Library()


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    """
    Get active page's url by a specified language
    Usage: {% change_lang 'en' %}
    """

    cur_language = get_language()
    path = context['request'].path
    try:
        url_parts = resolve(path)
    except:
        # need to finish here. e.g. for 404
        return ""
    url = path

    try:
        activate(lang)
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        activate(cur_language)
    return "%s" % url


@register.assignment_tag()
def latest_posts():
    return Post.objects.filter(draft=False).order_by('-created')[:3]


@register.assignment_tag()
def day_posts():
    now = datetime.now()
    day = now.day
    month = now.month
    return Post.objects.filter(draft=False, created__month=month,
                               created__day=day)


@register.simple_tag()
def travel_count_posts():
    return Post.objects.filter(draft=False).count()


@register.assignment_tag()
def flags(page_posts):
    posts = Post.objects.filter(draft=False, country__flag__isnull=False).\
        order_by('-created').values('country__slug',
                                    'country__title_en',
                                    'country__title_ru')
    flags = []
    for item in posts:
        if len(flags) > 0:
            if flags[-1]['country__slug'] == item['country__slug']:
                continue
        flags.append(item)
    return flags


@register.assignment_tag()
def uniq_flags(first=False, last=False):
    posts = Post.objects.filter(draft=False, country__flag__isnull=False).\
        order_by('-created').values('country__slug',
                                    'country__title_en',
                                    'country__title_ru',
                                    'country__ball')
    flags = []
    for item in posts:
        if item not in flags:
            flags.append(item)
    return flags
