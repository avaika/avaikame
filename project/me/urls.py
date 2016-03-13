from project.me import views
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<slug>[^/]*)/$', views.category, name='category'),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_redirect, name='page_redirect'),
    url(r'^tag/(?P<tag>.*)/$', views.tag, name='tag_list'),
    url(r'^country/(?P<country>.*)/$', views.country, name='country_list'),
    url(r'^page/(?P<pk>[0-9]+)/(?P<slug>.*)/$', views.page_display, name='page_display'),
    url(r'^directions/(?P<post>[0-9]+)/$', views.directions, name='directions'),
]
