from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^favicon\.ico$', RedirectView.as_view(url='/static/base/img/favicon.ico')),
    (r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt')),
    (r'^accounts/', include('project.registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('project.blog.urls')),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adminfiles/', include('project.adminfiles.urls')),
    url(r'^tags_input/', include('tags_input.urls', namespace='tags_input')),
    url(r'^accounts/passwordsent/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'project.blog.views.error404'
handler500 = 'project.blog.views.error500'
