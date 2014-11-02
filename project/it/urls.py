from project.it import views
from django.conf.urls import url, patterns

urlpatterns = patterns(
    '',
    url(r'^$', views.main),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='it_page_redirect'),
    url(r'^tag/(?P<tag>.*)/$', views.tag, name='it_tag_list'),
    url(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='it_page_display'),
)
