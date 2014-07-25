# from django.core.urlresolvers import reverse
# from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.http import Http404
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.generic import RedirectView, TemplateView, DetailView, ListView
from django.core.mail import send_mail
from models import Post, PostMap
# from django.contrib.auth import get_user_model
from django.db.models import Sum

# User = get_user_model()


class BlogListView(ListView):
    queryset = Post.objects.filter(draft=False)
    paginate_by = 10
    context_object_name = "posts"
    template_name = 'blog/list.html'

main = BlogListView.as_view()


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
    template_name = 'blog/page_detail.html'

    def get_object(self):
        object = super(PageDetailView, self).get_object()
        if object.draft:
            if not self.request.user.is_superuser:
                raise Http404
        return object

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context['random_posts'] = Post.objects.filter(draft=False).order_by('?')[:3]
        return context

page_display = PageDetailView.as_view()


class DirectionView(TemplateView):
    template_name = "blog/directions.html"
    context_object_name = "waypts"

    def get_context_data(self, **kwargs):
        context = super(DirectionView, self).get_context_data(**kwargs)
        context['waypts'] = PostMap.objects.filter(post=kwargs['post']).order_by('-id')
        return context

directions = DirectionView.as_view()


class InvoiceView(TemplateView):
    template_name = "dashboard/invoice.html"

    def get_context_data(self, **kwargs):
        context = super(InvoiceView, self).get_context_data(**kwargs)
        transactions = Post.objects.filter(user=self.request.user, payment__isnull=True)
        if transactions.count() > 0:
            summ = transactions.aggregate(s=Sum('summ'))['s']
            subject = u"[ cashout ] {user}".format(user=self.request.user)
            message = u"Requested {summ} rubles via {paym} system {pay_num}.".format(summ=summ,
                                                                                     paym=self.request.user.payment,
                                                                                     pay_num=self.request.user.phone)
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.CONTACTS,
            )
            print self.request.user.email
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.request.user.email],
            )
        context['transactions'] = transactions
        return context

invoice = InvoiceView.as_view()


def error404(request, template='404.html'):
    return render(request, template, status=404)


def error500(request, template='500.html'):
    return render(request, template, status=500)
