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
def count_posts(category):
    return Post.objects.filter(draft=False, category__slug=category).count()


@register.assignment_tag()
def flags():
    posts = Post.objects.filter(draft=False, country__flag__isnull=False).order_by('-created').values('country__value', 'country__flag')
    flags = []
    for item in posts:
        # exclude default for migration time. then it's not needed and can be
        # removed
        if len(flags) == 0 and item['country__value'] != "default":
            flags.append(item)
        elif len(flags) > 0:
            if flags[-1] != item and item['country__value'] != "default":
                flags.append(item)
    # limited to 23 until slider will be developed in front end part
    if len(flags) > 23:
        flags = flags[:23]
    return flags
