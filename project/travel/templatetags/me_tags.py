from django.template import Library
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language
from ..models import Post

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


@register.simple_tag()
def travel_count_posts():
    return Post.objects.filter(draft=False).count()


def get_flag_current(item, first, last):
    if item['created'] <= first.created and item['created'] >= last.created:
        item['current'] = True
    else:
        item['current'] = False
    return item


@register.assignment_tag()
def flags(page_posts):
    posts = Post.objects.filter(draft=False, country__flag__isnull=False).order_by('-created').values('created', 'country__value', 'country__flag', 'country_ball')
    first = page_posts[0]
    last = page_posts[len(page_posts) - 1]
    flags = []
    for item in posts:
        if len(flags) > 0:
            if flags[-1]['country__value'] == item['country__value']:
                # needed in case flag already popped up on prev page
                if not flags[-1]['current']:
                    flags[-1] = get_flag_current(item, first, last)
                continue
        item = get_flag_current(item, first, last)
        item['flag_url'] = item['country__value'].lower().replace(" ", "_")
        flags.append(item)
    return flags


@register.assignment_tag()
def uniq_flags(first=False, last=False):
    posts = Post.objects.filter(draft=False, country__flag__isnull=False).order_by('-created').values('country__value', 'country__flag', 'country__ball')
    flags = []
    for item in posts:
        item['flag_url'] = item['country__value'].lower().replace(" ", "_")
        if item not in flags:
            flags.append(item)
    return flags
