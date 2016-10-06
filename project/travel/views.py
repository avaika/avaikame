from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView, DetailView, ListView, UpdateView
from models import Post, PostMap, PostPhoto
from django.core.urlresolvers import reverse
from django.forms import modelform_factory


class CategoryListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"
    template_name = "me/list.html"

    def get_queryset(self):
        qs = super(CategoryListView, self).get_queryset()
        return qs.filter(draft=False)

category = CategoryListView.as_view()


class TagView(TemplateView):
    context_object_name = "posts"
    template_name = "me/list_search.html"

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(draft=False, tags__value__contains=kwargs['tag']).distinct()
        context['tag'] = kwargs['tag']
        return context

tag = TagView.as_view()


class CountryView(TemplateView):
    context_object_name = "posts"
    template_name = "me/list_search.html"

    def get_context_data(self, **kwargs):
        context = super(CountryView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(country__value=self.kwargs['country'], draft=False)
        context['country'] = kwargs['country']
        return context

country = CountryView.as_view()


class PageRedirectView(RedirectView):
    pattern_name = 'page_display'

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
    template_name = "me/page_detail.html"

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
        next_item = Post.objects.filter(created__gt=context['post'].created, draft=False).order_by('created')
        if next_item:
            context['next'] = next_item[0]
        prev_item = Post.objects.filter(created__lt=context['post'].created, draft=False).order_by('-created')
        if prev_item:
            context['prev'] = prev_item[0]
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


class TranslateView(UpdateView):
    model = PostPhoto
    context_object_name = "text"

    def get_template_names(self):
        raise NotImplementedError  # TODO

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_superuser:
            raise Http404()
        return super(TranslateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('translate', None, kwargs={})

    def get_form_fields(self):
        fields = ['text', 'comment', 'music', 'dictor']
        if self.object.techReqs is not None:
            fields.append('techReqs')
        if self.object.chrono is not None:
            fields.append('chrono')
        return fields

    def get_form_class(self):
        return modelform_factory(PostPhoto, fields=self.get_form_fields())


def error404(request, template='404.html'):
    return render(request, template, status=404)


def error500(request, template='500.html'):
    return render(request, template, status=500)
