from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from models import Post, PostMap, Tag, PostPhoto

# from django.contrib.auth import get_user_model
# User = get_user_model()
TRAVEL_CAT = 1
TRAVEL_SLUG = 'me'


class CategoryListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(draft=False, category__slug=self.kwargs['slug'])

    def get_template_names(self, *args, **kwargs):
        if self.kwargs['slug'] == TRAVEL_SLUG:
            return 'me/list.html'
        else:
            return 'it/list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        if slug != TRAVEL_SLUG:
            context['tags'] = Tag.objects.filter(category__slug=slug)
        return context

category = CategoryListView.as_view()


class TagView(TemplateView):
    context_object_name = "posts"

    def get_template_names(self):
        tag = Tag.objects.get(value=self.kwargs['tag'])
        if tag.category_id == TRAVEL_CAT:
            return 'me/list_tag.html'
        else:
            return 'it/list_tag.html'

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag = Tag.objects.get(value=self.kwargs['tag'])
        if tag.category_id != TRAVEL_CAT:
            context['tags'] = Tag.objects.filter(category=tag.category)
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

    def get_template_names(self):
        post = self.get_object()
        if post.category_id == TRAVEL_CAT:
            return 'me/page_detail.html'
        else:
            return 'it/page_detail.html'

    def get_object(self):
        object = super(PageDetailView, self).get_object()
        if object.draft:
            if not self.request.user.is_superuser:
                raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        obj = super(PageDetailView, self).get_object()
        context['text_chunks'] = PostPhoto.objects.filter(post_id=context['post'].id)
        next_item = Post.objects.filter(pk__gt=context['post'].id, category=context['post'].category).order_by('created')
        if next_item:
            context['next'] = next_item[0]
        prev_item = Post.objects.filter(pk__lt=context['post'].id, category=context['post'].category).order_by('-created')
        if prev_item:
            context['prev'] = prev_item[0]
        if obj.category_id != TRAVEL_CAT:
            context['tags'] = Tag.objects.filter(category=obj.category)
            context['random_post'] = Post.objects.filter(draft=False, category=obj.category).exclude(pk=obj.pk).order_by('?')[:1]
        else:
            context['random_posts'] = Post.objects.filter(draft=False, category=obj.category).exclude(pk=obj.pk).order_by('?')[:3]
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
