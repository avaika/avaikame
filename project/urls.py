from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from project.sitemap import TravelPostSitemap, TravelTagSitemap, StaticSitemap
admin.autodiscover()

sitemaps = {
    'static': StaticSitemap,
    'travel': TravelPostSitemap,
    'travel_tag': TravelTagSitemap,
}

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^favicon\.ico$',
        RedirectView.as_view(url='/static/base/img/favicon.ico',
                             permanent=True)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),
    url(r'^sudo/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/passwordsent/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^i/', include('project.travel.urls')),
    url(r'^lists/', include('project.lists.urls')),
    url(r'^books/', include('project.books.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns += patterns(url(r'^__debug__/',
    # include(debug_toolbar.urls)),)

handler404 = 'project.travel.views.error404'
handler500 = 'project.travel.views.error500'
