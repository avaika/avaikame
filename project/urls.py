from django.urls import include, re_path
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from project.sitemap import TravelPostSitemap, TravelTagSitemap, StaticSitemap

sitemaps = {
    'static': StaticSitemap,
    'travel': TravelPostSitemap,
    'travel_tag': TravelTagSitemap,
}

urlpatterns = [
re_path(r'^favicon\.ico$',
        RedirectView.as_view(url='/static/base/img/favicon.ico',
                             permanent=True)),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),
    re_path(r'^sudo/', admin.site.urls),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += i18n_patterns(
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    re_path(r'^i/', include('project.travel.urls')),
    re_path(r'^lists/', include('project.lists.urls')),
    re_path(r'^books/', include('project.books.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]

handler404 = 'project.travel.views.error404'
handler500 = 'project.travel.views.error500'
