from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from models import Post, PostMap

# from django.contrib.auth import get_user_model
# User = get_user_model()


class BlogListView(ListView):
    queryset = Post.objects.filter(draft=False)
    paginate_by = 10
    context_object_name = "posts"
    template_name = 'me/list.html'

main = BlogListView.as_view()


class TagView(TemplateView):
    context_object_name = "posts"
    template_name = 'me/list_tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(draft=False, tags__value__contains=kwargs['tag'])
        return context

tag = TagView.as_view()


class PageRedirectView(RedirectView):
    pattern_name = 'page_display'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            page = get_object_or_404(Post, pk=kwargs['pk'])
        else:
            page = get_object_or_404(Post, pk=kwargs['pk'], draft=False)
        kwargs['slug'] = page.slug
        return super(PageRedirectView, self).get_redirect_url(*args, **kwargs)

page_redirect = PageRedirectView.as_view()


class PageDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = 'me/page_detail.html'

    def get_object(self):
        object = super(PageDetailView, self).get_object()
        if object.draft:
            if not self.request.user.is_superuser:
                raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        obj = super(PageDetailView, self).get_object()
        context['random_posts'] = Post.objects.filter(draft=False).exclude(pk=obj.pk).order_by('?')[:3]
        return context

page_display = PageDetailView.as_view()


class DirectionView(TemplateView):
    template_name = "me/directions.html"
    context_object_name = "waypts"

    def get_context_data(self, **kwargs):
        context = super(DirectionView, self).get_context_data(**kwargs)
        context['waypts'] = PostMap.objects.filter(post=kwargs['post'])
        return context

directions = DirectionView.as_view()


def error404(request, template='404.html'):
    return render(request, template, status=404)


def error500(request, template='500.html'):
    return render(request, template, status=500)
