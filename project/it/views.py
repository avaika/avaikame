from django.http import Http404
# from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from models import Post, ITTag


class ITListView(ListView):
    queryset = Post.objects.filter(draft=False)
    paginate_by = 10
    context_object_name = "posts"
    template_name = 'it/list.html'

    def get_context_data(self, **kwargs):
        context = super(ITListView, self).get_context_data(**kwargs)
        context['tags'] = ITTag.objects.all
        return context

main = ITListView.as_view()


class TagView(TemplateView):
    context_object_name = "posts"
    template_name = 'it/list_tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(draft=False, tags__value__contains=kwargs['tag'])
        context['tags'] = ITTag.objects.all
        return context

tag = TagView.as_view()


class PageRedirectView(RedirectView):
    pattern_name = 'it_page_display'

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
    template_name = 'it/page_detail.html'

    def get_object(self):
        object = super(PageDetailView, self).get_object()
        if object.draft:
            if not self.request.user.is_superuser:
                raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        obj = super(PageDetailView, self).get_object()
        context['tags'] = ITTag.objects.all
        context['random_post'] = Post.objects.filter(draft=False).exclude(pk=obj.pk).order_by('?')[0]
        return context

page_display = PageDetailView.as_view()
