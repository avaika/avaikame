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
        url_parts = resolve("/" + str(cur_language) + path)
    url = path

    try:
        activate(lang)
        url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
    finally:
        activate(cur_language)
    return "%s" % url


@register.assignment_tag()
def latest_posts():
    latest_posts = Post.objects.filter(draft=False).order_by('-created')[:3]
    return latest_posts


@register.simple_tag()
def count_posts(category):
    num = Post.objects.filter(draft=False, category__slug=category).count()
    return num
