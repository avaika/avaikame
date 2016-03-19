from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from models import Post, Tag


class AllListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"
    template_name = "blog/list_tag.html"

    def get_queryset(self):
        qs = super(AllListView, self).get_queryset()
        return qs.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super(AllListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

all_posts = AllListView.as_view()


class CategoryListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"
    template_name = "blog/list_tag.html"

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(draft=False, category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['tags'] = Tag.objects.filter(category__slug=slug)
        return context

category = CategoryListView.as_view()


class TagView(TemplateView):
    context_object_name = "posts"
    template_name = "blog/list_tag.html"

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['posts'] = Post.objects.filter(draft=False, tags__value__contains=kwargs['tag'])
        return context

tag = TagView.as_view()


class PageRedirectView(RedirectView):
    pattern_name = 'blog_page_display'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_superuser:
            page = get_object_or_404(Post, pk=kwargs['pk'])
        else:
            page = get_object_or_404(Post, pk=kwargs['pk'], draft=False)
        kwargs['slug'] = page.slug
        return super(PageRedirectView, self).get_redirect_url(*args, **kwargs)

page_redirect = PageRedirectView.as_view(permanent=True)


class PageDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/page_detail.html"

    def get_object(self):
        object = super(PageDetailView, self).get_object()
        if object.draft:
            if not self.request.user.is_superuser:
                raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        obj = super(PageDetailView, self).get_object()
        next_item = Post.objects.filter(pk__gt=context['post'].id, category=context['post'].category).order_by('created')
        if next_item:
            context['next'] = next_item[0]
        prev_item = Post.objects.filter(pk__lt=context['post'].id, category=context['post'].category).order_by('-created')
        if prev_item:
            context['prev'] = prev_item[0]
        context['tags'] = Tag.objects.all()
        context['random_post'] = Post.objects.filter(draft=False, category=obj.category).exclude(pk=obj.pk).order_by('?')[:1]
        return context

page_display = PageDetailView.as_view()
