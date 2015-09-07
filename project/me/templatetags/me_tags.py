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

    path = context['request'].path
    url_parts = resolve(path)
    url = path
    cur_language = get_language()

    # Actually this dirty hack is applied due to some issues with reverse
    # TemplateView urls.
    # Will check a bit more detailed later.
    if url_parts.url_name != "index":
        try:
            activate(lang)
            url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
        finally:
            activate(cur_language)
    else:
        url = "/" + str(lang) + "/"
    return "%s" % url


@register.assignment_tag()
def latest_posts():
    latest_posts = Post.objects.filter(draft=False).order_by('-created')[:3]
    return latest_posts


@register.simple_tag()
def count_posts(category):
    num = Post.objects.filter(draft=False, category__slug=category).count()
    return num
