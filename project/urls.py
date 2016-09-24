from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
admin.autodiscover()

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/base/img/favicon.ico', permanent=True)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    # to be replaced by redirect
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),
    url(r'^sudo/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^i/', include('project.travel.urls')),
    url(r'^blog/', include('project.blog.urls')),
    url(r'^books/', include('project.books.urls')),
)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'project.travel.views.error404'
handler500 = 'project.travel.views.error500'
